import streamlit as st
from bb.api import quote

st.title("welcome to our website")


call = quote()
st.write(call)
