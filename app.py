import PDolar as PE
import streamlit as st


data = PE.last_days_data(days=10)

st.dataframe(data["he"])
