import streamlit as st
import asyncio
import nest_asyncio
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import load_config, check_reachability, connect_to_olt

nest_asyncio.apply()
config = load_config()

# Selenium Setup
@st.cache_resource
def init_driver():
    options = Options()
    options.add_argument("--headless") # Headless for deployment
    return webdriver.Chrome(options=options)

driver = init_driver()

st.title("🔍 ONU Checker")

if st.button("Verify Login"):
    driver.get(config['smartolt_url'])
    st.session_state.logged_in = True
    st.success("Ready!")

if st.session_state.get('logged_in'):
    username = st.text_input("Username/Serial:")
    if st.button("Search"):
        # Logic to use selenium, parse table, and call connect_to_olt
        # Example call: 
        # results = asyncio.run(connect_to_olt(ip, type, port, id, config['olt_credentials']))
        st.write("Search executed.")
