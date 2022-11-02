# Write a program in python that will read a file from a repository
# The program should then replace all the instances of the text "Andrew" with my name "Michelle"
# The program should then commit those changes and push the file back to the repository.

# Author : Michelle O'Connor

import requests
import json
from github import Github
from config import config as cfg

apiKey = cfg["key"]
