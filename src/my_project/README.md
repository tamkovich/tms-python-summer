# python

- cd src
- cd my_project
- pip install -r requirements.txt
- python app.py

# docker

cd src/
- sudo docker build -t my_flask_app:v0.1 my_project
- sudo docker run -p 5000:5000 my_flask_app:v0.1

# docker-compose

- cd src
- cd my_project
- docker-compose up
