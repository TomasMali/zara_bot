# from audioop import lin2ulaw
import requests
from bs4 import BeautifulSoup

#URL = "https://www.zara.com/it/it/woman-sale-l5503.html"


def getLinks():

    cookies = {
        'migrated': 'true',
        'rid': '3b952398-df8e-45e2-8a48-588542c0f23e',
        'storepath': 'it%2Fit',
        '_abck': '274F7BE792B2EFF154D74EB3EE95B832~0~YAAQDocQAjMq16aCAQAAFHQ3rQh0D8xbMjbWoKgR49XUuMX215ZEG0ZDgyC2W1MmqcAt9dOz3LukxDy1N2/2x2cdlS2hcGp7/HitBaN6mW1zyO2/DULk0tD/2EAWoBg6TRTHDQM0qyFLLtg367qzuJrd2TmRYxGySewb6EjzHoUITi+XNZ9v2hcxWll7m8h8+USxSjjQCB6Zk10OlSlzR5Swe7MHXx3DmFsOo2g/nOPV8SNh4AQrcbpcm8KZ2A1C1oKOphwuREBirAbdclkjrRaMJrNHOOt8ioQ3pBk067qDZwCr/gwXH0Xskd7KC1onuMUG1EHMFA1yZK5qvH4mWVaY3J6H8JMHgrcmZjjR3KnDwTLa8/Td4dRZHBXsGfhePddoH9hLq1PoHzWo7qt+dX/vntMN~-1~-1~-1',
        'bm_sz': 'CF01F56AD743BCEC6A101394D6E77683~YAAQDocQAjQq16aCAQAAFHQ3rRDf8pyNper1JIJ9eRSq5C1I3d46X2Qa9z1cnUyelLFFlLPTBsc4UewGhbWZ7SwKuFXj7mGYKF9yM4dk+e2Xwe7Qoe6mOUC7bkQ237yNtYHZWatYFGptChlxqAbzXDXhpYunf5rNjArIotNDvgaYYX//czb7H4aeBUv5bJqpJJxxWCsn+4vkgRWoMHcmHIsV6jmpkFIl87Zr45UYe0d7lJdt2+5Ay3ipUSsqkfQZErfm7giAq4udtjSQkFWHX2s1qDfV2/Ne9RmjlZcOf+xK~4407603~4469049',
        'ITXSESSIONID': '478091e39a69390e3f0c106ff35819b1',
        'cart-was-updated-in-standard': 'true',
        'OptanonAlertBoxClosed': '2022-08-17T19:11:13.377Z',
        'bm_mi': '75D57A27DD87CC6AE2E75CCEE98F90D0~YAAQZwsVAv5M4qaCAQAAdENBrRBK6FqGTMAK5e756dIPQEzNX+hVN1flxFspMCUq+DAbsmulRxrgXpb6m84z0k+Kj8YDxOcM/mKNDp6KqHhr1xcpIOJkyv7h3B9OyjqrvBl23OBrhvuq5xtts9WJiHruqIdlKoLvjLi7E7D/NGvYCJh0n+AaSRGFjY/0jTe+2Penbo11D9qoMJ6hAe+wejGMyAUgkNQhpAMA73nHhGyP7i+1moahLEtcWsmkbK+slwvxOAuIIfMbl4tPmJnjMClcCyw9ahH/bJdAKRGNgnH67OAlgkTJjXvLXp1TllMFuK0Y9jM74i3UMWYaO8Trk1aKDrY=~1',
        'ak_bmsc': '98410ACDB135169F543BEA3944E4A456~000000000000000000000000000000~YAAQZwsVAlVd4qaCAQAA1ktCrRC8Ee1Ww9A8omswP7wvxYg57DkNCV3PiN9DYp3z960HCCXer1nngUKVjLtJzdgEdvQBgbiLOp3qVMrAl5LI7qpcvB4b6jIv5498iiJit9/E2gpuLXETH+aimTzYMm1s/6xZgDVNLIfe4O1N8NuohRmARC+UZ/tGRdQt2S4vBqY70ClGtUtk9FfktqLGEhgbBOdaYM/nxhmgoEsAbQIDGM590GEEJaxG0eJW6bjH9K6NlBJ6WVFbyidbR6RwuX/TIVOw1g4YTC7LpVGkR8EXFl6AvDVfSb0Lxm+7SvVr+e/aukAjdg+VZkWrECKBlImbTnzYLBtYxsEuobHK/wJi3UiQLJ6SC3gcYWYg/vFaRivzZGsHq+nzeIS85hV3cG2kHOx8qXu/+lYGvGG8hZZAj2ihKXKr8w4xExj0n1zpzMEPS/4Cuxri6Y0/5mbQNvehoTjA6GA2DBNJy1VzJva3TS/lLnt1LDZxR1BdSlBivwqZbZzuA9yhndbmVC2BzKyDDKyHYY7nB6sCQA==',
        'IDROSTA': '8f2d26689c7c:1ee1ff58ece717304df861c20',
        'OptanonConsent': 'consentId=d2f1264d-f345-4138-89bc-61515d94f44c&datestamp=Wed+Aug+17+2022+21%3A23%3A30+GMT%2B0200+(Central+European+Summer+Time)&version=6.28.0&interactionCount=1&isGpcEnabled=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=IT%3B25',
    }

    headers = {
        'authority': 'www.zara.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'it-IT,it;q=0.9,la;q=0.8',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'migrated=true; rid=3b952398-df8e-45e2-8a48-588542c0f23e; storepath=it%2Fit; _abck=274F7BE792B2EFF154D74EB3EE95B832~0~YAAQDocQAjMq16aCAQAAFHQ3rQh0D8xbMjbWoKgR49XUuMX215ZEG0ZDgyC2W1MmqcAt9dOz3LukxDy1N2/2x2cdlS2hcGp7/HitBaN6mW1zyO2/DULk0tD/2EAWoBg6TRTHDQM0qyFLLtg367qzuJrd2TmRYxGySewb6EjzHoUITi+XNZ9v2hcxWll7m8h8+USxSjjQCB6Zk10OlSlzR5Swe7MHXx3DmFsOo2g/nOPV8SNh4AQrcbpcm8KZ2A1C1oKOphwuREBirAbdclkjrRaMJrNHOOt8ioQ3pBk067qDZwCr/gwXH0Xskd7KC1onuMUG1EHMFA1yZK5qvH4mWVaY3J6H8JMHgrcmZjjR3KnDwTLa8/Td4dRZHBXsGfhePddoH9hLq1PoHzWo7qt+dX/vntMN~-1~-1~-1; bm_sz=CF01F56AD743BCEC6A101394D6E77683~YAAQDocQAjQq16aCAQAAFHQ3rRDf8pyNper1JIJ9eRSq5C1I3d46X2Qa9z1cnUyelLFFlLPTBsc4UewGhbWZ7SwKuFXj7mGYKF9yM4dk+e2Xwe7Qoe6mOUC7bkQ237yNtYHZWatYFGptChlxqAbzXDXhpYunf5rNjArIotNDvgaYYX//czb7H4aeBUv5bJqpJJxxWCsn+4vkgRWoMHcmHIsV6jmpkFIl87Zr45UYe0d7lJdt2+5Ay3ipUSsqkfQZErfm7giAq4udtjSQkFWHX2s1qDfV2/Ne9RmjlZcOf+xK~4407603~4469049; ITXSESSIONID=478091e39a69390e3f0c106ff35819b1; cart-was-updated-in-standard=true; OptanonAlertBoxClosed=2022-08-17T19:11:13.377Z; bm_mi=75D57A27DD87CC6AE2E75CCEE98F90D0~YAAQZwsVAv5M4qaCAQAAdENBrRBK6FqGTMAK5e756dIPQEzNX+hVN1flxFspMCUq+DAbsmulRxrgXpb6m84z0k+Kj8YDxOcM/mKNDp6KqHhr1xcpIOJkyv7h3B9OyjqrvBl23OBrhvuq5xtts9WJiHruqIdlKoLvjLi7E7D/NGvYCJh0n+AaSRGFjY/0jTe+2Penbo11D9qoMJ6hAe+wejGMyAUgkNQhpAMA73nHhGyP7i+1moahLEtcWsmkbK+slwvxOAuIIfMbl4tPmJnjMClcCyw9ahH/bJdAKRGNgnH67OAlgkTJjXvLXp1TllMFuK0Y9jM74i3UMWYaO8Trk1aKDrY=~1; ak_bmsc=98410ACDB135169F543BEA3944E4A456~000000000000000000000000000000~YAAQZwsVAlVd4qaCAQAA1ktCrRC8Ee1Ww9A8omswP7wvxYg57DkNCV3PiN9DYp3z960HCCXer1nngUKVjLtJzdgEdvQBgbiLOp3qVMrAl5LI7qpcvB4b6jIv5498iiJit9/E2gpuLXETH+aimTzYMm1s/6xZgDVNLIfe4O1N8NuohRmARC+UZ/tGRdQt2S4vBqY70ClGtUtk9FfktqLGEhgbBOdaYM/nxhmgoEsAbQIDGM590GEEJaxG0eJW6bjH9K6NlBJ6WVFbyidbR6RwuX/TIVOw1g4YTC7LpVGkR8EXFl6AvDVfSb0Lxm+7SvVr+e/aukAjdg+VZkWrECKBlImbTnzYLBtYxsEuobHK/wJi3UiQLJ6SC3gcYWYg/vFaRivzZGsHq+nzeIS85hV3cG2kHOx8qXu/+lYGvGG8hZZAj2ihKXKr8w4xExj0n1zpzMEPS/4Cuxri6Y0/5mbQNvehoTjA6GA2DBNJy1VzJva3TS/lLnt1LDZxR1BdSlBivwqZbZzuA9yhndbmVC2BzKyDDKyHYY7nB6sCQA==; IDROSTA=8f2d26689c7c:1ee1ff58ece717304df861c20; OptanonConsent=consentId=d2f1264d-f345-4138-89bc-61515d94f44c&datestamp=Wed+Aug+17+2022+21%3A23%3A30+GMT%2B0200+(Central+European+Summer+Time)&version=6.28.0&interactionCount=1&isGpcEnabled=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=IT%3B25',
        'if-none-match': 'W/"9a35b-n1BNsMnTDZBMULc9E6ZeI4NGzPY"',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }

    links_list = []


    for page_nr in range(100):
        page = requests.get('https://www.zara.com/it/it/woman-sale-l5503.html?page='+str(page_nr+1),  headers=headers)
        # If no page is founded exit
        if page.status_code != 200:
            break

        soup = BeautifulSoup(page.content, "html.parser")
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
                        # print(a['href'])

            # print("\n")


    print(len(links_list))
    return links_list



print(getLinks()[0][1])



