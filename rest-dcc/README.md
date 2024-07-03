# RESTful interface to the DCC DocDB tables in MariaDB

This package implements a simple RESTful API to the DCC DocDB database using 
[FastAPI](https://fastapi.tiangolo.com/) and [SQLAlchemy](https://www.sqlalchemy.org/)


Set up the environment:

```
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda3
eval "$(${HOME}/miniconda3/bin/conda shell.bash hook)"

conda create --name dcc
conda activate dcc
conda install conda-forge::sqlalchemy conda-forge::sqlacodegen conda-forge::fastapi conda-forge:mariadb conda-forge::mysqlclient conda-forge::uvicorn
```

To regenerate `tables.py` if needed (for example if the schema changes)

```
# Adding +mariadbconnector would force communication over SSL, the MariaDB container would need
# to be modified to support this.
# sqlacodegen mariadb+mariadbconnector://root:abcde@127.0.0.1:3306/dcc

# Parameters in the URL should come from the dcc-environment.sh.  Hardcoded here for development.
sqlacodegen mariadb://root:abcde@127.0.0.1:3306/dcc > tables.py
```

Then to run the service

```
uvicorn main:app --reload
```

