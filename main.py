from icecream import ic

import streamlit as st

from parse import parse_with_ollama
from scrape import scrape_website, split_dom_content, clean_body_content, extract_body

from config import settings


st.title("AI Web Scraper")
url = st.text_input("Enter URL: ")

if st.button("Scrape the site"):
    st.write("Scraping the site...")

    try:
        result = scrape_website(url)
        ic(result)

        body_content = extract_body(result)
        cleaned_content = clean_body_content(body_content)

        st.session_state.dom_content = cleaned_content

        with st.expander("View DOM Content"):
            st.text_area("DOM Content", cleaned_content, height=settings.web.height_text_area)
    except Exception as e:
        st.error(f"An error occurred while scraping the site: {str(e)}")

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse?")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")

            try:
                dom_chunks = split_dom_content(st.session_state.dom_content)
                result = parse_with_ollama(dom_chunks, parse_description)
                st.write(result)
            except Exception as e:
                st.error(f"An error occurred while parsing the content: {str(e)}")
                ic(f"Error in parsing: {str(e)}")
