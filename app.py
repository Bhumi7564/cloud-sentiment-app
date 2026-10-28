
import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

st.set_page_config(
    page_title="Review Sentiment Checker",
    page_icon="💬"
)

st.title("💬 Review Sentiment Checker")

st.write(
    "Enter a product or movie review "
    "to check whether it is positive or negative."
)

review = st.text_area("Write your review here:")

if st.button("Check Sentiment"):
    if review.strip():
        analyzer = SentimentIntensityAnalyzer()
        score = analyzer.polarity_scores(review)["compound"]

        if score >= 0.05:
            st.success("😊 Positive Sentiment")
        elif score <= -0.05:
            st.error("😞 Negative Sentiment")
        else:
            st.info("😐 Neutral Sentiment")

        st.write("Sentiment Score:", round(score, 3))
    else:
        st.warning("Please enter a review first.")
