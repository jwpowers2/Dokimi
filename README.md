#Dokimi is a site I've built for a job interview

### the frontend is Vue.js and the backend is a simple Python Flask API

# install and run for dev

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

1. cd into backend from frontend
   `cd ../backend`
2. use pip to install dependencies
   `pip install -r requirements.txt`
3. env variable for flask app
   `export FLASK_APP=api_server.py`
4. run flask development server
   `flask run`
