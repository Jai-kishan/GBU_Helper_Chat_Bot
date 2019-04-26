#Flask is a Python web framework.Flask can be used for building complex , database-driven websites,starting with mostly static pages.
#Requests is a python module that you can use to send all kinds of HTTP requests
#The jsonify() function in flask returns a flask.Response()
from flask import Flask,jsonify,request
#The jsonify() function in flask returns a flask.Response()
import json, os.path,datetime
#The JSON module is mainly used to convert the python dictionary above into a JSON string that can be written into a file.
#The OS module in python provides functions for interacting with the operating system.
app=Flask(__name__)

#for greeting first step
@app.route("/api/chat_bot/<Email_Id>",methods=['POST'])

def post_data(Email_Id):
	now=datetime.datetime.now()
	localtime=(now.strftime("%x"))
	if os.path.isfile("feeling_share.json"):
		#The best way to do this is using the withstatement its work for file handling.
		#This ensures that the file is closed when the block inside with is exited.
		with open("feeling_share.json") as file:
			read_file=file.read()
			file_store=json.loads(read_file)
		newfeeling={
		"Name":request.json["Name"],
		"Feeling":request.json["Feeling"]
		# "Feeling_express":request.json["Feeling_express"]
		}

		if Email_Id not in file_store:
			file_store[Email_Id]={}

		if localtime in file_store[Email_Id]:
			file_store[Email_Id][localtime].append(newfeeling)
		else:
			file_store[Email_Id][localtime] =[]

		file_store[Email_Id][localtime].append(newfeeling)
		with open("feeling_share.json","w") as file:
			json.dump(file_store,file,indent=4, sort_key=True)
		return jsonify(newfeeling)
	return jsonify({"Errors":"No file"})

#make a new routes
@app.route("/api/chat_bot/<Email_Id>",methods=['GET'])
def get_data(Email_Id):
	with open("feeling_share.json") as file:
		read=file.read()
		jsonData=json.loads(read)
	a=jsonData[Email_Id].keys()
	list1=[]
	for i in a:
		list1.append(i)
	data=[]
	for date in list1:
		for i in jsonData[Email_Id][date]:
			data.append(i["Feeling"])
	return jsonify(data) 


if __name__ =="__main__":
	app.run(debug=True, port=8000)
