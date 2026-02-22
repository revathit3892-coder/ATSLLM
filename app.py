import streamlit as st
import pandas as pd
import numpy as np

#Title of the application:
st.title("Hello Streamlit")

#Display a simple text:
st.write("This sis simple text")

# Create a simple dataframe:
df = pd.DataFrame({
    'first_column' : [1,2,3,4],
    'second_column': [23,34,45,56]
})

#Display the DataFrame:
st.write("Here is the Dataframe")
st.write(df)

# Create. aline chart:
chart_data = pd.DataFrame(np.random.randn(20,3), columns = ['a','b','c'])
st.line_chart(chart_data)