import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def crawl_website(output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        # Prompt user to input the URL of the website
        website_url = input("Enter the URL of the website to scrape: ")
        
        # Parse the URL to extract the hostname
        parsed_url = urlparse(website_url)
        hostname = parsed_url.hostname
        
        # Send GET request to the website
        response = requests.get(website_url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all <p> tags containing text content
        paragraphs = soup.find_all('p')
        
        # Create a text file for each paragraph and store the text content
        for i, paragraph in enumerate(paragraphs):
            with open(os.path.join(output_dir, f"paragraph_{i+1}.txt"), 'w', encoding='utf-8') as file:
                file.write(paragraph.get_text())
        
        print("Scraping completed successfully.")
    except requests.RequestException as e:
        print(f"Failed to fetch website content: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Specify the output directory to store text files
    output_directory = "website_corpus"
    
    # Crawl the website and store text data as a corpus of text files
    crawl_website(output_directory)
