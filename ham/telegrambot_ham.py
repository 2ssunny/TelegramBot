from copyreg import dispatch_table
import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import configham

token = configham.token
id=configham.id

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("http://hitop.net/jbcgi/board/?code=board10")
# titles = driver.find_element(By.CSS_SELECTOR,"body > font > b > font > center > div > table > tbody > tr > td > table:nth-child(3) > tbody > tr:nth-child(13) > td:nth-child(3) > div > a")
# titles=driver.find_element_by_css_selector("body > font > b > font > center > div > table > tbody > tr > td > table:nth-child(3) > tbody > tr:nth-child(13) > td:nth-child(3) > div > a")

send_message_list=[]
while True:
    try:
        for i in range(13,20):
            if i%2!=0:
                titles = driver.find_element(By.CSS_SELECTOR,f"body > font > b > font > center > div > table > tbody > tr > td > table:nth-child(3) > tbody > tr:nth-child({i}) > td:nth-child(3) > div")
                urls = driver.find_element(By.CSS_SELECTOR,f"body > font > b > font > center > div > table > tbody > tr > td > table:nth-child(3) > tbody > tr:nth-child({i}) > td:nth-child(3) > div")
                # print(titles.text)
                message=""
                if "706" in range(titles):
                    message=titles[i].text+"\n"+urls[i].get_arrtiubute("href")
                    if message not in send_message_list:
                        print(message)
                        send_message_list.append(message)
                        bot = telegram.Bot(token)
                        bot.sendMessage(chat_id=id, text=message)
        time.sleep(60.0*1)
    except KeyboardInterrupt:
        break

# for i in range(1,30):
#     print(str(i)+"번째 페이지 검색중")
#     for a in range(1,7):
#         try :
#             bank = driver.find_element(By.CSS_SELECTOR,f"#main_pack > section.sc_new.cs_common_module.case_list.color_1._cs_interest_rate > div.cm_content_wrap > div > div > div._list._panel_wrapper > div:nth-child({i}) > div > div > div:nth-child({a}) > div > div > div.info > dl > dd:nth-child(2) > span")
#         except :
#             TOF=True 
#             break 
#         bank_list.append(bank.text)

#         name = driver.find_element(By.CSS_SELECTOR,f"#main_pack > section.sc_new.cs_common_module.case_list.color_1._cs_interest_rate > div.cm_content_wrap > div > div > div._list._panel_wrapper > div:nth-child({i}) > div > div > div:nth-child({a}) > div > div > div.title > div > strong > a")
#         name_list.append(name.text)

#         url = name.get_attribute('href')
#         url_list.append(url)

#         inter_basic = driver.find_element(By.CSS_SELECTOR,f"#main_pack > section.sc_new.cs_common_module.case_list.color_1._cs_interest_rate > div.cm_content_wrap > div > div > div._list._panel_wrapper > div:nth-child({i}) > div > div > div:nth-child({a}) > div > div > div.info > dl > dd:nth-child(4) > span > strong")
#         basic_list.append(inter_basic.text)

#         inter_max = driver.find_element(By.CSS_SELECTOR,f"#main_pack > section.sc_new.cs_common_module.case_list.color_1._cs_interest_rate > div.cm_content_wrap > div > div > div._list._panel_wrapper > div:nth-child({i}) > div > div > div:nth-child({a}) > div > div > div.interest_info > span > em")
#         max_list.append(inter_max.text+"%")


# driver.implicitly_wait(3)
# while True:
#     try:
#         driver.get(url_hitop)




# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# import pyshorteners as ps
# import pickle
# import os

# crawling=open("crawling.txt", "w")

# bank_list=[]
# name_list=[]
# basic_list=[]
# max_list=[]
# url_list=[]

# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# driver = webdriver.Chrome("./chromedriver")
# driver.implicitly_wait(10)
# driver.get("https://url.kr/kqj1wt")

# b = 0

# TOF=False

# for i in range(1,30):
#     print(str(i)+"번째 페이지 검색중")
#     for a in range(1,7):
#         try :
#             bank = driver.find_element(By.CSS_SELECTOR,f"#main_pack > section.sc_new.cs_common_module.case_list.color_1._cs_interest_rate > div.cm_content_wrap > div > div > div._list._panel_wrapper > div:nth-child({i}) > div > div > div:nth-child({a}) > div > div > div.info > dl > dd:nth-child(2) > span")
#         except :
#             TOF=True 
#             break 
#         bank_list.append(bank.text)

#         name = driver.find_element(By.CSS_SELECTOR,f"#main_pack > section.sc_new.cs_common_module.case_list.color_1._cs_interest_rate > div.cm_content_wrap > div > div > div._list._panel_wrapper > div:nth-child({i}) > div > div > div:nth-child({a}) > div > div > div.title > div > strong > a")
#         name_list.append(name.text)

#         url = name.get_attribute('href')
#         url_list.append(url)

#         inter_basic = driver.find_element(By.CSS_SELECTOR,f"#main_pack > section.sc_new.cs_common_module.case_list.color_1._cs_interest_rate > div.cm_content_wrap > div > div > div._list._panel_wrapper > div:nth-child({i}) > div > div > div:nth-child({a}) > div > div > div.info > dl > dd:nth-child(4) > span > strong")
#         basic_list.append(inter_basic.text)

#         inter_max = driver.find_element(By.CSS_SELECTOR,f"#main_pack > section.sc_new.cs_common_module.case_list.color_1._cs_interest_rate > div.cm_content_wrap > div > div > div._list._panel_wrapper > div:nth-child({i}) > div > div > div:nth-child({a}) > div > div > div.interest_info > span > em")
#         max_list.append(inter_max.text+"%")



#         crawling.write(str()+str(b*6 + a)+"번째 상품"+"\n")
#         crawling.write(str()+"은행명: "+bank_list[b*6 + a-1]+"\n")
#         crawling.write(str()+"상품명: "+name_list[b*6 + a-1]+"\n")
#         crawling.write(str()+"기본 금리: "+basic_list[b*6 + a-1]+"\n")
#         crawling.write(str()+"최고 금리: "+max_list[b*6 + a-1]+"\n")
#         crawling.write(str()+"상품 링크: "+url_list[b*6 + a-1]+"\n")
#         crawling.write(str()+"----------------------"+"\n")
#     if TOF :
#         break
#     driver.find_element(By.CSS_SELECTOR,f"#main_pack > section.sc_new.cs_common_module.case_list.color_1._cs_interest_rate > div.cm_content_wrap > div > div > div.cm_paging_area.no_margin._list > div > a.pg_next.on").click()
#     time.sleep(3)
#     b+=1
    

# with open("name_list.pkl","wb") as n:
#     pickle.dump(name_list, n)
# with open("bank_list.pkl","wb") as b:
#     pickle.dump(bank_list, b)
# with open("basic_list.pkl","wb") as bi:
#     pickle.dump(basic_list, bi)
# with open("max_list.pkl","wb") as mi:
#     pickle.dump(max_list, mi)

# print("크롤링 완료\n")
# print("수집된 정보는 crawling.txt에서 확인 하세요")
# print("수집된 정보를 사용해 계산하려면 crawling_deposit_py.py를 실행하세요.")
# time.sleep(5)
# crawling.close()
# os.system("pause")