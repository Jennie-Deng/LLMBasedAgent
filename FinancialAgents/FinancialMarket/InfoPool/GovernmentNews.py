import ast
import pandas as pd
# Path to your txt file
file_path1 = "/Volumes/Jennie/Agent/FinAgents/FinAi/data/CorporateNews.txt"
file_path2="/Volumes/Jennie/Agent/FinAgents/FinAi/data/GovernmentIndustry.txt"

# Read and parse the file content
with open(file_path1, 'r') as file:
    content = file.read()
    data_list1 = ast.literal_eval(content)
# Now data_list contains your list of dictionaries
data_list1

CorporateNews=pd.DataFrame(data_list1)
CorporateNews.set_index(CorporateNews['date'], inplace=True)
CorporateNews.to_csv('/Volumes/Jennie/Agent/FinAgents/FinAi/data/CorporateNews.csv')

with open(file_path2, 'r') as file:
    content = file.read()
    data_list2 = ast.literal_eval(content)

# Now data_list contains your list of dictionaries
data_list2
GovernmentIndustryNews=pd.DataFrame(data_list2)
GovernmentIndustryNews.index = GovernmentIndustryNews['date']
GovernmentIndustryNews.to_csv('/Volumes/Jennie/Agent/FinAgents/FinAi/data/GovernmentIndustryNews.csv')
