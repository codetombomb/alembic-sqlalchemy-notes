# alembic-sqlalchemy-notes

- [ ] Setting up the environment
- [ ] Initializing Alembic
- [ ] Alembic config
- [ ] Creating SQLAlchemy Model
- [ ] Creating A Migration with Alembic
- [ ] Writing to the DB using SQLAlchemy Models
- [ ] Reading From the DB using SQLAlchemy Models
- [ ] Enriching SQLAlchemy models with additional propetries and methods
- [ ] Wrapping up

## About SQLAlchemy
- SQLAlchemy is an ORM.
- It is a library that offers an object interface to the data in the database.
- It abstracts away the need to directly write SQL code to perform transactions with the database

## About Alembic
- It is part of the SQLAlchemy project 
- It allows you to replicate in the DB the schemas of the data that you have defined in your code using the SQLAlchemy models.
- It handles creating the tables, columns, and assigning data types and because of this, there is less room for error when creating and configuring db tables.

## Pipenv information
We are going to use [pipenv](https://pypi.org/project/pipenv/) to manage the dependencies.

- You can get a list of helpful hints on getting started just by running the command `pipenv` in the terminal. Here is what the output looks like:

```shell
Usage: pipenv [OPTIONS] COMMAND [ARGS]...

Options:
  --where                         Output project home information.
  --venv                          Output virtualenv information.
  --py                            Output Python interpreter information.
  --envs                          Output Environment Variable options.
  --rm                            Remove the virtualenv.
  --bare                          Minimal output.
  --man                           Display manpage.
  --support                       Output diagnostic information for use in
                                  GitHub issues.
  --site-packages / --no-site-packages
                                  Enable site-packages for the virtualenv.
                                  [env var: PIPENV_SITE_PACKAGES]
  --python TEXT                   Specify which version of Python virtualenv
                                  should use.
  --three                         Use Python 3 when creating virtualenv.
                                  Deprecated
  --clear                         Clears caches (pipenv, pip).  [env var:
                                  PIPENV_CLEAR]
  -q, --quiet                     Quiet mode.
  -v, --verbose                   Verbose mode.
  --pypi-mirror TEXT              Specify a PyPI mirror.
  --version                       Show the version and exit.
  -h, --help                      Show this message and exit.


Usage Examples:
   Create a new project using Python 3.7, specifically:
   $ pipenv --python 3.7

   Remove project virtualenv (inferred from current directory):
   $ pipenv --rm

   Install all dependencies for a project (including dev):
   $ pipenv install --dev

   Create a lockfile containing pre-releases:
   $ pipenv lock --pre

   Show a graph of your installed dependencies:
   $ pipenv graph

   Check your installed dependencies for security vulnerabilities:
   $ pipenv check

   Install a local setup.py into your virtual environment/Pipfile:
   $ pipenv install -e .

   Use a lower-level pip command:
   $ pipenv run pip freeze

Commands:
  check         Checks for PyUp Safety security vulnerabilities and against
                PEP 508 markers provided in Pipfile.
  clean         Uninstalls all packages not specified in Pipfile.lock.
  graph         Displays currently-installed dependency graph information.
  install       Installs provided packages and adds them to Pipfile, or (if
                no packages are given), installs all packages from Pipfile.
  lock          Generates Pipfile.lock.
  open          View a given module in your editor.
  requirements  Generate a requirements.txt from Pipfile.lock.
  run           Spawns a command installed into the virtualenv.
  scripts       Lists scripts in current environment config.
  shell         Spawns a shell within the virtualenv.
  sync          Installs all packages specified in Pipfile.lock.
  uninstall     Uninstalls a provided package and removes it from Pipfile.
  update        Runs lock, then sync.
  verify        Verify the hash in Pipfile.lock is up-to-date.
```
## Creating the Virtual Env
- Create a the virtual environment (using Python 3.8) by running:
    - `pipenv --python 3.8`

### Starting the Virtual Env
- Run `pipenv shell`

### Stopping the Virtual env
- Run `exit`

### Install Alembic and SQLAlchemy
- Run `pipenv install alembic sqlalchemy`



## Resources 

- SQLAlchemy Docs: [Link](https://www.sqlalchemy.org/)
- Alembic Docs: [Link](https://alembic.sqlalchemy.org/en/latest/)
- Setting Up Alembic With SQLAlchemy Video:[Link](https://youtu.be/nt5sSr1A_qw)
