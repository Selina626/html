"""
pip install selenium webdriver_manager
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

#%% 範例一: 模擬搜尋 (以台北資料開放網為例)
# 定義抓取一頁資料的函數
def extract_page_data():
    time.sleep(1)
    items = driver.find_elements(By.CLASS_NAME, "V9tjod") # Q?
    for item in items:
        title_element = item.find_element(By.CLASS_NAME, "zReHs") # Q?
        title = title_element.text
        data_list.append({"標題": title})
        print(title)


#%%
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    service=webdriver.chrome.service.Service(ChromeDriverManager().install()),
    options=options
)
# 啟動瀏覽器
driver.get("https://www.google.com/")
driver.maximize_window()

# 搜尋關鍵字
search_box = driver.find_element(By.ID, "APjFqb") # Q?
search_box.send_keys("車禍")
search_box.send_keys(Keys.ENTER)

#time.sleep(2)

# 存放所有資料的列表
data_list = []

# 迴圈抓多頁
count=0
while count<3:
    time.sleep(5)
    extract_page_data()
    try:
        next_button = driver.find_element(By.CLASS_NAME, "oeN89d") # Q?
        if next_button.is_enabled():
            next_button.click()
        else:
            break  # 已經是最後一頁
    except (NoSuchElementException, ElementNotInteractableException):
        break
    count +=1
    time.sleep(2)

driver.quit()


#%%
import pandas as pd
# 轉為 DataFrame 並輸出成 CSV
df = pd.DataFrame(data_list)
df.to_csv(r"data.csv", index=False, encoding="utf-8-sig")