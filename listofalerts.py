import requests
import json

# details of github repo
GITHUB_TOKEN = '<your-GitHub-API-token>'
REPO_OWNER = 'manoj-github-project'
REPO_NAME = 'sectest-as'

# GitHub API URL for code scanning alerts
url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/code-scanning/alerts'

# add authorization token
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def get_code_scanning_alerts(url, headers):
    alerts = []
    while url:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            alerts.extend(response.json())
            # Check if there is a next page of results
            if 'next' in response.links:
                url = response.links['next']['url']
            else:
                url = None
        else:
            print(f"Failed to retrieve alerts: {response.status_code} - {response.text}")
            break
    return alerts

alerts = get_code_scanning_alerts(url, headers)

# Print the alerts in JSON format for better readability
print(json.dumps(alerts, indent=2))
