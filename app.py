from flask import Flask,render_template,request

import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

app=Flask(__name__,static_url_path='/static')
model = pickle.load(open('Model.pkl','rb'))

@app.route('/',methods=['GET'])
def home():
    return render_template("index.html")
@app.route('/education',methods=['GET','POST'])
def education():
    return render_template("loading1.html")
@app.route('/food',methods=['GET','POST'])
def food():
    return render_template('loader2.html')
@app.route('/food2',methods=['GET','POST'])
def food2():
    return render_template('location.html')
@app.route('/business',methods=['GET','POST'])
def business():
    return render_template("loading.html")
@app.route('/vijayawada',methods=['GET','POST'])
def vijayawada():
    return render_template("vijayawada.html")
@app.route('/vishakapatnam',methods=['GET','POST'])
def vishapatnam():
    return render_template("vishakapatnam.html")
@app.route('/guntur',methods=['GET','POST'])
def guntur():
    return render_template("guntur.html")
@app.route('/loader')
def loader():
    return render_template('loader2.html')
standard_to = StandardScaler()
@app.route('/predict',methods=['POST'])
def predict():
    if request.method=="POST":
        Location=int(request.form['Location'])
        bsize=int(request.form['bsize'])
        amb=float(request.form['amb'])
        menu=float(request.form['menu'])
        Chef=float(request.form['chef'])
        ksize=float(request.form['ksize'])
        Marketing=float(request.form['mark'])
        Staff_Level=float(request.form['sl'])
        Security=int(request.form['sec'])
        Government_Permission=int(request.form['gp'])
        print(Location)
        print(bsize)
        print(amb)
        print(menu)
        print(Chef)
        print(ksize)
        print(Marketing)
        print(Staff_Level)
        print(Security)
        print(Government_Permission)
        # l=sum([Location,bsize,amb,menu,Chef,ksize,Marketing,Staff_Level])
        # output=round(l,2)
        output=model.predict([[Location,bsize,amb,menu,Chef,ksize,Marketing,Staff_Level]])
        output=round(output[0],2)
        if output<0:
            return render_template("endpage,html",prediction_text="sorry")
        else:
            return render_template("endpage.html",prediction_text="{}".format(output),Location=Location,out={0:["Ambience- Chavera Furniture & Interiors- 8632231188","Menu- Kolli sarada vegetables- 9440488633","Chef- jhonson- 9290410345","Marketing- Mangsen- 9044910449"],
      1:["Ambience- Royal Home Furniture- 9292459459","Menu- Maram Home Foods- 9885276319","Chef- Rakesh- 7382012081","Marketing- SearchBell- 9666112394"],
      2:["Ambience- Sky limits Greens - 9121162399","Menu- Sri lalitha Greens- 9393993839","Chef- Govind- 8019828828","Marketing- 10gminds- 9494586583"]})

if __name__=='__main__':
    app.run(debug=True)