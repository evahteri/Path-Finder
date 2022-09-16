# Data Structures Lab project fall 2022

Path Finder is a algorithm project made for data structures lab course in the University of Helsinki. The project is made with python.

## Weekly reports
- [Week 1](https://github.com/evahteri/Path-Finder/blob/main/documentation/weekly_reports/week1.md)
- [Week 2](https://github.com/evahteri/Path-Finder/blob/main/documentation/weekly_reports/week2.md)

## Documentation
- [Timesheet](https://github.com/evahteri/Path-Finder/blob/main/documentation/timesheet.md)
- [Project specification](https://github.com/evahteri/Path-Finder/blob/main/documentation/specification.md)

## User guide

### Installation

Download this project on your computer and run these commands

#### Install dependencies

```bash
poetry install
```
#### Launching the program

```bash
poetry run invoke start
```
#### Running tests

```bash
poetry run invoke test
```

#### Coverage report

```bash
poetry run invoke coverage-report
```
This command creates a htmlcov folder, where you can find index.html, which includes a visual coverage report

#### Checking style

With this command you can check if code is up to the standard python style of code

```bash
poetry run invoke lint
```


