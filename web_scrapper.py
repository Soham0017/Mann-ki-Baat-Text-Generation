import requests
from bs4 import BeautifulSoup

with open("mann_ki_baat_urls.txt", "r") as file:
    urls = [line.strip() for line in file.readlines()]

# extract the content of a Mann Ki Baat episode
def extract_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract the content within the specified div
        content_div = soup.find("div", class_="news-bg")
        if content_div:
            return content_div.get_text(separator="\n", strip=True)
        else:
            print("content not found----")
            return 
    else:
        print(f"Failed to retrieve content, status code: {response.status_code} --{url}")
        return 

# Open a file to save the content
with open("mann_ki_baat_content.txt", "w", encoding="utf-8") as file:
    for url in urls:
        content = extract_content(url)
        if content:
            file.write(content + "\n")

print("Content has been saved to mann_ki_baat_content.txt")
