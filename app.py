import streamlit as st 
import pickle 
import pandas as pd
# To load model back
with open('SVCpred.pickle','rb') as file:
    loaded_model = pickle.load(file)

st.title("Text Classification")
 
st.write("Enter news here")
 
news = st.text_area("Enter news")
 
if st.button("Submit"):
    df = pd.DataFrame({'news':[news]})
    result = loaded_model.predict(df['news'])
    st.success("The news has submitted")
    st.write(result)

