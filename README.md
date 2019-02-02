# Mastermind

Simple web application for playing Mastermind.

## Getting ready

1) Clone this repository.

```sh
git clone git@github.com:alemasseroli/mastermind.git
```

2) Enter project's directory.

```sh
cd mastermind
```

3) Activate your virtualenv (Python 2.7).

4) Install the necessary requirements.

```sh
pip install -r requirements.txt
```

## Running the tests

```sh
python -m tests.codemaker_tests
python -m tests.mastermind_tests
```

## Starting the API

```sh
python -m mastermind.app
```

### Usage

- Creating a new game.

```sh
curl -XPOST localhost:8080/mastermind/create
```

- Making a guess.

```sh
curl -XPUT localhost:8080/mastermind/guess -d '<SPACE_SEPARATED_COLORS>'
```

- Getting the current game's historic plays.

```sh
curl -XGET localhost:8080/mastermind/historic
```

### Example

```sh
curl -XPOST localhost:8080/mastermind/create
```
> {"Response": "New game created"}

```sh
curl -XPUT localhost:8080/mastermind/guess -d 'RED RED RED RED'
```
> {"Response": ["BLACK"]}

```sh
curl -XPUT localhost:8080/mastermind/guess -d 'BLUE BLUE BLUE BLUE'
```
> {"Response": []}


```sh
curl -XGET localhost:8080/mastermind/historic
```

> {"Response": [
    {"output": ["BLACK"], "guess": ["RED", "RED", "RED", "RED"]},
    {"output": [], "guess": ["BLUE", "BLUE", "BLUE", "BLUE"]}
    ]}

...

```sh
curl -XPUT localhost:8080/mastermind/guess -d 'RED GREEN RED YELLOW'
```
> {"Response": "You win!"}
