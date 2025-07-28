import requests

url = 'https://api.github.com/search/repositories&q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

response_dict = r.json()

print(f"Total repositories: {response_dict['total_count']}")

repo_dicts = response_dict['items']
print(f"Repositories returnes: {len(repo_dicts)}")

repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)