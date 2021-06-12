import flask
from flask import request
import functions

app = flask.Flask("app")


@app.route('/')
def homepage():
  return flask.redirect("/home")

@app.route('/home')
def homestats():
  return flask.render_template('home.html')


@app.route('/checker')
def checker():
  return flask.render_template('checker.html')


@app.route('/checker', methods=['POST'])
def my_form_post_checker():
    text = str(flask.request.form['text'])
    #info = text.upper()
    password = functions.checker_web(text)
    return flask.render_template(f"checker.html", password=password)


@app.route('/generator')
def generator():
  return flask.render_template('generator.html')


@app.route('/generator', methods=['POST'])
def my_form_post_gen1():
  if request.method == "POST":
    if request.form['submit_button'] == 'Simple':
      info = functions.gen_simple_web()
      return flask.render_template(f"generator.html", info=info)
    if request.form['submit_button'] == 'Tough':
      info = functions.gen_tough_web()
      return flask.render_template(f"generator.html", info=info)
    if request.form['submit_button'] == 'Clear':
      return flask.render_template(f"generator.html")
  

  

app.run(debug=True, host="0.0.0.0")