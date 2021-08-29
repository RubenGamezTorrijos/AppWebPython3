from flask import Flask, render_template

app = Flask(__name__)

@app.route()
def Inicio(/Inicio):
  return render_template ('Inicio.html')
def Sobre Mi(/SobreMi):
  return 'Sobre mí'

if __name__ ==  '__main__':
  app.run()
