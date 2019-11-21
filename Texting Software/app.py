import os
from flask import Flask, render_template, jsonify, request, session, Response, make_response
from flask_socketio import SocketIO, emit
from threading import Lock
##from gevent import monkey
##monkey.patch_all()
async_mode = None
from collections import OrderedDict
app = Flask(__name__)
app.config["SECRET_KEY"] = "something super secret"
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

newListOfTextsInChats = {}
listOfChats = []





@app.route("/")
def index():
	return render_template('index.html',async_mode=socketio.async_mode)

@app.route("/channels", methods=["POST"])
def channels():
	name = request.form.get("name")
	
	return render_template("createChatRoom.html", name=name, joinChatName="Skyrim Chat", listOfChats=listOfChats)
	
@app.route("/createChat/<name>", methods=["POST"])
def createChat(name):
	chatName = request.form.get("chatName")
	listOfChats.append(chatName)
	
	list = []
	
	newListOfTextsInChats.update({chatName: list})
	print(newListOfTextsInChats)
	
	return render_template("chatRoom.html", chatName=chatName, name=name, listOfTextsInChats=list)




@app.route("/joinExistingChat/<name>/<chatID>")
def joinExistingChat(name, chatID):
	
	print(name, chatID)
	
	listOfTextsInChats=newListOfTextsInChats.get(chatID)
	
	return render_template('chatRoom.html', name=name, chatName=chatID, listOfTextsInChats=listOfTextsInChats)

@socketio.on('announce', namespace='/test')
def text(message):
	print("we have made it to announce")
	
	theList = newListOfTextsInChats.get(message['chat'])
	theList.append(message['text'])
	
	newListOfTextsInChats[message['chat']] = theList
	
	print(newListOfTextsInChats)
	emit("announce text", {"text": message['text'] }, broadcast=True)



if __name__ == '__main__':
	app.run(debug=True)
	socketio.run(app)

	##index()

	"""
	
	flask run --no-reload 
	
	run with this command"""