from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time
import re
import string

class Download_PDF:
    def __init__(self,save_path,company_name,spec):
        # print(driver.title)
        # html = driver.page_source
        self.save_path = save_path
        self.company_name = company_name
        self.spec = spec

    def download_PDF(self,download_list):
        print("---Download started---")
        def url_download(self):
            try:
                if pdf_url[-3:] == 'pdf':
                    response = requests.get(pdf_url)
                    # 確認響應狀態碼為 200 (成功)
                    if response.status_code == 200:
                        # 指定下載的檔案名稱
                        filename = self.save_path+saved_name+".pdf"
                        # print(f"filename{filename}")
                        
                        #防止SSL限制Max retries exceeded
                        time.sleep(0.5)
                        
                        # 使用二進制模式寫入檔案
                        with open(filename, "wb") as file:
                            file.write(response.content)

                        print(f'PDF 下載完成，存至{filename}')
                    else:
                        print("無法下載 PDF")
                # else:
                #     print("Link isn't PDF")
            except:
                print("連線問題")

        for saved_name, pdf_url in download_list:
            # print("old_saved_name: ",saved_name)
            #PDF檔案名稱限制
            valid_chars = '-_.() %s%s' % (re.escape(string.ascii_letters), re.escape(string.digits))
            saved_name = re.sub(r'[^%s]' % valid_chars, '', saved_name) #saved_name.replace("/","_").replace(":","_").replace("|","_").replace("<","_").replace(">","_").replace("*","_").replace("'","_").replace('"',"_").replace("?","_")
            if len(saved_name)>50 :saved_name = saved_name[:50]
            print("new_saved_name: ",saved_name)
            url_download(self)
        print("\n---Download finished---")

    def search_SKU(self):

        # 設定 Chrome 瀏覽器選項
        options = Options()
        options.add_argument('--headless')  # 設定為無頭模式

        driver = webdriver.Chrome('chromedriver', options=options)
        # driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(30)
        driver.get('https://www.google.com/')
        url_list = []
        try:
            search = driver.find_element(By.NAME, 'q')
            key = "filetype:pdf "+self.company_name+" "+self.spec
            
            # print("search key: ",key)
            search.send_keys(key)
            search.send_keys(Keys.ENTER)

            items = driver.find_elements(By.CLASS_NAME, "LC20lb")
            addrs = driver.find_elements(By.CLASS_NAME, "yuRUbf")

            all = zip(items, addrs)
            
            for item in all:
                addr = item[1].find_element(By.TAG_NAME, 'a').get_attribute('href')
                url_list.append([item[0].text, addr])
                # print(f'{item[0].text} - {addr}')
            return url_list
        
        except NoSuchElementException:
            print('無法定位')
        # except StaleElementReferenceException:
        #     print('無法定位')
        driver.quit()

if __name__ == '__main__':
    _path = "./PDF/"
    company = "Riken Keiki"
    _spec = "RK-7000 Series" # Motion Control MX2 Series ，GD-K88 Series
    download = Download_PDF(_path,company, _spec)
    url_list = download.search_SKU()
    # print(f"url_list: {url_list}")
    download.download_PDF(url_list)