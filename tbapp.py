import streamlit as st 
import pandas as pd
import numpy as np
import datetime
import streamlit_shadcn_ui as ui


st.set_page_config(page_title="Tuberculosis in Kenya: ",
                   layout="wide",
                   initial_sidebar_state="expanded")

st.markdown("""<style>
            .block-container {
                padding-top:0rem;}
                </style>""", 
            unsafe_allow_html=True)

st.markdown("""<style>
            #MainMenu {visibility:hidden;}
            footer {visibility:hidden;}
            </style>""", 
            unsafe_allow_html=True)

with st.sidebar:
    st.subheader("Tuberculosis in Kenya: The Case of the Under 5 Child")