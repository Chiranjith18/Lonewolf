import requests
from datetime import datetime

url = "https://lonewolfsafebite.streamlit.app/"

try:
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        # save HTML to file with timestamp
        filename = f"scrape_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Scraped successfully: {filename}")
    else:
        print(f"Failed to scrape. Status code: {response.status_code}")
except Exception as e:
    print(f"Error: {e}")
