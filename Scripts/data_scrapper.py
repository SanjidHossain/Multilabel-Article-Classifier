import pandas as pd
import requests
from bs4 import BeautifulSoup

def scraper_code_with_no_headers():
    # Load the CSV file into a DataFrame without headers
    df = pd.read_csv('data.csv', header=None)
    
    # Rename columns
    df.columns = ["URL", "Category"]

    # Revised function to extract content from the URL using CSS selectors
    def revised_extract_content(url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'lxml')

            # Extract title using CSS selector
            title = soup.select_one('.title.mb10')
            title = title.text.strip() if title else None

            # Extract body using CSS selector
            body = soup.select_one('article.jw_detail_content_holder.jw_detail_content_body.content.mb16')
            body = body.text.strip() if body else None

            return title, body

        except Exception as e:
            print(f"Error fetching data for URL {url}: {e}")
            return None, None

    # Apply the revised function to the DataFrame
    df['Title'], df['Body'] = zip(*df['URL'].apply(revised_extract_content))

    # Save the data into category-specific CSV files
    for category, group_df in df.groupby('Category'):
        group_df.drop('Category', axis=1).to_csv(f"{category}.csv", index=False)

    return "Scraping and saving completed without headers."

# Run the scraper function
def check_files():
    try:
        with open('data.csv', 'r', encoding='utf-8') as f:
            with open('data_bak.csv', 'w', encoding='utf-8') as f1:
                for line in f:
                    f1.write(line)
            f1.close()
        f.close()
        print('your file has been backed up to data_bak.csv')
    except:
        f = open('data.csv', 'w')
        with open('data.csv', 'a', encoding='utf-8') as f:
            f.write('URL,Category\n')
        f.close()

check_files()
scraper_code_with_no_headers()
