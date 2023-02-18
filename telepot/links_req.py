# from audioop import lin2ulaw
import requests
from bs4 import BeautifulSoup


from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options





#webdriver = webdriver.Chrome()


options = Options()
options.add_argument('--headless=new')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
webdriver = webdriver.Chrome( chrome_options=options)

def getLinks():

    cookies = {
        'bm_sz': 'F5AAA1262668072258F44D347A595209~YAAQtDYWAiIamS+GAQAAIZkZZBJYFsINWg6ASOa/RK5L09yIi8qVKei1YNqdLTaJYBxe4SqcL6VOOtNSsyZ4xyD2LaQZ7TXRrIESjK3S/aPltnEvCgMVv528d//RmQApg0zgWlEY8QxxXctrahQCPxSaJtndMykYXzbcqIGHLrTTc5dDJNXQ9k+k+6NTXlrs1b0YobLNjRFtoWjDJCtfWdhsnGiHVIm5v7r4zcIr4Hz78Q9vMU//To537brxl8hni69nw+LHEVeB1c1u735mj8DvM6LZI4sVr0YgoO7SuIeQ~3290418~3421489',
        '_abck': 'CB824F1E384B196607D17E23FCD71E36~0~YAAQtDYWAi4amS+GAQAAEJ4ZZAlQOaVxksJ3sCtYMO0bVEzu2dGoYWOlzo2O9SE0yqrjQur7NFQsU1LTRjplIPLlBMaksNTc8L6SV6eEDIhBFBBzZx1llR3vCZEhNKpZYUsN2rV7x9PQQw8p1OlFbcsNV/PackURXEWIpg34r5U4gKuh+JAtZW72uuWbl513ZWrNFZkMwHk4sQYtDAr5WN6b5eYtzb8d+iVSFgJ4OZzCEFQY9UmpQMpkaea+UEOQvCHr2PEeyyUeA249+QICOpZ4xswQOuYSL0bS3FrjB7dHbxyXWNste5+n/FU1bFOdcsbbIpLJrlan2s9smJq5dliiKUyIke+osgdQfC+DRc9k9QGddBui24lQBdUOpks0KTw9dgy9076FjdVjjJoT5qxxfHuuzg==~-1~-1~-1',
        'rid': 'fe3046c4-d35c-4ed1-b83a-d23baa7c5d52',
        'cart-was-updated-in-standard': 'true',
        'ITXSESSIONID': '0dcea3afce672cd936c9255cd09ffcd3',
        'OptanonAlertBoxClosed': '2023-02-18T10:37:38.302Z',
        'selectedRegion': 'it',
        'bm_mi': 'ABDFF901EA7CDBEB3971A49B5C9AB542~YAAQVzYWAnzAECiGAQAAcNMwZBJX8aVXyE0SBKrBH6pMJvrc/N3r2gQbM6MP9NO0CGM0PZ+r3XIsSsu2aP7aSI3eH/mAsNtPXLN6caO2rtzqTAxykKF6jhcaMsj7hF3LKE0BJW6vuXPkAMalHu0m6Exj0OCdd149JNzge0tc9F2dsmeG+z8jcbJ643/zF6jXIk9/mhXixR8WsuGuuw5BHhAQt3W2RDZLEPtDj4soQTyZgNu/I6StMJOve3rKanwP2M/T7S8pUZHs2BL9klpGtwhknOENyRZPGKKpLUNOSKOKpxTrpfWn+vmrro7Jz0wHJM1pSgRvj7bVfaV5HfOJFwhIGKT3I0E=~1',
        'bm_sv': '959CEC0E6239254F242F39A3A4237331~YAAQVzYWApDAECiGAQAA0dkwZBIQ3H/8ywd0MxKBUEwKP5HbdRtgoE1czYQWiQsPtAYacfzg+WkIPxMNtyskCVRoD6W7rH6fghzSzaLU+P+hIfbNaZsfziekEEmSS22pxtqwRTBFAHXXyPgHGb1xkmuLOTCul0qnTd3Aw6JjTC43fA4ysE6k4XdOjgeDD5SjndehvJXSBPnOUwQdG8uj5tCWdKSK7d28d9iSEQaHaqE6qteBcfDTKwzjpeHhzig=~1',
        'ak_bmsc': '09561AF7817160437542725ACDD857E9~000000000000000000000000000000~YAAQVzYWAr3AECiGAQAARRwxZBK6Mv8JM+WUIaDOkdgV0StlYBHA6eSqNvmhZBY1q9YrCcZj9eyxqJ3PpamVHiqC1qVk1OUIPxhDCIaOq/NvBkIoI/erY5prxZyXraoq/bTP+1MulZ5tAZcKX2Nn/yzjQ5wVK43qxE+A8o4qY/u8aBd/8NG695NqqeVI6rwrnijcCk39quBYcqUZMFAWJeDFG6QrLmrIyYer+3S3vZFxJkUToVak/xPhT5FbmVmzS5suWLZsQGTHmk/vixdwKaKG5gvcJtXuPcMZaibq45l+q1kWm/VTXG3T7eqFAy324OJ82YS3saYKRrfBaLu/4Ie9Qz81xvyNMKVkZ4dA2XFp3SCowafIlaLCRg48kdYZD2bKGyb4lz8JbIsYFLrHLUjXFvUGmTCci0mLVJXOTU6zsf8rKsxeYGI7F/XDlP09kAJHVlB4LIqERigITHw4eAjSeqIUOkqqpxox8OqH+NP8DG05Zz6ZlG7n6qRYnTGGfDUqBtqw',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Sat+Feb+18+2023+12%3A31%3A03+GMT%2B0100+(Ora+standard+dell%E2%80%99Europa+centrale)&version=6.28.0&isIABGlobal=false&hosts=&consentId=295db455-ae01-4aaf-ba0b-fdd27c2ff01a&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=NL%3BNH&AwaitingReconsent=false',
        'storepath': 'it%2Fit',
        'IDROSTA': '7fabdd146b2f:1d840defea3942811c6faa5b2',
    }

    headers = {
        'authority': 'www.zara.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'it-IT,it;q=0.9,la;q=0.8',
        'cache-control': 'max-age=0',
        # 'cookie': 'bm_sz=F5AAA1262668072258F44D347A595209~YAAQtDYWAiIamS+GAQAAIZkZZBJYFsINWg6ASOa/RK5L09yIi8qVKei1YNqdLTaJYBxe4SqcL6VOOtNSsyZ4xyD2LaQZ7TXRrIESjK3S/aPltnEvCgMVv528d//RmQApg0zgWlEY8QxxXctrahQCPxSaJtndMykYXzbcqIGHLrTTc5dDJNXQ9k+k+6NTXlrs1b0YobLNjRFtoWjDJCtfWdhsnGiHVIm5v7r4zcIr4Hz78Q9vMU//To537brxl8hni69nw+LHEVeB1c1u735mj8DvM6LZI4sVr0YgoO7SuIeQ~3290418~3421489; _abck=CB824F1E384B196607D17E23FCD71E36~0~YAAQtDYWAi4amS+GAQAAEJ4ZZAlQOaVxksJ3sCtYMO0bVEzu2dGoYWOlzo2O9SE0yqrjQur7NFQsU1LTRjplIPLlBMaksNTc8L6SV6eEDIhBFBBzZx1llR3vCZEhNKpZYUsN2rV7x9PQQw8p1OlFbcsNV/PackURXEWIpg34r5U4gKuh+JAtZW72uuWbl513ZWrNFZkMwHk4sQYtDAr5WN6b5eYtzb8d+iVSFgJ4OZzCEFQY9UmpQMpkaea+UEOQvCHr2PEeyyUeA249+QICOpZ4xswQOuYSL0bS3FrjB7dHbxyXWNste5+n/FU1bFOdcsbbIpLJrlan2s9smJq5dliiKUyIke+osgdQfC+DRc9k9QGddBui24lQBdUOpks0KTw9dgy9076FjdVjjJoT5qxxfHuuzg==~-1~-1~-1; rid=fe3046c4-d35c-4ed1-b83a-d23baa7c5d52; cart-was-updated-in-standard=true; ITXSESSIONID=0dcea3afce672cd936c9255cd09ffcd3; OptanonAlertBoxClosed=2023-02-18T10:37:38.302Z; selectedRegion=it; bm_mi=ABDFF901EA7CDBEB3971A49B5C9AB542~YAAQVzYWAnzAECiGAQAAcNMwZBJX8aVXyE0SBKrBH6pMJvrc/N3r2gQbM6MP9NO0CGM0PZ+r3XIsSsu2aP7aSI3eH/mAsNtPXLN6caO2rtzqTAxykKF6jhcaMsj7hF3LKE0BJW6vuXPkAMalHu0m6Exj0OCdd149JNzge0tc9F2dsmeG+z8jcbJ643/zF6jXIk9/mhXixR8WsuGuuw5BHhAQt3W2RDZLEPtDj4soQTyZgNu/I6StMJOve3rKanwP2M/T7S8pUZHs2BL9klpGtwhknOENyRZPGKKpLUNOSKOKpxTrpfWn+vmrro7Jz0wHJM1pSgRvj7bVfaV5HfOJFwhIGKT3I0E=~1; bm_sv=959CEC0E6239254F242F39A3A4237331~YAAQVzYWApDAECiGAQAA0dkwZBIQ3H/8ywd0MxKBUEwKP5HbdRtgoE1czYQWiQsPtAYacfzg+WkIPxMNtyskCVRoD6W7rH6fghzSzaLU+P+hIfbNaZsfziekEEmSS22pxtqwRTBFAHXXyPgHGb1xkmuLOTCul0qnTd3Aw6JjTC43fA4ysE6k4XdOjgeDD5SjndehvJXSBPnOUwQdG8uj5tCWdKSK7d28d9iSEQaHaqE6qteBcfDTKwzjpeHhzig=~1; ak_bmsc=09561AF7817160437542725ACDD857E9~000000000000000000000000000000~YAAQVzYWAr3AECiGAQAARRwxZBK6Mv8JM+WUIaDOkdgV0StlYBHA6eSqNvmhZBY1q9YrCcZj9eyxqJ3PpamVHiqC1qVk1OUIPxhDCIaOq/NvBkIoI/erY5prxZyXraoq/bTP+1MulZ5tAZcKX2Nn/yzjQ5wVK43qxE+A8o4qY/u8aBd/8NG695NqqeVI6rwrnijcCk39quBYcqUZMFAWJeDFG6QrLmrIyYer+3S3vZFxJkUToVak/xPhT5FbmVmzS5suWLZsQGTHmk/vixdwKaKG5gvcJtXuPcMZaibq45l+q1kWm/VTXG3T7eqFAy324OJ82YS3saYKRrfBaLu/4Ie9Qz81xvyNMKVkZ4dA2XFp3SCowafIlaLCRg48kdYZD2bKGyb4lz8JbIsYFLrHLUjXFvUGmTCci0mLVJXOTU6zsf8rKsxeYGI7F/XDlP09kAJHVlB4LIqERigITHw4eAjSeqIUOkqqpxox8OqH+NP8DG05Zz6ZlG7n6qRYnTGGfDUqBtqw; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Feb+18+2023+12%3A31%3A03+GMT%2B0100+(Ora+standard+dell%E2%80%99Europa+centrale)&version=6.28.0&isIABGlobal=false&hosts=&consentId=295db455-ae01-4aaf-ba0b-fdd27c2ff01a&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=NL%3BNH&AwaitingReconsent=false; storepath=it%2Fit; IDROSTA=7fabdd146b2f:1d840defea3942811c6faa5b2',
        'if-none-match': 'W/"10885a-zVy/Bt41sg8ETuoMg2lpbum1Qa8"',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }

    links_list = []

    webdriver.get('https://www.zara.com/it/it/donna-prezzi-speciali-l1314.html')
    time.sleep(2)

    elem = webdriver.find_element(By.ID, "onetrust-accept-btn-handler")
    elem.send_keys(Keys.ENTER)       
    webdriver.find_element(By.CLASS_NAME, "zds-button").send_keys(Keys.ENTER)

    #  id="onetrust-accept-btn-handler"

    for page_nr in range(1):

        webdriver.get('https://www.zara.com/it/it/donna-prezzi-speciali-l1314.html')


        #webdriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        soup = BeautifulSoup(webdriver.page_source,"lxml")
        print("###################")
        # print(soup)

        if not soup:
            break

        ul_list = soup.find_all("ul", class_="product-grid__product-list")
        print(ul_list)
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

    print(len(links_list))
    return links_list

# getLinks()
#print(getLinks()[0][1])



