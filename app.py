from flask import Flask, request, redirect, url_for, render_template
import pickle
import numpy as np


app = Flask(__name__)

model = pickle.load(open('decision_tree.pkl','rb'))
cv = pickle.load(open('cv.pkl','rb'))
def get_prediction(text , model , cv):
    ##text in list
    text = cv.transform(text)
    pred = model.predict(text)
    if pred[0] == 1:
        return 'Offensive'
    else:
        return 'Not Offensive'

##default home page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    #For rendering results on HTML GUI
    text =[str(x) for x in request.form.values()]
    output = get_prediction(text, model, cv)
    return render_template('index.html', prediction_text='This tweet was {}'.format(output))
if __name__ == "__main__":
    app.run(host = '0.0.0.0' , debug = True)
