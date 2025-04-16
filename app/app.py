import streamlit as st
import requests

API_BASE = st.secrets["api"]["url"]

st.title("Staff Manager")

# Create staff
with st.form("add_staff"):
    name = st.text_input("Name")
    dept = st.text_input("Department")
    submitted = st.form_submit_button("Add Staff")
    if submitted:
        r = requests.post(f"{API_BASE}/staff", json={"name": name, "department": dept})
        st.success(r.json()["msg"])

# View staff
st.subheader("All Staff")
res = requests.get(f"{API_BASE}/staff")
if res.ok:
    st.table(res.json())
