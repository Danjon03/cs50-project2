import os
from flask import Flask, render_template, jsonify, request, session
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = "something super secret"
socketio = SocketIO(app)



@app.route("/")
def index():
	return render_template("index.html")

@app.route("/channels", methods=["POST"])
def channels():
	name = request.form.get("name")
	session["user"] = name
	return render_template("createChatRoom.html", name=name, joinChatName="Skyrim Chat")
	
@app.route("/createChat", methods=["POST"])
def createChat():
	chatName = request.form.get("chatName")
	user=session["user"]
	return render_template("chatRoom.html", user=user, chatName=chatName)
	
@app.route("/joinExistingChat", methods=["POST"])
def joinExistingChat():
	
	
	
	user=session["user"]
	return render_template("chatRoom.html", user=user, chatName="Skyrim Chat" )
	
	

	
	
	

if __name__ == '__main__':
	socketio.run(app)
	index()
	
	"""
	
	flask run --no-reload 
	
	run with this command"""