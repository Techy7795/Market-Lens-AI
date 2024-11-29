# import requests

# def search_with_serpapi(query):
#     """
#     Perform a web search using SerpAPI.
#     """
#     params = {
#         "q": query,
#         "api_key": "5b4b4dba87bd2deb833a8e2dfe699d1e9dd60675a71a496d0fa3e831c6f5c953",  # Replace with your actual API key
#         "num": 5  # Number of results to fetch
#     }
#     url = "https://serpapi.com/search"
#     response = requests.get(url, params=params)
#     if response.status_code == 200:
#         return response.json().get("organic_results", [])
#     else:
#         return f"Error: {response.status_code}, {response.text}"

# def research_steel_industry(company_name):
#     """
#     Perform market research on the steel industry and the company.
#     """
#     queries = [
#         f"{company_name} industry analysis",
#         # f"{company_name} focus areas in steel production",
#         # "Steel industry AI adoption trends"
#     ]
    
#     # Perform searches for each query
#     results = {query: search_with_serpapi(query) for query in queries}
#     return results

# # Example Usage
# company_data = research_steel_industry("Tesla")
# for query, result in company_data.items():
#     print(f"Query: {query}\nResult: {result}\n")


# import requests
# import json

# def search_with_serpapi(query):
#     """
#     Perform a web search using SerpAPI and return the search results.
#     """
#     params = {
#         "q": query,
#         "api_key": "5b4b4dba87bd2deb833a8e2dfe699d1e9dd60675a71a496d0fa3e831c6f5c953",  # Replace with your actual API key
#         "num": 5  # Number of results to fetch
#     }
#     url = "https://serpapi.com/search"
#     response = requests.get(url, params=params)
#     if response.status_code == 200:
#         return response.json().get("organic_results", [])
#     else:
#         return f"Error: {response.status_code}, {response.text}"

# def research_steel_industry(company_name):
#     """
#     Perform market research on the steel industry and the company.
#     Expands search to gather more relevant insights into key offerings and strategic focus areas.
#     """
#     queries = [
#         f"{company_name} focus areas", 
#     ]
    
#     # Perform searches for each query
#     results = {query: search_with_serpapi(query) for query in queries}
    
#     # Store the results in a JSON file
#     with open(f"{company_name}_industry_research.json", "w") as f:
#         json.dump(results, f, indent=4)
    
#     return results

# # Example Usage
# company_name = "Tesla"  # Change to any company you want to research
# company_data = research_steel_industry(company_name)

# # Print the results from the search
# for query, result in company_data.items():
#     print(f"Query: {query}\nResult: {result}\n")

# print(f"Results saved to {company_name}_industry_research.json")

# import requests
# import json

# def search_with_serpapi(query):
#     """
#     Perform a web search using SerpAPI.
#     """
#     params = {
#         "q": query,
#         "api_key": "5b4b4dba87bd2deb833a8e2dfe699d1e9dd60675a71a496d0fa3e831c6f5c953",  # Replace with your actual API key
#         "num": 10  # Number of results to fetch
#     }
#     url = "https://serpapi.com/search"
#     response = requests.get(url, params=params)
#     if response.status_code == 200:
#         return response.json().get("organic_results", [])
#     else:
#         return {"error": f"Error: {response.status_code}, {response.text}"}

# def research_steel_industry(company_name):
#     """
#     Perform market research on the steel industry and the company.
#     """
#     queries = [
#         # f"{company_name} industry analysis",
#         # # f"focus areas in {company_name}",
#         # f"{company_name} AI adoption trends"
#     ]
    
#     # Perform searches for each query
#     results = {query: search_with_serpapi(query) for query in queries}
#     return results

# def save_responses_to_file(data, file_name="responses.json"):
#     """
#     Save the search results to a JSON file.
#     """
#     with open(file_name, "w") as file:
#         json.dump(data, file, indent=4)
#     print(f"Responses saved to {file_name}")

# # Example Usage
# company_name = "TCS"
# company_data = research_steel_industry(company_name)

# # Save responses to a file
# save_responses_to_file(company_data, f"{company_name}_responses.json")

# # Print confirmation
# print("All responses have been saved to the file.")


import requests
import json
def extract_snippets(data):
    """
    Extracts the 'snippet' field from the search results.

    Args:
        data (dict): The JSON response containing search results.

    Returns:
        dict: A dictionary with queries as keys and corresponding snippets as values.
    """
    snippets = {}
    for query, results in data.items():
        snippets[query] = [result.get("snippet", "No snippet available") for result in results]
    return snippets

def search_with_serpapi(query):
    """
    Perform a web search using SerpAPI.
    """
    params = {
        "q": query,
        "api_key": "5b4b4dba87bd2deb833a8e2dfe699d1e9dd60675a71a496d0fa3e831c6f5c953",  # Replace with your actual API key
        "num":2  # Number of results to fetch
    }
    url = "https://serpapi.com/search"
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("organic_results", [])
    else:
        return {"error": f"Error: {response.status_code}, {response.text}"}

def research_steel_industry(company_name):
    """
    Perform market research on the steel industry and the company.
    """
    queries = [
          f"{company_name} industry analysis",  # Overview of the industry
        f"{company_name} business model",  # Business model analysis
        f"{company_name} key offerings",  # Company product offerings
        f"{company_name} strategic focus areas",  # Strategic focus areas like operations, customer experience
        f"{company_name} AI adoption trends",  # AI and tech adoption in the company
        f"{company_name} market trends",  # Market trends in the specific industry (Automotive, Finance, etc.)
        f"{company_name} AI and automation adoption",  # Trends of AI and automation in the industry
        f"{company_name} supply chain strategy",  # Focus on supply chain
        f"{company_name} customer experience strategy",  # Focus on customer experience
        f"{company_name} vision and product innovations",  # Industry vision and innovations

    ]
    
    # Perform searches for each query
    results = {query: search_with_serpapi(query) for query in queries}
    return results

def save_snippets_to_file(snippets, file_name="snippets.json"):
    """
    Save the extracted snippets to a JSON file.

    Args:
        snippets (dict): A dictionary of extracted snippets.
        file_name (str): The name of the file to save the snippets.
    """
    with open(file_name, "w") as file:
        json.dump(snippets, file, indent=4)
    print(f"Snippets saved to {file_name}")


def save_responses_to_file(data, file_name="responses.json"):
    """
    Save the search results to a JSON file.
    """
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Responses saved to {file_name}")

# Example Usage
company_name = "infosys"
company_data = research_steel_industry(company_name)

snippets = extract_snippets(company_data)

save_snippets_to_file(snippets, f"{company_name}_snippets.json")

save_responses_to_file(company_data, f"{company_name}.json")

# Print confirmation
print("All responses have been saved to the file.")