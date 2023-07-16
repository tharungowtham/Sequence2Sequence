from flask import Flask
import tensorflow as tf
reloaded = tf.saved_model.load('my_html_page\mymodel')
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"
    
@app.route('/<english>')
def translate(english, model=reloaded):
  pred = model.translate([english.lower()])[0].numpy().decode()
  return {"english":english,"predict":pred}

if __name__ == '__main__':
    app.run()