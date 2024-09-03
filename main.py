from icecream import ic

import streamlit as st
from scrape import scrape_website


st.title("AI Web Scraper")
url = st.text_input("Enter URL: ")

if st.button("Scrape the site"):
    st.write("Scraping the site...")
    result = scrape_website(url)
    ic(result)
