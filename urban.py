import json
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.urbanhome.ch/search/rent/living/apartment/zh/winterthur')

container_number = 1
apartment_name_list = []
address_list = []
while True:
    try:
        apartment_name = browser.find_elements_by_css_selector('#grid > li:nth-child('+str(container_number)+') > div.a.ax > h2.fl.pr.s73.pt5 > a')[0].text
        apartment_name_list.append(apartment_name)
        address = browser.find_elements_by_css_selector('#grid > li:nth-child('+str(container_number)+') > div.a.ax > div:nth-child(3) > div.a.ay')[0].text.replace('\n','|')
        address_list.append(address)
        container_number += 1
    except:
        break

print(apartment_name_list)
print(address_list)

browser.close()
