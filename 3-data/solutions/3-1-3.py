import streamlit as st
import pandas as pd
import numpy as np

st.title('Customers')
customers = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/master/customers/customers.csv')
st.dataframe(customers)


