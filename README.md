# Data Structures Lab project fall 2022

Path Finder is a algorithm project made for data structures lab course in the University of Helsinki. The project is made with python.

## Weekly reports
- [Week 1](https://github.com/evahteri/Path-Finder/blob/main/documentation/weekly_reports/week1.md)
- [Week 2](https://github.com/evahteri/Path-Finder/blob/main/documentation/weekly_reports/week2.md)
- [Week 3](https://github.com/evahteri/Path-Finder/blob/main/documentation/weekly_reports/week3.md)
- [Week 4](https://github.com/evahteri/Path-Finder/blob/main/documentation/weekly_reports/week4.md)
- [Week 5](https://github.com/evahteri/Path-Finder/blob/main/documentation/weekly_reports/week5.md)

## Documentation
- [Timesheet](https://github.com/evahteri/Path-Finder/blob/main/documentation/timesheet.md)
- [Project specification](https://github.com/evahteri/Path-Finder/blob/main/documentation/specification.md)
- [Test coverage](https://github.com/evahteri/Path-Finder/blob/main/documentation/coverage_report.png)
- [Test specification](https://github.com/evahteri/Path-Finder/blob/main/documentation/test_specification.md)
- [Implementation document](https://github.com/evahteri/Path-Finder/blob/main/documentation/implementation.md)


## User guide

### Installation

Download this project on your computer and run these commands. Note! If you download the app as a ZIP -file, make sure that, after extraction, you name the parent folder "Path_Finder". Unless it is not named that, the app will not find the map files.

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


