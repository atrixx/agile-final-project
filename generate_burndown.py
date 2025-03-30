import matplotlib.pyplot as plt
import requests
import datetime

# GitHub repository details
owner = "atrixx"
repo = "agile-final-project"
milestone = "Sprint 1"

# Get issues from GitHub API
response = requests.get(f"https://api.github.com/repos/{owner}/{repo}/issues?milestone={milestone}&state=all")
issues = response.json()

# Process issues and calculate burndown data
dates = []
remaining_tasks = []

for issue in issues:
    if 'closed_at' in issue and issue['closed_at']:
        closed_at = datetime.datetime.strptime(issue['closed_at'], '%Y-%m-%dT%H:%M:%SZ')
        dates.append(closed_at.date())
    else:
        dates.append(datetime.datetime.now().date())
    remaining_tasks.append(len(issues) - issues.index(issue))

# Plot burndown chart
plt.figure(figsize=(10, 5))
plt.plot(sorted(dates), remaining_tasks)
plt.xlabel('Date')
plt.ylabel('Remaining Tasks')
plt.title('Burndown Chart')
plt.savefig('burndown_chart.png')
