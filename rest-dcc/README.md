# RESTful interface to the DCC DocDB tables in MariaDB

This package implements a simple RESTful API to the DCC DocDB database.

Set up the environment:

```bash
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda3
eval "$(${HOME}/miniconda3/bin/conda shell.bash hook)"

conda create --name dcc conda-forge:mariadb conda-forge::mysqlclient conda-forge::mysql-client=8.4.2
```

Note that version 8.4.2 is needed as later versions drop support for password authentication.

Run the service:

```bash
./RESTServer.py
```

## Generating an Entity Relationship Diagram

### Install the system and conda packages

```bash
sudo apt install graphviz libgraphviz-dev
conda install -c conda-forge eralchemy
```

There is an [incompatibility](https://github.com/eralchemy/eralchemy/issues/80) 
between current versions of eralchemy and the pysql driver, the fix is to edit

```
${CONDA_HOME}/envs/dcc/lib/python3.9/site-packages/eralchemy/sqla.py
```

and replace line 50 with

```python
columns=[column_to_intermediary(col) for col in table.c._colset]
```

### Apply patches to the database

The DCC schema as written does not include any foreign key mapping.  This can partly be fixed 
with code in this repository

```bash
source ~/ce-it-infrastructure/config/dcc-environment.sh
./fix_fks.py  > fixes.sql
mysql -h ${DCC_HOST} --force  -u${DCC_USER} -p${DCC_PASSWORD} dcc < fixes.sql
```

That will catch most of them, for the additional ones

```sql
ALTER TABLE UsersGroup ADD CONSTRAINT FOREIGN KEY (GroupID) REFERENCES AuthorGroupDefinition (AuthorGroupID);
ALTER TABLE AuthorGroupList ADD CONSTRAINT FOREIGN KEY (AuthorGroupID) REFERENCES AuthorGroupDefinition (AuthorGroupID);
```

NOTE: These changes will not be compatible with the DCC in production, there is no guarantee that the code adds
entries to the database in a way that honors the foreign key relationships.  Either make these changes in a scratch
database or delete and rebuild the database after generating the PDF.

### Generate the PDF

```bash
eralchemy -i mariadb://${DCC_USER}:${DCC_PASSWORD}@${DCC_HOST}/dcc -o dcc_erd.pdf
```


