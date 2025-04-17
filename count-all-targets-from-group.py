import requests
import os

BASE_URL = "https://api.snyk.io/rest"
SNYK_TOKEN = os.getenv("SNYK_TOKEN")
GROUP_ID = ""
API_VERSION = "version=2024-10-15"


def get_organizations():
    # Step 1: Construct URL
    url = f"{BASE_URL}/orgs?{API_VERSION}"

    # Step 2: Define headers
    headers = {
        "Authorization": f"token {SNYK_TOKEN}",
        "Content-Type": "application/vnd.api+json",
        "Accept": "application/vnd.api+json"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json().get("data", [])

        org_ids = [{"id": org["id"], "name": org["attributes"]["name"]} for org in data]
        return org_ids
    else:
        print(f"Error getting organizations: {response.status_code}, {response.text}")
        return None


organizations = get_organizations()

if organizations:
    print("Organizations:")
    for org in organizations:
        print(f"ID: {org['id']}, Name: {org['name']}")
else:
    print("No organizations found or there was an error.")


def get_targets(org_id):
    url = f"{BASE_URL}/orgs/{org_id}/targets?{API_VERSION}"
    headers = {
        "Authorization": f"token {SNYK_TOKEN}",
        "Accept": "application/vnd.api+json",
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        targets_data = response.json().get("data", [])
        return targets_data
    else:
        print(f"Error getting targets for organization {org_id}: {response.status_code}, {response.text}")
        return None


if organizations:
    print("\nTarget Counts per Organization:")
    total_target_count = 0
    for org in organizations:
        org_id = org['id']
        org_name = org['name']
        targets = get_targets(org_id)
        if targets is not None:
            target_count = len(targets)
            print(f"Organization: {org_name} (ID: {org_id}) - Number of Targets: {target_count}")
            total_target_count += target_count
        else:
            print(f"Could not retrieve targets for organization: {org_name} (ID: {org_id})")

    print(f"\nTotal Number of Targets Across All Organizations: {total_target_count}")
else:
    print("\nCould not retrieve target counts as no organizations were found.")
