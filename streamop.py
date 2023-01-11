import streamlit as st
import pandas as pd

st.write("""
# THIS IS THE MINI-PROJECT FOR IH
This will help the user to optimize their sales by our suggestions of selling price and rating

Please enter the required fields!!
""")
product = st.radio("Select the branch you want to sell your product--",('A','B', 'C'))
st.write(product)