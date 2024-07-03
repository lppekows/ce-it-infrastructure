# DCC

An updated version of the DCC based on the latest LIGO release

```
git clone git@github.com:cosmic-explorer/ligo-dcc.git
pushd ligo-dcc
# This has some patches that have not yet been accepted into the main repo
git checkout installation-fixes
source dcc-environment.sh
docker compose up
```
