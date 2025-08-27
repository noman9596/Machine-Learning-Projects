from flask import Flask,render_template,request
import pandas as pd
import numpy as np
import pickle
app=Flask(__name__)
df=pd.read_csv(r"D:\Projects\Linear_Regression\static\clean_car_price.csv")
with open("linear_model","rb") as f:
     load_model=pickle.load(f)
@app.route("/")
def index():
    company=sorted(df["company"].unique())
    model=sorted(df["short_name"].unique())
    fuel=sorted(df["fuel_type"].unique())
    year=sorted(df["year"].unique())
    return render_template("index.html",company=company,model=model,fuel=fuel
                          ,year=year)

@app.route("/predict",methods=["POST"])
def predict():
    com=request.form.get("company")   
    model=request.form.get("model")
    fuel=request.form.get("fuel")
    year=int(request.form.get("year"))
    km=int(request.form.get("kms"))

    input_user_df=pd.DataFrame([[com,model,fuel,year,km]],columns=["company",
                                                                   "short_name","fuel_type","year","kms_driven"])                                                               
    model=load_model.predict(input_user_df)
    print(model[0])
    return render_template("result.html",model=model[0].reshape(1,).round(2).astype(int)) 

if __name__=='__main__':
    app.run(debug=True)

