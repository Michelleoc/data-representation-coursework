# Write a program in python that will read a file from a repository
# The program should then replace all the instances of the text "Andrew" with my name "Michelle"
# The program should then commit those changes and push the file back to the repository.

# Author : Michelle O'Connor

import requests
import json
from github import Github
from config import config as cfg

# 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

url = "https://github.com/Michelleoc/data-representation-coursework"
url1 = "https://github.com/Michelleoc/aprivateone"

apiKey = cfg["key"]

response = requests.get(url1, auth = ('token', apiKey))
print (response.status.code)

'''
g = Github(apiKey)

repo = g.get_repo("Michelleoc/aprivateone")

file_info = repo.get_contents("testing_Andrew_Michelle.txt")
file_url = file_info.download_url    

response = requests.get(file_url)
file_content = response.text
new_file_content = file_content.replace("Andrew", "Michelle")

github_response = repo.update_file(file_info.path,"Replace Andrew with Michelle",new_contents,file_info.sha)
print (github_response)
'''

