import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = webdriver.ChromeService(ChromeDriverManager().install())

driver= webdriver.Chrome(service=service)
categories = ['https://www.dhakatribune.com/bangladesh/politics', 'https://www.dhakatribune.com/bangladesh/crime', 'https://www.dhakatribune.com/bangladesh/education', 'https://www.dhakatribune.com/business/economy','https://www.dhakatribune.com/business/banks', 'https://www.dhakatribune.com/business/commerce','https://www.dhakatribune.com/business/stock','https://www.dhakatribune.com/business/real-estate','https://www.dhakatribune.com/sport/cricket','https://www.dhakatribune.com/sport/football','https://www.dhakatribune.com/sport/tennis','https://www.dhakatribune.com/sport/other-sports' ,'https://www.dhakatribune.com/world/asia', 'https://www.dhakatribune.com/world/south-asia','https://www.dhakatribune.com/world/africa','https://www.dhakatribune.com/world/middle-east','https://www.dhakatribune.com/world/europe','https://www.dhakatribune.com/world/north-america']


# make a loop to click load button 10 times

def get_links(url):
    driver.get(url)
    for i in range(120):
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.find_element(By.XPATH, "(//button[normalize-space()='More'])[1]").click()
        except:
            continue
        time.sleep(1)
    links = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "link_overlay")))
    return links

def main():
    for category in categories:
        links = get_links(category)
        with open('data.csv', 'a', encoding='utf-8') as f:
            for link in links:
                # write like this link, category. split the category using '/' and take the last element
                f.write(link.get_attribute('href') + ',' + category.split('/')[-1] + '\n')



if __name__ == '__main__':
    main()
