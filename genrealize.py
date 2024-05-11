import getpass
import os
import openai
import logging
import sys
from openai import OpenAI
import PIL.Image
from googleapiclient.discovery import build
import google.generativeai as genai
# import nest_asyncio
import os
import PyPDF2
import re
import requests
from bs4 import BeautifulSoup
import streamlit as st
# nest_asyncio.apply()
gemini_api_key=""
openai_api_key=""
genai.configure(api_key=gemini_api_key)
gemini_model = genai.GenerativeModel('gemini-pro')
openai.api_key = openai_api_key
GOOGLE_API_KEY=gemini_api_key
genai.configure(api_key=GOOGLE_API_KEY)
timestamping_model = genai.GenerativeModel('gemini-pro')

def topic_date_identifier(user_prompt):
  from openai import OpenAI
  os.environ['OPENAI_API_KEY'] = openai_api_key
  client = OpenAI()
  topic_prompt=user_prompt+" can you tell , on what topic is the user wanting research papers, don't write anything else,just the heading in 3-4 words"
  topic= client.chat.completions.create(model="gpt-3.5-turbo",messages=[{"role": "user", "content": topic_prompt}]).choices[0].message.content
  date_prompt=user_prompt+" can you tell , on what date range is the user wanting research papers, don't write anything else, just the start date"
  date = client.chat.completions.create(model="gpt-3.5-turbo",messages=[{"role": "user", "content": date_prompt}]).choices[0].message.content
  return [topic,date]

def webscrape_ainews(search_query):
  search_query=search_query.replace(' ', '+')
  results=[]
  try:
    r=requests.get("https://www.artificialintelligence-news.com/?s="+search_query)
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('main', class_='main small-12 medium-8 large-8 cell')
    content = s.find_all('article')
    for article in content:
      result=[]
      result.append(article.find('a')['href'])
      result.append(article.find('a').text.strip())
      results.append(result)
    return results
  except:
    return []

def webscrape_arix(search_query):
  search_query=search_query.replace(' ', '+')
  results=[]
  try:
    r=requests.get("https://arxiv.org/search/?query="+search_query+"&searchtype=all&source=header")
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('ol', class_='breathe-horizontal')
    content = s.find_all('li')
    for article in content:
      result=[]
      result.append(article.find('p',class_='title is-5 mathjax').text.strip())
      result.append(article.find('div',class_='is-marginless').find('p',class_='list-title is-inline-block').find('span').find('a')['href'])
      results.append(result)
    return results
  except:
    return []

def download_file(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print("Downloaded successfully as", filename)
    else:
        print("Failed to download:", response.status_code)

def paper_summarizer(url):
  from openai import OpenAI
  client = OpenAI()
  download_file(url, 'downloaded_paper')
  pdf_summary_text=""
  pdf_file_path=r"C:\Users\whyis\Desktop\GenRealize\downloaded_paper.pdf"
  pdf_file=open(pdf_file_path,'rb')
  pdf_reader=PyPDF2.PdfReader(pdf_file)
  for page_num in range(len(pdf_reader.pages)):
    page_text=pdf_reader.pages[page_num].extract_text().lower()
    # os.environ['OPENAI_API_KEY'] = userdata.get('openai_api_key')
    summar_text="You are a helpful research assistant, summarize the following content:"+page_text
    summarized_text = client.chat.completions.create(model="gpt-3.5-turbo",messages=[{"role": "user", "content": summar_text}]).choices[0].message.content
    pdf_summary_text+=summarized_text
  return pdf_summary_text

def summarize_news(url):
  response = gemini_model.generate_content("you are a helpful news assistant , help me summarize the following news article"+url, stream=True)
  response.resolve()
  return response.text

# def main():
#     st.title("GenRealize - What's in the AI World!")
#     user_input = st.text_input("Enter your time frame:")
#     if user_input:
#         response = topic_date_identifier(user_input)
#         if st.button("Research Papers"):
#             research_paper_links=webscrape_arix(response[1])
#             for count in range(len(research_paper_links)):
#               st.text_area(research_paper_links[count][0]+": ", value=research_paper_links[count][1])
#         if st.button("News & Events"):
#             news_links=webscrape_ainews(response[1])
#             for count in range(len(news_links)):
#               st.text_area(news_links[count][0]+": ", value=news_links[count][1])

#     st.subheader("Summarizer")
#     news_input=st.text_input("Summarize News Event")
#     if st.button("Go"):
#       summarized_news=summarize_news(news_input)
#       st.text_area(summarized_news)

#     paper_input=st.text_input("Summarize Research Paper")
#     if st.button("Go"):
#       summarized_paper=paper_summarizer(paper_input)
#       st.text_area(summarized_paper)

# if __name__ == "__main__":
#     main()
