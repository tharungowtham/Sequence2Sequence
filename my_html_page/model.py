import tensorflow as tf
reloaded = tf.saved_model.load('mymodel')
def translate(text, model=reloaded):
  pred = model.translate([text.lower()])[0].numpy().decode()
  print("pred:", pred)
translate("how are you", model=reloaded)
translate("i like sitting in parliament .")
translate("adjournment of the session .")
translate("What is your name ?")
translate("i am grateful for all your speeches .")
translate("madam prime minister , commissioner , I am delighted to see you here again today in america .")