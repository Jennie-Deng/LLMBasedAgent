from crewai import Agent, Task, Crew, Process
from openai import OpenAI
from langchain_openai import ChatOpenAI
import json
import os


os.environ["OPENAI_API_KEY"] = "sk-T2QXqSmLhdFRbr44352418B0F8D3498dA077C0EbE34b415a"
os.environ["OPENAI_API_BASE"] = "https://api.xi-ai.cn/v1"

#government and Fed news
Agent1 = Agent(
    role="news generator",
    goal="generate 3 important national news and 4 important about interest rate news from the Federal Reserve.",
    backstory="you are a new reporter in USA, you can write and publish news ", # Added backstory
    verbose=True,
    llm=ChatOpenAI(model_name="gpt-4o", temperature=0.7),
    allow_delegation=True,
)

Task1=Task(
    description= "generate 3 important national news and 4 important about interest rate news from the Federal Reserve."
                  "the 3 inportant news may be bad news: finanical crisis, disasters, wars or good news: the opening olympics"
                  "collabrations with other countries..."
                  "Simulate Fed to increase rate or decrease rate"
                  "news is categoty by Government, Fed",
    expected_output = "7 news with date, title, content, source, level and sentiment with jason format",
    agent=Agent1,
    output_format="json"
)

my_crew = Crew(agents=[Agent1],
               tasks=[Task1],
               verbose=True,
               )
GovermentFedNews= my_crew.kickoff()

#insudtry news
Agent2 = Agent(
    role="news generator",
    goal="generate 110 industrial news.",
    backstory="you are a new reporter from stock exchange in USA, you can write and publish instrial news ", # Added backstory
    verbose=True,
    llm=ChatOpenAI(model_name="gpt-4o", temperature=0.7),
    allow_delegation=True,
)
# 11 industries: Energy，Materials，Industrials，Consumer Staples，Consumer Discretionary，Healthcare，Financials, Information Technology， Communication Services，
# Utilities， Real Estate
Task2=Task(
    description= "this task need genenrate 110 indutrial news from 11 industries in NYSE."
                "the 11 industries includes Healthcare, Real Estate"
                 "in general, every industry has 10 news ."
                 "the source incuding which industy",
    expected_output = "110 news with date, title, content, source, and sentiment with jason format",
    agent=Agent1,
    output_format="json"
)

my_crew = Crew(agents=[Agent2],
               tasks=[Task2],
               verbose=True,
               )
industryNews= my_crew.kickoff()


Agent3 = Agent(
    role="corporte news generator",
    goal="Simulate 50 important corporte news for 10 comnanies in {industry} industry.",
    backstory="You are a financial news editor who frequently writes about company stock prices."
              "The content of your articles may include aspects such as the quality of financial reports, changes in company management,"
              " mergers and acquisitions, product launches, financial fraud by the company, or issues with product quality.", # Added backstory
    verbose=True,
    llm=ChatOpenAI(model_name="gpt-4o", temperature=0.7),
    allow_delegation=True,
)
Task3=Task(
    description= "there are 10 different companies. Their stock codes are from {code range}."
                  " this task needs to wtite 5 shor-form corporte news for every company in {industry} industry."
                  "these news are financial news, which include one of the following topics:financial reports, changes in company management"
                  "mergers and acquisitions, product launches, financial fraud by the company, or issues with product quality",
    expected_output = "50 news with stock code, date, title, content, industry, and sentiment, using jason format",
    agent=Agent1,

)

my_crew = Crew(agents=[Agent3],
               tasks=[Task3],
               #manager_agent=manager,
               #manager_llm=manager2,
               #process=Process.hierarchical,
               #memory=True,
               #planning=True,
               verbose=True,
               output_format="json",
               output_log_file="news.json",
               )
CorporateNews=my_crew.kickoff({"industry":"Industrials","code range":"101-110"})