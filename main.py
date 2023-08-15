import time
from selenium import webdriver
from bs4 import BeautifulSoup
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

file_path = r"C:\Users\Zed\Documents\Code\repos\letterboxd_scraper"

num = input("Enter Popular Films Page number: ")
# link = 'https://letterboxd.com/films/popular/page/'
# link = 'https://letterboxd.com/films/popular/genre/-animation/language/japanese/page/'

# link = 'https://letterboxd.com/jack/list/official-top-250-films-with-the-most-fans/page/'
# link = "https://letterboxd.com/darrencb/list/letterboxds-top-250-horror-films/page/"
link = 'https://letterboxd.com/bfi/list/sight-and-sounds-greatest-films-of-all-time/page/'

# link = "https://letterboxd.com/lifeasfiction/list/letterboxd-100-animation"

# url = link
url = link + num

driver = webdriver.Chrome()
driver.get(url)

# Perform scrolling
# UNCOMMENT if link is user list. COMMENT if link is official letterboxd list.
num_scrolls = 9  # Adjust this value based on your needs
for _ in range(num_scrolls):
    body = driver.find_element(By.TAG_NAME, "body")
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)  
print("Finished scrolling")

time.sleep(5)

page_source = driver.page_source

driver.quit()

# Parse the HTML content 
soup = BeautifulSoup(page_source, "html.parser")

# film_posters = soup.find_all(class_='film-poster')
film_posters = soup.find_all(class_="linked-film-poster")
# film_posters = soup.find_all(class_='react-component poster')

# Extract film titles and store them in a list
# film_titles = [poster['data-film-name'] for poster in film_posters]
film_titles = [poster.get("data-film-name") for poster in film_posters]

# Create txt file and write film titles
file_name = "movie_list_" + str(num) + ".txt"
file_full_path = os.path.join(file_path, file_name)
with open(file_full_path, "w") as file:
    for title in film_titles:
        file.write(str(title) + "\n")

print("Movie titles saved to " + file_name)
