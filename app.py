import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain

os.environ['OPENAI_API_KEY'] = apikey

# app framework
st.title('History GPT')
prompt = st.text_input('Give me a year')

title_template = PromptTemplate(
  input_variables = ['topic'], 
  template = 'what was happening in the world during this year: {topic}'
)

# llms
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True)

# show stuff on the screen
if prompt:
  response = title_chain.run(topic=prompt)
  st.write(response)