# streamlit_app.py

import streamlit as st
import pandas as pd
from app.services.scrape_emails import batch_search_emails

st.title("Investor Email Finder (via SerpAPI)")

uploaded_file = st.file_uploader("Upload CSV with investor names", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    if "name" not in df.columns:
        st.error("CSV must have a column named 'name'")
    else:
        st.write("✅ Investor names loaded:")
        st.write(df["name"])

        if st.button("🔍 Find Emails"):
            with st.spinner("Searching for emails..."):
                results = batch_search_emails(df["name"].tolist())
                output_df = pd.DataFrame(results)
                st.success("Done!")

                st.write(output_df)

                csv = output_df.to_csv(index=False).encode("utf-8")
                st.download_button(
                    label="📥 Download Results CSV",
                    data=csv,
                    file_name="investor_emails.csv",
                    mime="text/csv"
                )
