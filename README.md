# alembic-sqlalchemy-notes

- [x] Setting up the environment
- [x] Initializing Alembic
- [x] Alembic config
- [ ] Creating SQLAlchemy Model
- [ ] Creating A Migration with Alembic
- [ ] Writing to the DB using SQLAlchemy Models
- [ ] Reading From the DB using SQLAlchemy Models
- [ ] Enriching SQLAlchemy models with additional propetries and methods
- [ ] Wrapping up

## Initializing Alembic  
- In the project directory, run `alembic init migrations`

### Taking A Look At What `alembic init migrations` Does

When you run the `alembic init migrations` command, it initializes a new Alembic migration environment in your Python project. It sets up the necessary directory structure and configuration files that Alembic uses to manage database migrations. The command creates a directory called "migrations" (if not already present) and populates it with essential files:

- `env.py`: This Python script serves as the migration environment, handling configuration and metadata.

- `script.py`.mako: A Mako template file that is used to generate migration scripts.

- `versions` directory: This directory is where Alembic stores the individual migration scripts. Each migration script represents a specific database schema change and is named with a unique identifier, usually a timestamp followed by a descriptive name.

- `README.md` - Included with this template and should contain something informative. [link](https://alembic.sqlalchemy.org/en/latest/tutorial.html#the-migration-environment)

In the main or top level directory, a file called `alembic.ini` will be created:

- `alembic.ini`: This configuration file contains settings for the Alembic migration environment, including database connection string, target metadata, and other options.

### Configure The Database Connection URL
In the `alembic.ini` file, find the following line: `sqlalchemy.url = driver://user:pass@localhost/dbname`

We need to change the value to `sqlite:///name_of_db.db`

- ***NOTE***: Make sure that you are using `sqlite` here and not `sqlite3`. You will get the following error otherwise:

```shell
raise exc.NoSuchModuleError(
sqlalchemy.exc.NoSuchModuleError: Can't load plugin: sqlalchemy.dialects:sqlite3
)
```


## Resources 

- SQLAlchemy Docs: [Link](https://www.sqlalchemy.org/)
- Alembic Docs: [Link](https://alembic.sqlalchemy.org/en/latest/)
- Setting Up Alembic With SQLAlchemy Video:[Link](https://youtu.be/nt5sSr1A_qw)
