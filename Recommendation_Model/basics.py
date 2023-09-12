#Importing requried librares
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from flask import Flask,render_template,request,redirect,url_for
import pickle
from hi import cus_dit,loc_dit
from hi import df
from hi import location_list

#Loading the Model
model=pickle.load(open('price_model.pkl','rb'))
app=Flask(__name__)
@app.route('/', methods=['GET','POST'])
# def index():
#     if request.method=='POST':
#         return web()
#     location=location_list
#     return render_template('web.html',location_list=location,predict='',predict_1='',predict_2='',predict_3='',predict_4='')
def main():
    if request.method=='POST':
        return web()
    #Returing the values in required fields
    return render_template('web.html',predict="",predict_1="",predict_2="",predict_3="",predict_4="")
@app.route('/predict', methods=['POST','GET'])
def web():
    if request.method=='POST':
        data1=request.form['cusine']
        data2=float(request.form['price'])
        data3=request.form['loc']
        data1_encode=cus_dit.get(data1,-1)
        data3_encode=loc_dit.get(data3,-1)
        arr=np.array([[data1_encode,data3_encode]])
        predict=model.predict(arr)
        pop_cousine=df[df['location']==data3]['Cousines'].value_counts().idxmax()
        pop_loc=df[(df['Cousines']==data1) & (df['Price']<=data2)]['location'].value_counts().idxmax()
        pop_dish=df[df['Price']<=data2]['dish_name'].value_counts().idxmax()
        pop_res=df[df['Cousines']==data1]['Restaurant_Name'].value_counts().idxmax()
        return render_template('web.html',predict=predict[0],predict_1=pop_cousine,predict_2=pop_loc,predict_3=pop_dish,predict_4=pop_res)
    return redirect(url_for('main'))
            

if __name__=='__main__':
    app.run(debug=True)

    
