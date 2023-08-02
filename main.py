from flask import *
from flask_cors import CORS
import requests
app=Flask(__name__)
cors = CORS(app, resources={"*": {"origins": "*"}})

@app.route('/')
def home():
    return render_template("home.html")


@app.route("/getData",methods=["GET","POST"])
def getData():
    try:
        formData=request.get_json().copy()
        result=requests.get("https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22")
        data=result.json()["list"]
        if(len(data)>0):
            for i in data:
                print(i["dt_txt"].split(" "),str(formData["date"]))    
                if(i["dt_txt"].split(" ")[0]==formData["date"]):
                    print(i,formData)
                    if(int(formData["option"])==1):
                        return {"msg":i["weather"]}
                    elif(int(formData["option"])==2):
                        return {"msg":i["wind"]["speed"]}
                    elif(int(formData["option"])==3):
                        return {"msg":i["main"]["pressure"]}
                    else:
                        return {"msg":"an error occurred with data"}
            return {"msg":"no data"}
        else:
            return {"msg":"no data"}
                
        
    except Exception:
        return {"msg":"error occurred"}

if __name__=="__main__":
        app.run(debug=True,port=3000)