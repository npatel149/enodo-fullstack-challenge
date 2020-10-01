#!/bin/bash

echo "Hello, world!"
#!/bin/bash -x

GUI_BASE="./enodo-app"
API_BASE="./enodo-api"

# Dependencies
# node 12.17.0
# npm 6.14.4
# Python 3.8.0

node -v
npm -v
python3 --version

echo "GUI_BASE"
pushd "$GUI_BASE"
npm install
popd

echo "API_BASE"
pushd "$API_BASE"
python3 -m venv .venv
. .venv/bin/activate
pip3 install -r requirements_prod.txt
python3 presetup_load_xlsx_data_to_sqlite_db.py
python3 manage.py migrate
popd

echo "Done!"