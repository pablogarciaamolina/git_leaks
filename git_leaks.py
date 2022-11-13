#! user/bin/python
from asyncio.format_helpers import extract_stack
from git import Repo

import re


REPO_DIR = "./skale/skale-manager"

PATTERN = '(password|Credentials|key)'

# def handler_signal(signal, frame):
#     print("\n\n [!] Out .........\n")
#     sys.exit(1)

# #Control+C
# signal.signal(signal.SIGINT, handler_signal)

def extract(path: str) -> list:
    repo = Repo(path)
    
    return list(repo.iter_commits())


def transform(commits: list, found: list=[]) -> list:
    
    for commit in commits:
        s = re.findall(PATTERN, commit.message, re.I)

        found.append([commit,s]) if s != [] else None 

    return found
    ...

def load(found: list):

    file = open('secrets.txt','w')

    for secret in found: file.write(f'>> {secret[0].message}')

    file.close()
    ...

if __name__ == "__main__":
    
    # #Control+C
    # signal.signal(signal.SIGINT, handler_signal)

    commits = extract(REPO_DIR)
    found = transform(commits)
    load(found)