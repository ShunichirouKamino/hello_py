# hello_py

## Env

### Assumed

- Windows11
- PowerShell
  - install poetry
- Git Bash
  - anything

### Procedure

- PowerShell

```powershell
$ (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
```

- Git Bash

```sh
$ poetry new <PROJECT-NAME>
```

## Virtualization

- Change the poetry config.

```sh
$ poetry config virtualenvs.in-project true
$ poetry config virtualenvs.path .
$ poetry config --list | grep virtualenvs
virtualenvs.create = true
virtualenvs.in-project = true
virtualenvs.path = "."
```

- Make the virtual environment.

```sh
$ poetry install
```

## Hello World

```sh
$ poetry run hello_py/main.py
```
