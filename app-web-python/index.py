from flask import Flask

app = Flask(__name__)

@app.route()
def Inicio(/Inicio):
  return 'Hola Mundo'
def Sobre Mi(/SobreMi):
  return 'Sobre mí'

if __name__ ==  '__main__':
  app.run()
