import  streamlit as st
import pickle
import pandas as pd

with open("house_price_app.pkl", "rb") as file:
    model = pickle.load(file)

    # 

    st.title("House Price Prediction App")
    area =st.number_input("Enter the area of the house (in square feet):", min_value=100, max_value=10000, value=1000)


    if st.button("Predict House Price"):

        #create DataFrame 

        new_house=pd.DataFrame([[area]], columns=["area"])
        prediction = model.predict(new_house    )
       

    predicted_price=model.predict(new_house)

    st.success(f"The predicted house price is: ${predicted_price[0]:,.2f}")

    st.markdown("---")
    st.write("Machine learning model used: Linear Regression")