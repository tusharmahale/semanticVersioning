# Micro-service Semantic Versioning Script
This is a Python script that helps in versioning micro-service releases based on the commit message. The script takes in the current version of the micro-service and the commit message as input, and based on the commit message, it bumps the version to the next appropriate version according to the predefined guidelines.

## Getting Started
### Prerequisites
Python 3.x
### Usage
To use the script, simply call the bump_version() function and pass in the current version and the commit message as arguments:

```shell
python bump_version.py '<current_version>' '<change-type>: <change message>'
python bump_version.py '1.2.3' 'ci: this is test'
```
OR you can call python function as below
```python
bump_version('3.2.0', 'feat: New shiny feature')
```

new_version: Function will return new version

### Guidelines for Version Bumping
The following table shows the version bump based on the commit message's change type:

| Change Type | Section | Example Version Bump | From | To |
| ------ | ------ | ------ | ------ | ------ |
| ci | PATCH | 1.0.0 → 1.0.1 | x.y.z | x.y.(z+1) |
| chore | PATCH | 1.0.1 → 1.0.2 | x.y.z | x.y.(z+1) |
| feat | MINOR | 1.0.2 → 1.1.0 | x.y.z | x.(y+1).0 |
| feature | MINOR | 1.0.2 → 1.1.0 | x.y.z | x.(y+1).0 |
| breaking | MAJOR | 1.1.0 → 2.0.0 | x.y.z | (x+1).0.0 |
| major | MAJOR | 2.2.1 → 3.0.0 | x.y.z | (x+1).0.0 |

Any change type that is not part of the above table results in an increase in the PATCH version.

### Running the tests
The script comes with a set of unit tests. To run the tests, simply execute the following command:

```shell
python Test.py
```
This will run the test suite and print out the results.