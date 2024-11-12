import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

url = 'https://www.keno.com.au/check-results/'
driver.get(url)

# Initial delay to allow full page load
time.sleep(5)

scraped_data = []

try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//ul[@class='game-board-listing']"))
    )
    elements = driver.find_elements(By.XPATH, "//li[@data-id='game-board-container']")
    
    # Loop through each element and extract relevant data
    for element in elements:
        # Split the text by lines to get individual data points
        lines = element.text.splitlines()
        
        balls = lines[:20]  
        draw_number = lines[22]  
        heads_or_tails = lines[23]  
        bonus = lines[25]  # Assuming "REG" or similar is at index 24

        # Compile the row with 23 columns
        row = [draw_number] + balls + [bonus, heads_or_tails]

        scraped_data.append(row)

finally:
    driver.quit()

with open("scraped_data.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    # Write header row
    header = ["Draw Number"] + [f"Ball {i}" for i in range(1, 21)] + ["Bonus", "Heads or Tails"]
    writer.writerow(header)
    writer.writerows(scraped_data)

print("Data saved to scraped_data.csv")
