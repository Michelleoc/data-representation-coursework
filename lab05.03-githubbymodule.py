from github import Github
from config import config as cfg

apikey = cfg["key"]

g = Github(apikey)

for repo in g.get_user().get_repos():
    print(repo.name)
