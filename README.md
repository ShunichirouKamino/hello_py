# hello_py

## Env

### Assumed

- Windows11
- PowerShell

### Procedure

- Install poetry.

```sh
$ (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
```

- Make a new project.

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
$ poetry run start
PS D:\workspace\python\hello_py> poetry run start
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 10/10 [00:10<00:00,  1.01s/it]
```

## Formatter

- install autopep8

```sh
$ pip install -U autopep8
```

- Check VSCode config
  - Find `python.formatting.provider` in the settings.
  - change to autopep8


if you use black

- $ poetry run black . --check
## TIPS

- clean (Update your lock file)
  - $ poetry lock --no-update
- Run
  - $ poetry run python src/xxx.py
- Test
  - $ poetry run python -rP
