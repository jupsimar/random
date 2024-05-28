from flask import Flask, render_template
import random

app = Flask('app')
#Activate the App inside Flask
#/ is the main page of the website, example AOL
@app.route('/')  
def hello_world():
  people = ['a','b','c']
  person = random.choice(people)
  numbers = f"{random.randint(1,49)} {random.randint(1,49)} {random.randint(1,49)} {random.randint(1,49)} {random.randint(1,49)} {random.randint(1,49)}"
  return render_template("index.html",numbers=numbers,person=person)

app.run(host='0.0.0.0', port=8080)
