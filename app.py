from flask import Flask, render_template,request #rendering of html page
import pickle
import numpy as np

# request is to get the values entered by the users in the html page
app = Flask(__name__) #gatewat between webserver and py prog
model = pickle.load(open('admission.pkl','rb'))
@app.route('/')
def hello_world1():
    return render_template('index.html')#html file object
#after submitting of values it has to get connected to login beacuse of action method so..

@app.route('/login',methods = ['POST'])
def login():
    ms = request.form["ms"]
    ad =request.form["ad"]
    rd =request.form["rd"]
    sop =request.form["sop"]
    lor =request.form["lor"]
    cgpa =request.form["cgpa"]
    s = request.form["s"]
   
    if(s == "1"):
        s=1
    if(s == "0"):
        s=0
    total = [[int(ms),int(ad),int(rd),float(sop),float(lor),float(cgpa),int(s)]]
    p =  model.predict(total)
    output = np.round(p,3)
    #print(total)
    return render_template('index.html',Something = str(output[0]*100))

#before line, in index.html whereever you find something replace with the value given in the Name box, in the form


if __name__ == '__main__':
    app.run(debug = True)
    #if you want to change things put True, else 
    #you cannot make changes for debug=False, you can click red button and then restart everyt time yiu make chnges
    #you dont get url through True.
    #with True you need to run through prompt anaconda
    #port can be changed app.run(debug=True,port=9000)
    


