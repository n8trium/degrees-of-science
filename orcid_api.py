import requests

# Replace this with the ORCID ID you want to query
orcid_id = "0000-0001-2345-6789"  # Example ORCID ID

# ORCID API endpoint for fetching public record
url = f"https://pub.orcid.org/v3.0/{orcid_id}/works"

# Define headers for authorization
headers = {
    "Accept": "application/json",
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    # Now you can process the JSON data to get publications
    for work in data['group']:
        print(work['work-summary'][0]['title']['title']['value'])
else:
    print(f"Error fetching data: {response.status_code}")
