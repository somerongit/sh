import requests
import csv
from datetime import datetime

# Replace with your values
GITHUB_TOKEN = "your_personal_access_token"
ORG = "your_org_name"
START_DATE = "2026-01-01T00:00:00Z"
END_DATE = "2026-01-31T23:59:59Z"

BASE_URL = "https://api.github.com"

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def get_repos(org, start_date):
    url = f"{BASE_URL}/orgs/{org}/repos"
    params = {"per_page": 100}
    repos = []
    while url:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            raise Exception(f"Error fetching repos: {response.status_code}, {response.text}")
        data = response.json()
        for repo in data:
            pushed_at = repo.get("pushed_at")
            if not repo.get("archived") and pushed_at and pushed_at >= start_date:
                repos.append(repo["name"])
        if "next" in response.links:
            url = response.links["next"]["url"]
            params = None
        else:
            url = None
    return repos

def get_branches(org, repo):
    url = f"{BASE_URL}/repos/{org}/{repo}/branches"
    params = {"per_page": 100}
    branches = []
    while url:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            raise Exception(f"Error fetching branches for {repo}: {response.status_code}, {response.text}")
        data = response.json()
        branches.extend([branch["name"] for branch in data])
        if "next" in response.links:
            url = response.links["next"]["url"]
            params = None
        else:
            url = None
    return branches

def get_commits(org, repo, branch, start_date, end_date):
    url = f"{BASE_URL}/repos/{org}/{repo}/commits"
    params = {
        "sha": branch,
        "since": start_date,
        "until": end_date,
        "per_page": 100
    }
    commits = []
    while url:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            raise Exception(f"Error fetching commits for {repo}/{branch}: {response.status_code}, {response.text}")
        data = response.json()
        for commit in data:
            commits.append({
                "sha": commit.get("sha"),
                "repo": repo,
                "author": commit.get("commit", {}).get("author", {}).get("name"),
                "date": commit.get("commit", {}).get("author", {}).get("date"),
                "message": commit.get("commit", {}).get("message"),
                "url": commit.get("html_url")
            })
        if "next" in response.links:
            url = response.links["next"]["url"]
            params = None
        else:
            url = None
    return commits

if __name__ == "__main__":
    repos = get_repos(ORG, START_DATE)
    seen_commits = set()

    # Dynamic filename: org + date range + runtime timestamp
    runtime = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"commits_{ORG}_{START_DATE[:10]}_to_{END_DATE[:10]}_{runtime}.csv"

    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["repo", "author", "date", "message", "url"])
        writer.writeheader()

        for repo in repos:
            print(f"Fetching branches for repo: {repo}")
            branches = get_branches(ORG, repo)
            for branch in branches:
                print(f"  Checking branch: {branch}")
                commits = get_commits(ORG, repo, branch, START_DATE, END_DATE)
                for c in commits:
                    if c["sha"] not in seen_commits:
                        seen_commits.add(c["sha"])
                        writer.writerow({
                            "repo": c["repo"],
                            "author": c["author"],
                            "date": c["date"],
                            "message": c["message"],
                            "url": c["url"]
                        })

    print(f"Commits across all branches exported to {filename}")
