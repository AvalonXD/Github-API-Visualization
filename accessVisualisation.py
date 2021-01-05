from github import Github

username = input("Please input a valid GitHub username here: ")

try:
    token = input("Please enter a valid OAuth Token: ")
    g = Github(token)
    user = g.get_user(username)
    print("Your token is valid - Good Job")
except:
    print("Bad Credentials - will continue running program with no token but it will be ratelimited!")
    g = Github()
    user = g.get_user(username)