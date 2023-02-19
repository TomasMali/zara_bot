# from audioop import lin2ulaw
import requests
from bs4 import BeautifulSoup



#https://www.zara.com/it/it/uomo-prezzi-speciali-l806.htm




#webdriver = webdriver.Chrome()


# options = Options()
# options.add_argument('--headless=new')
# options.add_argument('--disable-gpu')  # Last I checked this was necessary.
# webdriver = webdriver.Chrome()

def getLinks(link="https://www.zara.com/it/it/woman-sale-l5503.html"):
    from selenium import webdriver
    import time

    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By

    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    webdriver = webdriver.Chrome(chrome_options=options)

    links_list = []

    webdriver.get(link)
    time.sleep(2)

    elem = webdriver.find_element(By.ID, "onetrust-accept-btn-handler")
    elem.send_keys(Keys.ENTER)        
   # webdriver.find_element(By.CLASS_NAME, "zds-button").send_keys(Keys.ENTER)

    #  id="onetrust-accept-btn-handler"

    for page_nr in range(6):

        webdriver.get(link + "?page=" + str(page_nr+1))


        #webdriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        soup = BeautifulSoup(webdriver.page_source,"lxml")
        print("###################")
        # print(soup)

        if not soup:
            break

        ul_list = soup.find_all("ul", class_="product-grid__product-list")
        for ul in ul_list:
            li_list = ul.find_all("li", class_="product-grid-block-dynamic")

            for i in li_list:
                items = i.find_all("div", class_="product-grid-product-info__product-header")
                #  product-grid-product-info__product-header
                for item in items:
                    price = item.find_all("span", class_="price-current__amount")
                    price_formated = float(str((price[0].text)[:4]).replace(",","."))
                    # print(price_formated)
                    all_a = item.find_all('a', href=True)
                    for a in all_a:
                        links_list.append((a['href'], price_formated))

        print(str(page_nr) ,len(links_list))
    webdriver.close()
    return links_list

#getLinks()
#print(getLinks()[0][1])



