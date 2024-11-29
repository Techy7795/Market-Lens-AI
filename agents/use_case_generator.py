# import openagi

# # Define a simple agent that can generate use cases based on the company and industry
# class UseCaseGenerationAgent(openagi.Agent):
#     def __init__(self, name, company_name, industry):
#         super().__init__(name)
#         self.company_name = company_name
#         self.industry = industry

#     def execute(self, *args, **kwargs):
#         prompt = f"""
#         Generate AI use cases for {self.company_name}, operating in the {self.industry} industry. Focus on:
#         1. Customer Experience.
#         2. Operational Efficiency.
#         3. Industry Trends.
#         """
#         # Simulate generating use cases based on the prompt (you can replace this with OpenAI or other APIs)
#         return f"Generated AI Use Cases for {self.company_name} in {self.industry}: \n" \
#                "1. Predictive maintenance for the vehicles.\n" \
#                "2. AI-powered customer service chatbots.\n" \
#                "3. Optimizing production and supply chain.\n" \
#                "4. Automated quality control using computer vision.\n" \
#                "5. Personalized driving assistance systems."

# # Initialize the agent with company and industry information
# agent = UseCaseGenerationAgent(name="Use Case Generator", company_name="Tesla", industry="Automotive")

# # Execute the agent's task
# result = agent.execute()

# print(result)

# import requests
# import json

# # Replace this with your actual GroQ API key
# API_KEY = "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"  # Get this from https://console.groq.com/keys

# def generate_use_cases_with_groq(snippets):
#     """
#     This function uses the GroQ API to generate AI/ML use cases based on the provided company data.
#     """
    
#     # Combine the snippets into a single string prompt
#     combined_snippets = ""
#     for key, values in snippets.items():
#         combined_snippets += f"{key}:\n" + "\n".join(values) + "\n\n"
    
#     # Prepare the payload for the GroQ API request
#     payload = {
#         "model": "groq-model-v1",  # Replace with the actual GroQ model name (check GroQ documentation)
#         "prompt": f"Based on the following company and industry information, generate relevant use cases for AI/ML technologies (Generative AI, LLMs, Machine Learning) that can improve processes, customer satisfaction, and operational efficiency.\n\nInformation:\n{combined_snippets}\n\nPlease generate 5 use cases.",
#         "max_tokens": 1024,  # Adjust as necessary
#         "temperature": 1,  # Adjust for creativity
#     }

#     # Define the API endpoint for GroQ
#     api_url = "https://api.groq.com/openai/v1/chat/completions"  # Replace with actual GroQ API URL
#     headers = {
#         "Authorization": f"Bearer {API_KEY}",  # Include your GroQ API key
#         "Content-Type": "application/json",
#     }

#     # Send the request to the GroQ API
#     response = requests.post(api_url, headers=headers, data=json.dumps(payload))
    
#     if response.status_code == 200:
#         return response.json().get("use_cases", [])
#     else:
#         return {"error": f"Error: {response.status_code}, {response.text}"}

# def save_use_cases_to_file(use_cases, file_name="generated_use_cases.json"):
#     """
#     Save the generated use cases to a JSON file.
#     """
#     with open(file_name, "w") as file:
#         json.dump({"use_cases": use_cases}, file, indent=4)
#     print(f"Use cases saved to {file_name}")

# # Example Usage
# snippets = {
#     "infosys industry analysis": ["The IT services industry is highly competitive...", "Infosys focuses on innovation...", "Infosys' market capitalization is 6.2 trillion INR."],
#     "infosys business model": ["Infosys provides IT services, consulting, outsourcing..."],
#     "infosys AI adoption trends": ["Generative AI spending is growing in 2024...", "AI adoption is predicted to increase by 15% productivity..."],
#     "infosys supply chain strategy": ["Infosys accelerates transformation with custom models for supply chain..."]
# }

# # Generate use cases with GroQ
# use_cases = generate_use_cases_with_groq(snippets)

# # Save the generated use cases to a file
# save_use_cases_to_file(use_cases, "generated_use_cases.json")  # Save to file

# # Print out the results for review
# print(f"Generated Use Cases: \n{use_cases}")


# import requests
# import json

# # Replace this with your actual GroQ API key
# API_KEY = "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"  # Get this from https://console.groq.com/keys

# def generate_use_cases_with_groq(snippets):
#     """
#     This function uses the GroQ API to generate AI/ML use cases based on the provided company data.
#     """
    
#     # Combine the snippets into a single string message
#     combined_snippets = ""
#     for key, values in snippets.items():
#         combined_snippets += f"{key}:\n" + "\n".join(values) + "\n\n"
    
#     # Prepare the payload for the GroQ API request
#     payload = {
#         "model": "llama3-8b-8192",  # Specify the model you want to use
#         "messages": [
#             {
#                 "role": "user",
#                 "content": f"Based on the following company and industry information, generate relevant use cases for AI/ML technologies (Generative AI, LLMs, Machine Learning) that can improve processes, customer satisfaction, and operational efficiency:\n\n{combined_snippets}"
#             }
#         ],
#         "max_tokens": 1024,  # Adjust as necessary
#         "temperature": 1,  # Adjust for creativity
#     }

#     # Define the API endpoint for GroQ
#     api_url = "https://api.groq.com/openai/v1/chat/completions"  # Use the correct GroQ endpoint
#     headers = {
#         "Authorization": f"Bearer {API_KEY}",  # Include your GroQ API key
#         "Content-Type": "application/json",
#     }

#     # Send the request to the GroQ API
#     response = requests.post(api_url, headers=headers, data=json.dumps(payload))
    
#     if response.status_code == 200:
#         return response.json().get("choices", [])
#     else:
#         return {"error": f"Error: {response.status_code}, {response.text}"}

# def save_use_cases_to_file(use_cases, file_name="generated_use_cases.json"):
#     """
#     Save the generated use cases to a JSON file.
#     """
#     with open(file_name, "w") as file:
#         json.dump({"use_cases": use_cases}, file, indent=4)
#     print(f"Use cases saved to {file_name}")

# # Example Usage
# snippets = {
#     "infosys industry analysis": ["The IT services industry is highly competitive...", "Infosys focuses on innovation...", "Infosys' market capitalization is 6.2 trillion INR."],
#     "infosys business model": ["Infosys provides IT services, consulting, outsourcing..."],
#     "infosys AI adoption trends": ["Generative AI spending is growing in 2024...", "AI adoption is predicted to increase by 15% productivity..."],
#     "infosys supply chain strategy": ["Infosys accelerates transformation with custom models for supply chain..."]
# }

# # Generate use cases with GroQ
# use_cases = generate_use_cases_with_groq(snippets)

# # Save the generated use cases to a file
# save_use_cases_to_file(use_cases, "generated_use_cases.json")  # Save to file

# # Print out the results for review
# print(f"Generated Use Cases: \n{use_cases}")


# import requests
# import json

# # Replace this with your actual GroQ API key
# API_KEY = "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"  # Get this from https://console.groq.com/keys

# def generate_use_cases_with_groq(snippets):
#     """
#     This function uses the GroQ API to generate AI/ML use cases based on the provided company data.
#     It generates detailed use cases and their descriptions on where the company can leverage GenAI, LLMs, and ML technologies.
#     """
    
#     # Combine the snippets into a single string message
#     combined_snippets = ""
#     for key, values in snippets.items():
#         combined_snippets += f"{key}:\n" + "\n".join(values) + "\n\n"
    
#     # Prepare the payload for the GroQ API request
#     payload = {
#         "model": "llama3-8b-8192",  # Specify the model you want to use
#         "messages": [
#             {
#                 "role": "user",
#                 "content": f"Based on the following company and industry information, generate 5 actionable use cases where the company can leverage Generative AI (GenAI), Large Language Models (LLMs), and Machine Learning (ML) technologies to improve their processes, enhance customer satisfaction, and boost operational efficiency. For each use case, provide a title and a detailed description of how the technology would be applied:\n\n{combined_snippets}"
#             }
#         ],
#         "max_tokens": 1024,  # Adjust as necessary
#         "temperature": 1,  # Adjust for creativity
#     }

#     # Define the API endpoint for GroQ
#     api_url = "https://api.groq.com/openai/v1/chat/completions"  # Use the correct GroQ endpoint
#     headers = {
#         "Authorization": f"Bearer {API_KEY}",  # Include your GroQ API key
#         "Content-Type": "application/json",
#     }

#     # Send the request to the GroQ API
#     response = requests.post(api_url, headers=headers, data=json.dumps(payload))
    
#     if response.status_code == 200:
#         return response.json().get("choices", [])
#     else:
#         return {"error": f"Error: {response.status_code}, {response.text}"}

# def save_use_cases_to_file(use_cases, file_name="generated_use_cases.json"):
#     """
#     Save the generated use cases to a JSON file.
#     """
#     with open(file_name, "w") as file:
#         json.dump({"use_cases": use_cases}, file, indent=4)
#     print(f"Use cases saved to {file_name}")

# # Function to accept dynamic snippets and generate use cases
# def generate_and_save_use_cases(snippets):
#     """
#     Generate use cases dynamically from the provided snippets and save them to a file.
#     """
#     # Generate use cases with GroQ
#     use_cases = generate_use_cases_with_groq(snippets)
    
#     # Save the generated use cases to a file
#     save_use_cases_to_file(use_cases, "generated_use_cases.json")  # Save to file

#     # Print out the results for review
#     print(f"Generated Use Cases: \n{use_cases}")



# import requests
# import json

# # Replace this with your actual GroQ API key
# API_KEY = "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"  # Get this from https://console.groq.com/keys

# def generate_use_cases_with_groq(snippets):
#     """
#     This function uses the GroQ API to generate AI/ML use cases based on the provided company data.
#     It generates detailed use cases and their descriptions on where the company can leverage GenAI, LLMs, and ML technologies.
#     """
    
#     # Combine the snippets into a single string message
#     combined_snippets = ""
#     for key, values in snippets.items():
#         combined_snippets += f"{key}:\n" + "\n".join(values) + "\n\n"
    
#     # Prepare the payload for the GroQ API request
#     payload = {
#         "model": "llama3-8b-8192",  # Specify the model you want to use
#         "messages": [
#             {
#                 "role": "user",
#                 "content": f"Based on the following company and industry information, generate 5 actionable use cases where the company can leverage Generative AI (GenAI), Large Language Models (LLMs), and Machine Learning (ML) technologies to improve their processes, enhance customer satisfaction, and boost operational efficiency. For each use case, provide a title and a detailed description of how the technology would be applied:\n\n{combined_snippets}"
#             }
#         ],
#         "max_tokens": 1024,  # Adjust as necessary
#         "temperature": 1,  # Adjust for creativity
#     }

#     # Define the API endpoint for GroQ
#     api_url = "https://api.groq.com/openai/v1/chat/completions"  # Use the correct GroQ endpoint
#     headers = {
#         "Authorization": f"Bearer {API_KEY}",  # Include your GroQ API key
#         "Content-Type": "application/json",
#     }

#     # Send the request to the GroQ API
#     response = requests.post(api_url, headers=headers, data=json.dumps(payload))
    
#     if response.status_code == 200:
#         return response.json().get("choices", [])
#     else:
#         return {"error": f"Error: {response.status_code}, {response.text}"}

# def save_use_cases_to_file(use_cases, file_name="generated_use_cases.json"):
#     """
#     Save the generated use cases to a JSON file.
#     """
#     with open(file_name, "w") as file:
#         json.dump({"use_cases": use_cases}, file, indent=4)
#     print(f"Use cases saved to {file_name}")

# def load_snippets_from_file(file_path):
#     """
#     Load snippets from the specified JSON file.
#     """
#     with open(file_path, "r") as file:
#         return json.load(file)

# # Function to accept dynamic snippets from JSON file and generate use cases
# def generate_and_save_use_cases(file_path):
#     """
#     Generate use cases dynamically from the provided JSON file and save them to a file.
#     """
#     # Load snippets from the JSON file
#     snippets = load_snippets_from_file(file_path)
    
#     # Generate use cases with GroQ
#     use_cases = generate_use_cases_with_groq(snippets)
    
#     # Save the generated use cases to a file
#     save_use_cases_to_file(use_cases, "generated_use_cases.json")  # Save to file

#     # Print out the results for review
#     print(f"Generated Use Cases: \n{use_cases}")

# # Example Usage: Path to your snippets JSON file
# file_path = r"C:\\Users\\user\\Desktop\\internship Project\\agents\\infosys_snippets.json"

# # Generate and save use cases dynamically
# generate_and_save_use_cases(file_path)


# import requests
# import json
# import re
# # from dotenv import load_dotenv
# # import os

# # load_dotenv()

# API_KEY = "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"
# # Get this from https://console.groq.com/keys

# def generate_use_cases_with_groq(snippets):
#     """
#     This function uses the GroQ API to generate AI/ML use cases based on the provided company data.
#     """
    
#     # Combine the snippets into a single string message
#     combined_snippets = ""
#     for key, values in snippets.items():
#         combined_snippets += f"{key}:\n" + "\n".join(values) + "\n\n"
    
#     # Prepare the payload for the GroQ API request
#     payload = {
#         "model": "llama3-8b-8192",  # Specify the model you want to use
#         "messages": [
#             {
#                 "role": "user",
#                 "content": f"Based on the following company and industry information, generate relevant use cases for AI/ML technologies (Generative AI, LLMs, Machine Learning) that can improve processes, customer satisfaction, and operational efficiency:\n\n{combined_snippets}"
#             }
#         ],
#         "max_tokens": 1024,  # Adjust as necessary
#         "temperature": 1,  # Adjust for creativity
#     }

#     # Define the API endpoint for GroQ
#     api_url = "https://api.groq.com/openai/v1/chat/completions"  # Use the correct GroQ endpoint
#     headers = {
#         "Authorization": f"Bearer {API_KEY}",  # Include your GroQ API key
#         "Content-Type": "application/json",
#     }

#     # Send the request to the GroQ API
#     response = requests.post(api_url, headers=headers, data=json.dumps(payload))
    
#     if response.status_code == 200:
#         return response.json().get("choices", [])
#     else:
#         return {"error": f"Error: {response.status_code}, {response.text}"}

# def extract_use_cases(response_content):
#     """
#     Extracts individual use cases from the response content, ensuring formatting is correct.
#     """
#     # Remove all sections that look like "XX. Use Case Title"
#     cleaned_content = re.sub(r"\\[^:]+ Use Cases\\:", "", response_content)  # Remove the Use Cases titles

#     # Remove extra newlines between use cases
#     cleaned_content = cleaned_content.replace("\n\n", "\n")
    
#     if '\n**' in cleaned_content:
#         # Remove everything after '\n' and add a period at the end
#         print(cleaned_content)
#         cleaned_content = cleaned_content.split('\n')[0] + '.'
#     # Use regular expressions to find all numbered use cases (e.g., 1., 2., 3., ...)
#     use_cases = re.findall(r"\d+\.\s[\s\S]+?(?=\n\d+\.|\n$)", cleaned_content)
    
#     # Return the extracted use cases
#     return use_cases

# def save_use_cases_to_json(use_cases, file_name="generated_use_cases.json"):
#     """
#     Save the generated use cases to a JSON file.
#     """
#     use_cases_data = {"use_cases": use_cases}
#     with open(file_name, "w") as json_file:
#         json.dump(use_cases_data, json_file, indent=4)
#     print(f"Use cases saved to {file_name}")

# # Example Usage
# snippets = {
#     "infosys industry analysis": ["The IT services industry is highly competitive...", "Infosys focuses on innovation...", "Infosys' market capitalization is 6.2 trillion INR."],
#     "infosys business model": ["Infosys provides IT services, consulting, outsourcing..."],
#     "infosys AI adoption trends": ["Generative AI spending is growing in 2024...", "AI adoption is predicted to increase by 15% productivity..."],
#     "infosys supply chain strategy": ["Infosys accelerates transformation with custom models for supply chain..."]
# }

# # Generate use cases with GroQ
# use_cases_response = generate_use_cases_with_groq(snippets)

# # Extract the use cases from the response content
# if "error" not in use_cases_response:
#     response_content = use_cases_response[0]['message']['content']
#     use_cases = extract_use_cases(response_content)

#     # Save the extracted use cases to a JSON file
#     save_use_cases_to_json(use_cases, "generated_use_cases.json")  # Save to JSON file
# else:
#     print(use_cases_response["error"])


import requests
import json
import re

# Replace this with your actual GroQ API key
API_KEY = "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"  # Get this from https://console.groq.com/keys

def generate_use_cases_with_groq(snippets):
    """
    This function uses the GroQ API to generate AI/ML use cases based on the provided company data.
    """
    
    # Combine the snippets into a single string message
    combined_snippets = ""
    for key, values in snippets.items():
        combined_snippets += f"{key}:\n" + "\n".join(values) + "\n\n"
    
    # Prepare the payload for the GroQ API request
    payload = {
        "model": "llama3-8b-8192",  # Specify the model you want to use
        "messages": [
            {
                "role": "user",
                "content": f"Based on the following company and industry information, generate relevant use cases for AI/ML technologies (Generative AI, LLMs, Machine Learning) that can improve processes, customer satisfaction, and operational efficiency:\n\n{combined_snippets}"
            }
        ],
        "max_tokens": 1024,  # Adjust as necessary
        "temperature": 1,  # Adjust for creativity
    }

    # Define the API endpoint for GroQ
    api_url = "https://api.groq.com/openai/v1/chat/completions"  # Use the correct GroQ endpoint
    headers = {
        "Authorization": f"Bearer {API_KEY}",  # Include your GroQ API key
        "Content-Type": "application/json",
    }

    # Send the request to the GroQ API
    response = requests.post(api_url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        return response.json().get("choices", [])
    else:
        return {"error": f"Error: {response.status_code}, {response.text}"}

def extract_use_cases(response_content):
    """
    Extracts individual use cases from the response content, ensuring formatting is correct.
    """
    # Remove all sections that look like "XX. Use Case Title"
    cleaned_content = re.sub(r"\\[^:]+ Use Cases\\:", "", response_content)  # Remove the Use Cases titles

    # Remove extra newlines between use cases
    cleaned_content = cleaned_content.replace("\n\n", "\n")
    
    # if "\n*" in cleaned_content:
    #     # Remove everything after '\n' and add a period at the end
    #     cleaned_content = cleaned_content.split('\n')[0] + '.'
    # Use regular expressions to find all numbered use cases (e.g., 1., 2., 3., ...)
    use_cases = re.findall(r"\d+\.\s[\s\S]+?(?=\n\d+\.|\n$)", cleaned_content)
    
    # Return the extracted use cases
    return use_cases

def save_use_cases_to_json(use_cases, file_name="generated_use_cases.json"):
    """
    Save the generated use cases to a JSON file.
    """
    use_cases_data = {"use_cases": use_cases}
    with open(file_name, "w+") as json_file:
        json.dump(use_cases_data, json_file, indent=4)
    print(f"Use cases saved to {file_name}")

# Example Usage
snippets = {
    "infosys industry analysis": ["The IT services industry is highly competitive...", "Infosys focuses on innovation...", "Infosys' market capitalization is 6.2 trillion INR."],
    "infosys business model": ["Infosys provides IT services, consulting, outsourcing..."],
    "infosys AI adoption trends": ["Generative AI spending is growing in 2024...", "AI adoption is predicted to increase by 15% productivity..."],
    "infosys supply chain strategy": ["Infosys accelerates transformation with custom models for supply chain..."]
}

# Generate use cases with GroQ
use_cases_response = generate_use_cases_with_groq(snippets)

# Extract the use cases from the response content
if "error" not in use_cases_response:
    response_content = use_cases_response[0]['message']['content']
    use_cases = extract_use_cases(response_content)

    # Save the extracted use cases to a JSON file
    save_use_cases_to_json(use_cases, "generated_use_cases.json")  # Save to JSON file
else:
    print(use_cases_response["error"])