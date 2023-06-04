# COURSE WORK 3
## Code for the “Account Operations” widget


## Description

Functionality has been implemented that allows you to display a list of the last 5 transactions performed by the client.

```bash
# Sample output for one operation:
14.10.2018 Перевод организации
Visa Platinum 7000 79** **** 6361 -> Счет **9638
82771.72 руб.
```

### Requirements

- The last 5 executed (EXECUTED) operations are displayed
- Operations are separated by an empty line
- The transfer date is presented in the format DD.MM.YYYY (example, 10/14/2018)
- At the top of the list are the most recent transactions (by date)
- The card number is masked and not displayed in its entirety, in the format XXXX XX** **** XXXX (the first 6 digits and the last 4 are visible, divided into blocks of 4 digits separated by a space)
- The account number is masked and not displayed in full, in the format **XXXX
(only the last 4 digits of the account number are visible)

## Data

[operations.json](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json)

## Decision criteria

- The project is posted on github
- The README.md file is formatted
- The project has at least 2 branches, and development is carried out in `develop`, and the stable version at the time of delivery of the project lies in the `main` branch
- The development of the project is carried out in a virtual environment, the project has information about the requirements of the project (dependencies)
- Tests with at least 80% coverage were written for the project
- Tests written in `pytest` or `unittest`
- The project is structured, readable, each function is no more than 50 lines

## How to Use the Project

1.	Clone project from github:
```bash
git@github.com:sergey-raskolenko/cw_3.git
```
2.	Create poetry venv and download dependencies by terminal:
```bash
poetry install
```
3.	Run main.py file from /cw_3/src
4.	To test project with coverage by terminal:
```bash
poetry run pytest –cov
```
