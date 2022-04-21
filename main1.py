import pip



from flask import Flask ,render_template,request

app= Flask(__name__)

@app.route('/')
def home():
    return render_template("home1.html")
    
# #@app.route('/data')
# def data():
#     first_name= request.form.get("first_name")
#     second_name= request.form.get("second_name")
#     number= request.form.get("number")
#     email= request.form.get("email")

#     print(first_name ,second_name ,number ,email)
#     return 'Data received'

@app.route('/data', methods=['post'])
def data():
    first_name= request.form.get("first_name")
    second_name= request.form.get("second_name")
    number= request.form.get("number")
    email= request.form.get("email")

    print(first_name ,second_name ,number ,email)
    return 'Data received'


app.run(debug=True) # changes made in home1.html file will update automaticlly
                    #when we  refresh the browser insted of running the terminal

