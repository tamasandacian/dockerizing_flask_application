# dockerizing_flask_application

A simple tutorial of how to create docker image for a Python Flask application.

The following are the basic steps:
```

1. create new folder
   mkdir "folder_name"
   
2. create Flask application (root folder)
   app.py
   
3. add the following code (app.py)
   from flask import Flask
   from flask import jsonify
   
   app = Flask(__name__)

   @app.route('/')
   def hello_world():
      """
      Method returning json message.
      """
      message = { "message": "Hello World!"}
      return jsonify(message)

   if __name__ == "__main__":
      app.run(debug=True, host='0.0.0.0')

3. create requirements.txt file (root folder)

4. inside requirements.txt file add python library name(s)
   flask

5. create Dockerfile without suffix (root folder) 

6. add the following code
   FROM python:3.6
   COPY . /app
   WORKDIR /app
   RUN pip install -r requirements.txt
   ENTRYPOINT ["python"]
   CMD ["app.py"]

8. to build docker image run command:
   docker build -t "folder_name":latest .

9. to run docker image run command:
   docker run -d -p 5000:5000 "folder_name"
   
10. open browser and access http://127.0.0.1:5000/
```
