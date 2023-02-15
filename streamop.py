import streamlit as st
import pandas as pd
import ml


st.write("""
# THIS IS THE MINI-PROJECT FOR IH
This will help the user to optimize their sales by our suggestions of gender audience and rating

Please enter the required fields!!
""")
member_check= st.radio("Are you a member of Innovation Hub",("Yes","No"))
st.write("\n\n\n")

branch = st.radio("Select the branch you want to sell your product at--",('A','B', 'C'))

city = st.radio("Select the city you want to sell your product in--",('Yangon', 'Naypyitaw', 'Mandalay'))

customer_type = st.radio("Select the customer type you want to sell your product to--",('Member','Normal'))

product_line = st.radio("Select the product line of your product--",('Health and beauty', 'Electronic accessories','Home and lifestyle', 'Sports and travel', 'Food and beverages','Fashion accessories'))

unit_price = st.slider("Select the unit price of your product", 0, 100)


arr=[branch,city,customer_type,product_line,unit_price,member_check]
rating_ans, gender_ans = ml.get_data(arr)

if gender_ans==0:
    gender_ans_converted="Male"
else:
    gender_ans_converted="Female"

st.write("---")
st.write("""
# Your Results are Here!!

Our application predicts that your product will have an average market rating of-- 
""",round(rating_ans[0],4))

st.write("Your product will be more popular amongst the ",gender_ans_converted," audience")