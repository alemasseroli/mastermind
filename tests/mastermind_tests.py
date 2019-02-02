import json
import unittest

import mastermind.app


class MastermindTests(unittest.TestCase):

    def setUp(self):
        self.app = mastermind.app.app.test_client()

    def test_create_game(self):
        response = self.app.post('/mastermind/create')
        assert response.status_code == 200
        assert 'New game created' in response.data

    def test_guess(self):
        self.app.post('/mastermind/create')
        mastermind.app.codemaker.code = ['RED', 'RED', 'RED', 'RED']
        response = self.app.put(
            '/mastermind/guess',
            data='RED BLUE BLUE BLUE'
        )
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'response' in data
        assert data['response'] == ['BLACK']

    def test_guess_win(self):
        code = ['RED', 'RED', 'RED', 'RED']
        self.app.post('/mastermind/create')
        mastermind.app.codemaker.code = code
        response = self.app.put(
            '/mastermind/guess',
            data=' '.join(code)
        )
        assert response.status_code == 200
        assert 'You win!' in response.data

    def test_guess_lose(self):
        self.app.post('/mastermind/create')
        mastermind.app.codemaker.code = ['BLUE', 'BLUE', 'BLUE', 'BLUE']
        response = None
        for _ in range(mastermind.app.MAX_ATTEMPTS + 1):
            response = self.app.put(
                '/mastermind/guess',
                data='RED RED RED RED'
            )
        assert response.status_code == 200
        assert 'You lose' in response.data

    def test_guess_for_not_started_game_should_fail(self):
        mastermind.app.started = False
        response = self.app.put(
            '/mastermind/guess',
            data='RED RED RED RED'
        )
        assert response.status_code == 400
        assert 'Game not created' in response.data

    def test_invalid_guess_should_fail(self):
        self.app.post('/mastermind/create')
        response = self.app.put(
            '/mastermind/guess',
            data='RED RED'
        )
        assert response.status_code == 400
        assert 'Invalid guess' in response.data

    def test_get_historic_for_not_started_game_should_fail(self):
        mastermind.app.started = False
        response = self.app.get('/mastermind/historic')
        assert response.status_code == 400
        assert 'Game not created' in response.data

    def test_get_historic_for_new_game(self):
        self.app.post('/mastermind/create')
        response = self.app.get('/mastermind/historic')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'response' in data
        assert len(data['response']) == 0

    def test_get_historic_for_played_game(self):
        self.app.post('/mastermind/create')
        mastermind.app.codemaker.code = ['BLUE', 'BLUE', 'BLUE', 'BLUE']
        self.app.put('/mastermind/guess', data='RED RED RED RED')
        self.app.put('/mastermind/guess', data='BLUE RED RED RED')
        response = self.app.get('/mastermind/historic')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'response' in data
        assert len(data['response']) == 2
        assert data['response'][0] == {'guess': ['RED', 'RED', 'RED', 'RED'], 'output': []}
        assert data['response'][1] == {'guess': ['BLUE', 'RED', 'RED', 'RED'], 'output': ['BLACK']}


if __name__ == '__main__':
    unittest.main()
