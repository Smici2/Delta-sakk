from flask import Flask
from flask import render_template

app = Flask(__name__)

def beolvas(filenev):
	try:
		with open(filenev, 'r') as f:
			return f.read()
	except:
		return "rnbqkbnrpppppppp********************************PPPPPPPPRNBQKBNR"
	

def atalakito(data):
	adatok = {
		"r" : "images/dr.png",
		"n" : "images/dn.png",
		"b" : "images/db.png",
		"q" : "images/dq.png",
		"k" : "images/dk.png",
		"p" : "images/dp.png",

		"R" : "images/wr.png",
		"N" : "images/wn.png",
		"B" : "images/wb.png",
		"Q" : "images/wq.png",
		"K" : "images/wk.png",
		"P" : "images/wp.png",

		"*" : "images/blank.png"
	}
	lista = []
	for x in data:
		lista.append(adatok[x])

	return lista


@app.route("/")
def main():
    return render_template('main.html')

@app.route("/game")
def game():
	return render_template('game.html')

@app.route("/tabla")
def tabla():
	return render_template('tabla.html', data=atalakito(beolvas("lepesek.txt")))

if __name__ == "__main__":
    app.run(debug=True)