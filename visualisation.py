# I took inspiration for how to organise all of this and actually use the graph tool from a classmate here https://github.com/Seyekt/GitHub-Visualisation

from github import Github
from githubAPI import *
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def labelFunction(val):
	return f'{val / 100 * len(data):.0f}\n{val:.0f}%'

sns.set_theme()

g = Github()
tokenPresent = 0

try:
	tokentext = open("token.txt")
except FileNotFoundError:
	print("Token file not found.")
	username = input("Enter GitHub username: ")
	user = g.get_user(username)	
else:
	token = tokentext.readline()
	g = Github(token)
	user = g.get_user()
	tokenPresent = 1

	
repoData = repoToData(user)
issueData = issuesToData(user)

data = pd.DataFrame.from_dict(repoData, orient = 'index', columns = ["Repository Name", "Programming language", 
"Date created", "Date Last Pushed", "Repo Commits", "Star Count"])

dataTwo = pd.DataFrame.from_dict(issueData, orient = 'index', columns = ["Issue ID", "No of Comments", "Date created", 
"Date Closed"])

numberOfCommits = data.sort_values(by = ['Repo Commits'], ascending = True)
plot = sns.barplot(data = numberOfCommits[0:10], x = 'Repo Commits', y = 'Repository Name', palette = 'mako')
plot.set_title(user.login + " Repository Commits")

plt.show()

data.groupby('Programming language').size().plot(kind = 'pie', autopct = labelFunction, textprops = {'fontsize': 14}, ylabel = 'By Language')

plt.show()

if(tokenPresent):
	commentsOnIssues = dataTwo.sort_values(by = ['No of Comments'], ascending = False)
	plot = sns.barplot(data = commentsOnIssues[0:10], x = 'Issue ID', y = 'No of Comments', palette = 'rocket')
	plot.set_title(user.login + " No of User Issues")

	plt.show()