# Dokimi is a demo site for Flask and Vue.js

### the frontend is Vue.js and the backend is a simple Python Flask API

## install and run for dev

## frontend

1. clone repo
   `git clone https://github.com/jwpowers2/Dokimi`
2. cd into the frontend directory of Dokimi
   `cd Dokimi/frontend`
3. install npm dependencies
   `npm i`
4. run Vue.js dev server
   `npm run serve`

## backend

1. cd into root of project
   `cd ..`
2. make backend a virtualenv
   `virtualenv backend`
3. activate virtualenv
   `source backend/bin/activate`
4. use pip to install dependencies
   `pip install -r requirements.txt`
5. env variable for flask app
   `export FLASK_APP=api_server.py`
6. run flask development server
   `flask run`
