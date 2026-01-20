from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup
driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org")

# Search
search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("Python (programming language)")
search_box.send_keys(Keys.RETURN)

time.sleep(3) 

# Scrape and save
try:
    article_title = driver.find_element(By.ID, "firstHeading")
    text_content = article_title.text
    print(f"--- SUCCESS: The Title is: '{text_content}' ---")

    with open("wiki_data.txt", "w") as file:
        file.write(f"Title: {text_content}\n")
        file.write("Scrapped by manual bot")
        print("Success! File saved")

except Exception as e:
    print("\n!!!!! ERROR !!!!!")
    print(f"I could not find the element. Here is why: {e}")

driver.quit()