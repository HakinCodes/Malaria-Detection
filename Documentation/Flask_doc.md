# ![](https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSZSpvSw_GYFMCxg8stQY6y4ZUMut4liIVYlg&usqp=CAU)

Flask is a micro web application framework. Flask was created by [Armin Ronacher](https://en.wikipedia.org/wiki/Armin_Ronacher) of Pocoo, 
an international group of Python enthusiasts formed in 2004.

It is designed to make getting started quick and easy, with the ability to scale up to complex applications. 
It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.</br>

Flask depends on two external libraries:
1) [Jinja2 template engine](https://jinja.palletsprojects.com/en/2.11.x/2/documentation/)
2) [Werkzeug WSGI toolkit](https://palletsprojects.com/p/werkzeug/)

Applications that use the Flask framework include **Pinterest** and **LinkedIn**.

## INSTALLATION

* Creating **Virtual Enviroment** (It helps a user to create multiple Python environments side-by-side. 
    Thereby, it can avoid compatibility issues between the different versions of the libraries.) </br>
    If you’re using Python 2, Install Virtual Enviroment first and replace venv with virtualenv in the below commands.. 
    If you’re using a modern version of Python, you can may or may not create Virtual Enviroment.
    
    **On Linux**:
    ```
    sudo apt-get install python3-venv
    python3 -m venv env
    source env/bin/activate
    ```

    **On Windows**:
    ```
    pip install virtualenv
    py -m venv env
    .\env\Scripts\activate
    ```
> venv will create a virtual Python installation in the env folder.

* Installing **FLASK**

    ```
    pip install Flask
    ```

* Deactivating Virtual Enviroment

    ```
    deactivate
    ```

## EXAMPLE
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def detetction():
   return 'Malaria Detection’

if __name__ == '__main__':
   app.run(debug=True)
```
Analyze the code line by line.

* In the first line, we are importing the Flask class.
* Next, we creating an instance of the Flask class.
* Then we use the **route()** decorator to register the **detection** function for the **/** route. When this route is requested, detection is called and the message “Malaria Detection” is returned to the client. 
* Finally the **run()** method of Flask class runs the application on the local development server. If the **Debug mode** is enabled, The server will then reload itself if the code changes. 
> The above given Python script is executed from Python shell
```
python app.py
```
**OUTPUT**
```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
> **127.0.0.1** and **5000** are the default _host and route_. </br>
Open http://127.0.0.1:5000/ or [localhost:5000](http://127.0.0.1:5000/) and **Malaria Detection** would be seen on screen.

