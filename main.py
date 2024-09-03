from icecream import ic

import streamlit as st
from scrape import scrape_website, split_dom_content, clean_body_content, extract_body

from config import settings


ic.disable()

st.title("AI Web Scraper")
url = st.text_input("Enter URL: ")

if st.button("Scrape the site"):
    st.write("Scraping the site...")

    result = scrape_website(url)
    ic(result)

    body_content = extract_body(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=settings.web.height_text_area)
