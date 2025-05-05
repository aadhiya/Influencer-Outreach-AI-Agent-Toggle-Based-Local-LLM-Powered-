# streamlit_app.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
from app.services.gmail_service import send_emails_with_followup
from app.services.ollama_service import personalize_message
from app.services.scrape_emails import batch_search_emails as scrape_emails

from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Investor Email Outreach Agent", layout="centered")
st.title("📬 Investor Outreach Agent")

st.markdown("Upload a CSV file with a column named `name` containing investor names.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    if "name" not in df.columns:
        st.error("CSV must have a column named 'name'")
    else:
        st.success("Investor names loaded successfully.")
        investor_names = df["name"].tolist()

        st.markdown("### ✉️ Customize Your Message")
        subject = st.text_input("Email Subject", value="Introducing AImodularity – A Seed Round Opportunity")

        default_message = (
            "<p>Hello,</p>"
            "<p>We’re opening up our seed round and would love to share our vision with you. Here’s a short deck:"
            " <a href=\"https://gamma.app/docs/AImodularity-tfwp4h4khivmrrz\">AImodularity Deck</a>.</p>"
            "<p>Looking forward to hearing your thoughts.</p>"
            "<p>Best,<br>Team AImodularity</p>"
        )

        message = st.text_area("Email Body (HTML Allowed)", height=250, value=default_message)

        personalize = st.checkbox("🔁 Use Ollama to personalize messages")
        follow_up = st.checkbox("📆 Schedule follow-up emails (3 days)")

        uploaded_attachment = st.file_uploader("📎 Add Optional Attachment (PDF, DOCX, etc.)", type=["pdf", "docx"])

        if st.button("Run Outreach Agent"):
            with st.spinner("Scraping emails..."):
                email_map = scrape_emails(investor_names)

             # 👇 Force override for testing
            email_map = [{"name": "Aadhiya Thomas", "emails": "aadhiyamaria@gmail.com"}]

            st.success("Emails scraped!")
            st.write(email_map)
            with st.spinner("Sending emails..."):
                results = send_emails_with_followup(
                    email_map=email_map,
                    subject=subject,
                    body=message,
                    personalize=personalize,
                    follow_up=follow_up,
                    attachment=uploaded_attachment
                )

            st.success("Emails sent!")
            st.dataframe(results)

            csv = pd.DataFrame(results).to_csv(index=False).encode("utf-8")
            st.download_button("📥 Download Log", csv, "email_results.csv", "text/csv")
