from flask import Flask
from flask import request
from keras.models import load_model
from flask import render_template

model = load_model('/ws/diabetes_dl_model.h5')
app = Flask("myapp")
@app.route("/output",methods=["GET"])
def home():
    glu=int(request.args.get("glucose"))
    pregnancy=int(request.args.get("pregnancy"))
    press=int(request.args.get("pressure"))
    skin=int(request.args.get("skin"))
    ins=int(request.args.get("insulin"))
    bmi=float(request.args.get("bmi"))
    dfunc=float(request.args.get("dfunc"))
    age=int(request.args.get("age"))
    output = model.predict([[pregnancy,glu,press,skin,ins,bmi,dfunc,age]])
    return(str(round(output[0][0])))


@app.route("/form")
def myform():
    return(render_template('myform.html'))

app.run(host="0.0.0.0",port=8080)

