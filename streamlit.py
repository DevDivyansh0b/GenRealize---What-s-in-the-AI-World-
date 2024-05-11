from genrealize import topic_date_identifier,webscrape_ainews,webscrape_arix,paper_summarizer,summarize_news
import streamlit as st
st.title("GenRealize - What's in the AI World!")
user_input = st.text_input("Enter your time frame:")
if user_input:
    response = topic_date_identifier(user_input)
    if st.button("Research Papers"):
        research_paper_links=webscrape_arix(response[1])
        for count in range(len(research_paper_links)):
            st.text_area(research_paper_links[count][0]+": ", value=research_paper_links[count][1])
    if st.button("News & Events"):
        news_links=webscrape_ainews(response[1])
        for count in range(len(news_links)):
            st.text_area(news_links[count][0]+": ", value=news_links[count][1])

st.subheader("Summarizer")
news_input=st.text_input("Summarize News Event")
if st.button("Go News"):
    summarized_news=summarize_news(news_input)
    st.write(summarized_news)

paper_input=st.text_input("Summarize Research Paper")
if st.button("Go Paper"):
    summarized_paper=paper_summarizer(paper_input)
    st.write(summarized_paper)