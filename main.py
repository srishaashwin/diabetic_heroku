
from flask import Flask ,render_template,request
import joblib
app= Flask(__name__)
#loading the model
model=joblib.load("models\diabetic_80.pkl")

@app.route('/')
def home():
    return render_template("home1.html")
    
@app.route('/data', methods=['post'])
def data():
    preg= request.form.get("preg")
    plas= request.form.get("plas")
    pres= request.form.get("pres")
    test= request.form.get("test")
    skin=request.form.get("skin")
    mass= request.form.get("mass")
    pedi= request.form.get("pedi")
    age= request.form.get("age")

    result =model.predict([[preg,plas,pres,test,skin,mass,pedi,age]])

    if result[0]==1:
        data="Person is Diabetic"
    else:
        data= "Person is Healthy"

    return render_template("test.html", data=data) #just added the html to show the output results

app.run(debug=True) # changes made in home1.html file will update automaticlly
                    #when we  refresh the browser insted of running the terminal
