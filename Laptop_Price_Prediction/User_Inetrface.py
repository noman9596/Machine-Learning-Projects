import streamlit as st
import pandas as pd
import pickle
import numpy as np

df=pd.read_csv(r"C:\Users\arman\ML_14_Days\laptop.csv")
with open ("model_lap","rb") as f:
    model=pickle.load(f)

st.title("Welcome to OpenAI Laptop Shop")
company=df["Company"].unique()
com=st.selectbox("Choose Compnay",company)

type_name=df["TypeName"].unique()
type_=st.selectbox("Choose Type",type_name)


inches=st.slider("Choose a Value",10.0,18.0,10.0)

cpu_=df["Cpu"].unique()
cpu=st.selectbox("Choose CPU",cpu_)


ram_=df["Ram"].unique()
ram=st.selectbox("Choose Ram",ram_)

gpu_=df["Gpu"].unique()
gpu=st.selectbox("Choose GPU",gpu_)

os_=df["OpSys"].unique()
os=st.selectbox("Choose Ram",os_)

weight=st.slider("Choose a Value",0.69,4.7,0.69)

screen_=df["Screen"].unique()
screen=st.selectbox("Choose Screen",screen_)

mt_=df["Memory_Type"].unique()
mt=st.selectbox("Choose Screen",mt_)

input_df = pd.DataFrame({
    "Company": [com],
    "TypeName": [type_],
    "Cpu": [cpu],
    "Gpu": [gpu],
    "OpSys": [os],
    "Screen": [screen],
    "Memory_Type": [mt],
    "Inches": [inches],
    "Ram": [ram],
    "Weight": [weight]

})

if st.button("Predict Price"):
  try:
    price=model.predict(input_df)[0]
    price_=np.exp(price)
    st.success(f"Estimated Price: Rs{int(price_)}")

  except Exception as e:
    st.error(f"Prediction failed: {e}")











