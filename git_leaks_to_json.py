from git_leaks import *
import json
from git import Commit

def load_to_json(found: list[list]):
    '''
    -> found: list of lists: [Commit, ocurrences of leak in the Commit message]
    '''

    # with open("secrets.json", "w") as outfile:
        
    #     for leak in found:
    #         commit: Commit = leak[0]
    #         commit_dict = {
    #             'author': commit.author.name,
    #             'commiter': commit.committer.name,
    #             'commited_date': commit.committed_date,
    #             'message': commit.message,
    #             'ocurrences': leak[1]
    #             }
    #         json.dump(commit_dict, fp=outfile, skipkeys=True, indent=4)

    secrets = {'leaking_commits': []}
    for leak in found:
        commit: Commit = leak[0]
        commit_dict = {
                'author': commit.author.name,
                'commiter': commit.committer.name,
                'commited_date': commit.committed_date,
                'message': commit.message,
                'ocurrences': leak[1]
                }
        secrets['leaking_commits'].append(commit_dict)
    
    with open("secrets.json", "w") as outfile:
        json.dump(secrets, fp=outfile, skipkeys=True, indent=3)



if __name__ == '__main__':

    commits = extract(REPO_DIR)
    found = transform(commits)
    load_to_json(found)