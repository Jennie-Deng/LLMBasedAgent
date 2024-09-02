from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = "sk-T2QXqSmLhdFRbr44352418B0F8D3498dA077C0EbE34b415a"
os.environ["OPENAI_API_BASE"] = "https://api.xi-ai.cn/v1"


# # 创建生成代理的Agents
# def create_agent_profile(agent_type:[],n:[int]):
#     generator_agent = Agent(
#         role=f"{agent_type}Profile Generator",
#         goal=f"Generate {n} unique profiles with name and {n} risk-averse coefficient",
#         backstory="This agent is responsible for generating {n} unique profiles for future agents' descreption.",  # Added backstory
#         verbose=True,
#         llm=ChatOpenAI(model_name="gpt-4o", temperature=0.7)
#     )
#     return generator_agent

#rationalAgent
Agent1 = Agent(
    role="Profile Generator for Rational Agent",
    goal="Generate 30 unique profiles with name and 30 risk-averse coefficient and rational ragent type",
    backstory="This agent is responsible for generating 30 unique profiles for 30 agents for future multi-agent system.", # Added backstory
    verbose=True,
    llm=ChatOpenAI(model_name="gpt-4o", temperature=0.7),
    allow_delegation=True,
)
#rationalTask
Task1=Task(
    description= "Generate 30 unique name and 30 risk-averse coefficient (a number between 2 and 4) "
                 "for agents in a multi-agent system. The risk-averse coefficient should reflect "
                  "the agent's risk preference. Risk-averse coefficient between 2 and 4, "
                  "indicating the agent maintains a balanced approach when weighing returns against risks. ",
    expected_output = "30 names and clarity the agent type  and includes 30 risk-averse coefficients in a json data file",
    agent=Agent1,
    output_format="json"
)
#OverconfidenceLossAverse
Agent2 = Agent(
    role="Profile Generator for Overconfidence Loss Averse Agent",
    goal="Generate 30 unique profiles with name and 30 risk-averse coefficient and Overconfidence Loss Averse Agent type",
    backstory="This agent is responsible for generating 30 unique profiles for 30 agents for future multi-agent system.", # Added backstory
    verbose=True,
    llm=ChatOpenAI(model_name="gpt-4o", temperature=0.7),
    allow_delegation=True,
)
#OverconfidenceLossAverse
Task2=Task(
    description= "Generate 30 unique name and 30 risk-averse coefficient (a number between 4 and 10) "
                 "for agents in a multi-agent system. The risk-averse coefficient should reflect "
                  "the agent's risk preference. Risk-averse coefficient between 4 and 10, "
                  "indicating the agent highly risk-averse and prefer to choose low-risk portfolios, even if it means accepting lower expected returns ",
    expected_output = "30 names and clarity the agent type and includes 30 risk-averse coefficients in a json data file",
    agent=Agent2,
    output_format="json"
)
#AnchoringHerdingAgent
Agent3 = Agent(
    role="Profile Generator for Anchoring Herding Agent",
    goal="Generate 30 unique profiles with name and Anchoring Herding agent type",
    backstory="This agent is responsible for generating 30 unique profiles for 30 agents for future multi-agent system.", # Added backstory
    verbose=True,
    llm=ChatOpenAI(model_name="gpt-4o", temperature=0.7),
    allow_delegation=True,
)
#AnchoringHerding
Task3=Task(
    description= "Generate 30 unique name",
    expected_output = "30 names and clarity the agent type in a json data file",
    agent=Agent3,
    output_format="json"
)

#NoiseTraderOverreacting
Agent4 = Agent(
    role="Profile Generator for Noise Trader Overreacting Agent",
    goal="Generate 30 unique profiles with name and Noise Trader Overreacting agent type",
    backstory="This agent is responsible for generating 30 unique profiles for 30 agents for future multi-agent system.", # Added backstory
    verbose=True,
    llm=ChatOpenAI(model_name="gpt-4o", temperature=0.7),
    allow_delegation=True,
)
#NoiseTraderOverreacting
Task4=Task(
    description= "Generate 30 unique name",
    expected_output = "30 names and clarity the agent type in a json data file",
    agent= Agent4,
    output_format="json"
)

#SelfAttributionBias
Agent5 = Agent(
    role="Profile Generator for Self-Attribution Bias Overconfident Agent",
    goal="Generate 30 unique profiles with name and Self-Attribution Bias Overconfident agent type",
    backstory="This agent is responsible for generating 30 unique profiles for 30 agents for future multi-agent system.", # Added backstory
    verbose=True,
    llm=ChatOpenAI(model_name="gpt-4o", temperature=0.7),
    allow_delegation=True,
)
#SelfAttributionBias
Task5=Task(
    description= "Generate 30 unique name",
    expected_output = "30 names and clarity the agent type in a json data file",
    agent=Agent5,
    output_format="json"
)
#AnchoringLossAverse
Agent6 = Agent(
    role="Profile Generator for Anchoring Loss Averse Agent",
    goal="Generate 30 unique profiles with name and Anchoring Loss Averse agent type",
    backstory="This agent is responsible for generating 30 unique profiles for 30 agents for future multi-agent system.", # Added backstory
    verbose=True,
    llm=ChatOpenAI(model_name="gpt-4o", temperature=0.7),
    allow_delegation=True
)
#AnchoringLossAverse
Task6=Task(
    description= "Generate 30 unique name",
    expected_output = "30 names and clarity the agent type in a json data file",
    agent=Agent6,
    output_format="json"
)
#HerdingOverreacting
Agent7 = Agent(
    role="Profile Generator for Herding Overreacting Agent",
    goal="Generate 30 unique profiles with name and Herding Overreacting agent type",
    backstory="This agent is responsible for generating 30 unique profiles for 30 agents for future multi-agent system.", # Added backstory
    verbose=True,
    llm=ChatOpenAI(model_name="gpt-4o", temperature=0.7),
    allow_delegation=True,
)
#HerdingOverreacting
Task7= Task(
    description= "Generate 30 unique name",
    expected_output = "30 names and clarity the agent type in a json data file",
    agent=Agent7,
    output_format="json"
)

manager=Agent(
    role="project manager",
    goal="collect all the 150 agents' profiles and generate a csv file which I can download",
    backstory="This agent is responsible for collecting all the 150 agents' profiles after they give final profiles and generate a csv file",
    allow_delegation=True,

)
#manager2=ChatOpenAI(model_name="gpt-4o")
my_crew = Crew(agents=[Agent1,Agent2,Agent3,Agent4,Agent5],
               tasks=[Task1, Task2,Task3,Task4,Task5],
               manager_agent=manager,
               #manager_llm=manager2,
               process=Process.hierarchical,
               memory=True,
               planning=True,
               verbose=True,
               )
all_agent_profile = my_crew.kickoff()


manager2=Agent(
    role="project manager",
    goal="collect all the 60 agents' profiles and generate a csv file which I can download",
    backstory="This agent is responsible for collecting all the 60 agents' profiles after they give final profiles and generate a csv file",
    allow_delegation=True,

)

#AnchoringLossAverse
Agent6 = Agent(
    role="Profile Generator for Anchoring Loss Averse Agent",
    goal="Generate 30 unique profiles with name and Anchoring Loss Averse agent type",
    backstory="This agent is responsible for generating 30 unique profiles for 30 agents for future multi-agent system.", # Added backstory
    verbose=True,
    llm=ChatOpenAI(model_name="gpt-4o", temperature=0.7),
    allow_delegation=True
)
#AnchoringLossAverse
Task6=Task(
    description= "Generate 30 unique name",
    expected_output = "30 names and clarity the agent type in a json data file",
    agent=Agent6,
    output_format="json"
)
#HerdingOverreacting
Agent7 = Agent(
    role="Profile Generator for Herding Overreacting Agent",
    goal="Generate 30 unique profiles with name and Herding Overreacting agent type",
    backstory="This agent is responsible for generating 30 unique profiles for 30 agents for future multi-agent system.", # Added backstory
    verbose=True,
    llm=ChatOpenAI(model_name="gpt-4o", temperature=0.7),
    allow_delegation=True,
)
#HerdingOverreacting
Task7= Task(
    description= "Generate 30 unique name",
    expected_output = "30 names and clarity the agent type in a json data file",
    agent=Agent7,
    output_format="json"
)


my_crew2 = Crew(agents=[Agent6, Agent7],
               tasks=[Task6,Task7],
               manager_agent=manager2,
               process=Process.hierarchical,
               memory=True,
               planning=True,
               verbose=True,
               )
all_agent_profile = my_crew2.kickoff()