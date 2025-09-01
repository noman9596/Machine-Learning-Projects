import streamlit as st
import pandas as pd
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import string
import nltk
import pickle
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re
nltk.download('stopwords')

def preprocessing(text):
   import re

def preprocessing(text):
    text=text.lower()
    text=text.split()
    
    y=[]
    for i in text:
        if i.isalpha():
            y.append(i)
    z=y[:]
    y.clear()
    
    for i in z:
        if i not in stopwords.words("english") and i not in string.punctuation:
            y.append(i)
    
    z=y[:]
    y.clear()
    for i in z:
        y.append(ps.stem(i))
    return " ".join(y)
       


# st.title("Email Checker")
model=pickle.load(open("model.pkl","rb"))
cv=pickle.load(open("vetorizer.pkl","rb"))
ps=PorterStemmer()

wc=WordCloud(width=300,height=300,min_font_size=3,background_color="white")
mail=st.text_input("Enter mail")
if mail:
   if st.button("Check") :
      text=preprocessing(mail)
      embeddings=cv.transform([text])[0]

      x=model.predict(embeddings)
      if x==1:
         st.success("📩 This is SPAM")
         st.write("Why spam")
         wordcloud_img = wc.generate(text)
         plt.figure(figsize=(3,3))
         plt.imshow(wordcloud_img, interpolation='bilinear')
         plt.axis('off')
         st.pyplot(plt)
         plt.clf()
      else:
         st.success("✅ This is NOT SPAM")
      
