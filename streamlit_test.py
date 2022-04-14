import streamlit as st
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


st.title('Counter Example')
if 'count' not in st.session_state:
    st.session_state.count = 0

increment = st.button('Increment')
if increment:
    st.session_state.count += 1

st.write('Count = ', st.session_state.count)

st.title('Dataset Visual (with penguin_size.csv')
df = pd.read_csv('penguins_size.csv')
st.dataframe(df)


fig, ax = plt.subplots()
ax.hist(df['flipper_length_mm'], bins=20)

st.pyplot(fig)

st.caption('Histogram for flipper_length_mm')

st.title('Persistent Comments')
f = open("comments.txt", "a")
input = st.text_input('Enter comment here')
f.write(input)
f.write('\n')
f.close()

f_again = open("comments.txt", "r")
acc_comments = f_again.read()
st.text(acc_comments)
f_again.close()




