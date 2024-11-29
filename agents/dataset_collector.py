import requests
import json

# API Key for SerpAPI
SERPAPI_KEY = "00f0bdf6f347bc7afa42b7c0219d2709893a30e275af60bc4db9756134391f62"

def fetch_datasets_with_serpapi(keywords):
    """
    Use SerpAPI to search for dataset links from Kaggle, GitHub, and HuggingFace.
    Returns a dictionary with platform names as keys and clickable links as values.
    """
    # Query strings for each platform
    queries = {
        "Kaggle": f"{keywords} site:kaggle.com",
        "GitHub": f"{keywords} site:github.com",
        "HuggingFace": f"{keywords} site:huggingface.co"
    }

    dataset_links = {}

    for platform, query in queries.items():
        # SerpAPI search URL
        search_url = "https://serpapi.com/search"
        params = {
            "q": query,
            "api_key": SERPAPI_KEY,
            "num": 5  # Fetch top 5 results
        }

        try:
            response = requests.get(search_url, params=params)
            if response.status_code == 200:
                results = response.json().get("organic_results", [])
                # Extract clickable links from the results
                links = [result["link"] for result in results if "link" in result]
                dataset_links[platform] = links
            else:
                dataset_links[platform] = [f"Error fetching datasets from {platform} (status code: {response.status_code})"]
        except Exception as e:
            dataset_links[platform] = [f"Error fetching datasets from {platform}: {e}"]

    return dataset_links

# Example Usage
keywords ="Unlock Supply Chain Insights with Explainable AI-driven Optimization"
dataset_links = fetch_datasets_with_serpapi(keywords)

# Save results to JSON file
with open("dataset_links.json", "w") as file:
    json.dump(dataset_links, file, indent=4)

# Print the results with clickable links
for platform, links in dataset_links.items():
    print(f"\n{platform} Datasets:")
    for link in links:
        print(f"- [{link}]({link})")
