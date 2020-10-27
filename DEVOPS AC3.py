Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Como criar uma imagem no Docker
1)	Cria um repositório no GitHub
2)	No labs.play-with-docker.com : git clone <repositório>
3)	Cria 2 arquivos: Dockerfile e app.py (através do vim em python)
Exemplos:
Dockerfile	app.py

FROM python:3.6.1-alpine
RUN pip install flask
COPY app.py /app.py
CMD ["python", "app.py"]	import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(_name_)

@app.route('/')
def fibonacci():
  prox = 1
  ant = 0
  lim = 50
  cont = 0
  resp = "0, "
 while (cont < lim):
    temp = prox
    prox = prox + ant
    ant = temp
    cont = cont + 1
    resp += str(prox) + ", "


  return resp

if _name_ == "_main_":
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)

4)	Roda os comandos:
•	docker image build -t <nome de um arquivo>
•	doker run -p 5001:5000 -d <nome de um arquivo>
5)	Roda a porta 5001 e “printa” a tela
6)	Envia para o GitHub: git add .    /     git commit -m “   “     /     git push