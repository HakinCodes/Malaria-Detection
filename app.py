from flask import Flask, render_template,url_for,request, redirect
import numpy as np
import tensorflow as tf
from keras.models import load_model
import re
from keras.preprocessing import image
from skimage import transform

app = Flask(__name__)
model = load_model('CNN.h5')
graph = tf.get_default_graph()

def ValuePredictor(np_arr):   
    global graph
    with graph.as_default():
        result = loaded_model.predict(np_arr)
    return result[0]

def image_preprocess(img):
  new_shape = (50, 50, 3)
  img = image.load_img(img)
  image_array = image.img_to_array(img)
  image_array = transform.resize(image_array, new_shape, anti_aliasing = True)
  image_array /= 255
  image_array = np.expand_dims(image_array, axis = 0)
  return image_array


@app.route("/")
def landingPage():
    return render_template("index.html")


@app.route("/form")
def inputForm():
    return render_template('form.html')


@app.route("/result", methods = ['GET', 'POST'])
def result():
    if request.method == 'POST':
        image = request.form['image']
        img_array = image_preprocess(image)
        result = int(np.argmax(ValuePredictor(img_array)))
        if result == 1:
            pred = "This cell is likely to be Uninfected and free from Malarial Parasite"
        else:
            pred = "This cell is likely to be infected with Malarial Parsite"
        print(pred)
        return render_template('result.html', image=image)
    

@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    try:
        app.run(debug=True)
    except:
        print("Error")
