# streamlit_app.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
from app.services.gmail_service import send_emails_with_followup
from app.services.ollama_service import personalize_message
from app.services.scrape_emails import batch_search_emails as scrape_emails
from app.services.scrape_emails_v2 import process_name


from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Web Search Email Scraper", layout="wide")
st.title("🔍 Web-Based Email Discovery Agent")

st.markdown("Upload a CSV file with a column named `name` containing the names of individuals.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    if "name" not in df.columns:
        st.error("CSV must have a column named 'name'")
    else:
        st.success("Names loaded. Ready to scan the web.")

        if st.button("Start Email Discovery"):
            with st.spinner("Scraping emails..."):
                results = [process_name(name) for name in df["name"].tolist()]
                results_df = pd.DataFrame(results)

            st.success("✅ Done! Here are the results:")
            st.dataframe(results_df)

            csv = results_df.to_csv(index=False).encode("utf-8")
            st.download_button("📥 Download Results as CSV", csv, "email_results.csv", "text/csv")
