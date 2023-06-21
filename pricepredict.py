import streamlit as st
import pickle
from sklearn.preprocessing import QuantileTransformer

rf_regressor,X_train = pickle.load(open('PROFITMODEL.pkl','rb'))
#,x_train
#Streamlit is a light weight web app making framework.
st.title ("Price Prediction")
with st.form("my_form"):
    bmi = st.text_input('R&D Spend')
    bp = st.text_input('Administration')
    glu =st.text_input('Marketing Spend')
  
    submitted = st.form_submit_button("Submit")

#Model Only takes scaled values. So we have to scale those values before giving input into our model.
if submitted:
    # scaler = QuantileTransformer(n_quantiles=100, random_state=0, output_distribution='normal')
    # values = scaler.fit_transform(rf_regressor,X_train)
    glu,bp,bmi = int(glu),int(bp),int(bmi)
    # values = scaler.transform([[glu,bp,bmi]])
    values = [[bmi,bp,glu]]
    pred = rf_regressor.predict(values)
    st.success(f'Price {pred[0]}')

        
