
# GenRealize - What's in the AI World!

An AI bot aggregating research papers and AI news from various sources. Utilizing web scraping and Genmini for article summarization, along with ChatGPT-4 for research paper summaries, it offers a centralized platform for accessing curated content.


## API References

#### Get all items

Get the following api keys from respective links and save them as environment variables.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `openai_api_key` | `string` | **Get From:** https://platform.openai.com/account/organization |
| `gemini_api_key` | `string` | **Get From:** https://aistudio.google.com/app/prompts/new_chat?utm_source=agd&utm_medium=referral&utm_campaign=core-cta&utm_content= |

## Terminal setup
Open vs code and create a new virtual environment by following commands
```bash
  python -m venv Genrealize_env
```
```bash
  Genrealize_env\Scripts\activate
```
Install the required libraries for the project using the following pip install

```bash
pip install google-generativeai llama-index llama-index-embeddings-together llama-index-llms-together openai langchain langchainhub llama-index-llms-langchain streamlit google-api-python-client pyPDF2
```
## Python files
put the respective codes in genrealize.py and streamlit.y files code in a file knowmad.py, This file contains all important functions necessary to perform web scraping and summarization tasks.
## Deployment

To deploy this project using streamlit run the following command in your app.py file

```bash
  streamlit run streamlit.py
```

