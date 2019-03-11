from flask import Flask,jsonify,request
import json, os.path,datetime

app=Flask(__name__)x

#for greeting first step
@app.route("/api/chat_bot/<Email_Id>",methods=['POST'])

def post_data(Email_Id):
	now=datetime.datetime.now()
	localtime=(now.strftime("%x"))
	if os.path.isfile("feeling_share.json"):
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