# Write a program in python that will read a file from a repository
# The program should then replace all the instances of the text "Andrew" with my name "Michelle"
# The program should then commit those changes and push the file back to the repository.

# Author : Michelle O'Connor

import requests
from github import Github
from config import config as cfg

url = "Michelleoc/data-representation-courseware"

apiKey = cfg["key"]
g = Github(apiKey)

repo = g.get_repo("Michelleoc/data-representation-coursework")

file_info = repo.get_contents("testing_Andrew_Michelle.txt")
file_url = file_info.download_url    

response = requests.get(file_url)
file_content = response.text
new_content = file_content.replace("Andrew", "Michelle")

github_response = repo.update_file(file_info.path,"Replace Andrew with Michelle",new_content,file_info.sha)

