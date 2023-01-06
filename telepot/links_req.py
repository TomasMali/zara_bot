# from audioop import lin2ulaw
import requests
from bs4 import BeautifulSoup

#URL = "https://www.zara.com/it/it/woman-sale-l5503.html"


def getLinks():

    cookies = {
        'bm_sz': '72EA09655327DBC60B819CFF2CCE8420~YAAQfq4AF4x7qQWFAQAAZwYkiRI09psxoScFv30I6AXwrddXNjSPtQH72Y3kMc8utdE08oYb6pocjqjp68kBUthhg3Tx/doJhnPBNkKtDTtF1IGOYsHoq6oDGDu+0pktnfk/qEiRpFHPe9AjQque+6UOgAiKFlQCdbJDBrkSu6Kyng/sjODuxxqtkpdmInm0ofny+OuUkV0Fb8Csx8S2n60hwax4pt+wIFOPYp0VB0UjkoPzPZ9PkH8LlZKs16XLxuvRI2BmtmtMUgbEb1BpX54BZHLnFaHMJr5VFjAWmFrq~3622453~3158832',
        'rid': '18e8360a-e5df-40c7-98ba-05972a099d63',
        'cart-was-updated-in-standard': 'true',
        'bm_mi': '5286D7B35E4F2810FD1B6CB41AC388D4~YAAQXa4AF1YDjYCFAQAAJ4MuiRJWk4cJ9ysGmb0V3D9NyEH0hbNwHEsP7L1dnrW0Wa2DogvftHO9EIRiBJx9kQ29VxneS7Z/t8Q50qUxDWiZG6ehqSgbeEZBEiEseV4l0FdGo32cCnuy3M8iM39QIXzLlGDq7A86BxJQM8fHjsnyp2tX2bOYV3NLeBb993SjrjwUnqiUniwCkonqHjeiz74FEdvRXde8cMt4TFEY9IQAd55n5hSqJasJhoV8f9Y3Y/6K+YQidR6FM58qTI0X3J1oE72sNLiUav4lvAIXejvs7QYVRL68L1Q9UZ9LvTM=~1',
        'bm_sv': '28F909032E8BE0119F94301A0AF69CB0~YAAQXa4AF20DjYCFAQAAeoguiRL6RSRtE5oCNCtBaYoYM8PcvXSyl47ySQW4V8rVcgubLlqc05GIKPslRC5PnyIhdjdUxXvXFpziMT555T7aQ3jArDW/073j88CMdmB8VM2KkkrV0VI4MUO18dYBYdxIZcjAmpF20lfSvQC6iT1qWDyENzYnlM7H1J335EQHHj0Ku20py2aRx5Js2l6gT8oKH0ANY6+D5cmfhgxfLqlYIECTzCRLNyTANVFhTU8=~1',
        'ak_bmsc': '260504C6B78401C0463FE84EC552F1CF~000000000000000000000000000000~YAAQXa4AF7UEjYCFAQAAuc8uiRIbLIXcIdLC2lqFaXPFWbvlFLTf9MJRtaYf7naN7s8z7r8NINtkxP3pvxMdEolkVU7qSiB3pje/ZR1OBi49E37X7dR6mlecdr6hepTqBiufNYWjawAcWh42Nz6VZRt258HHVOMdmddjahm2uchiTXNJEq7gbv1i6wy1cBJ+D4b8Qp3tdI8oOuCtFqwIoTjJ3ASIVqo0/doCzoFiU0nf5dnz03cmRMhouLPwi2fH6bfpn7JEd61lPuNX4isWrd/SW3DGMq2z0mPubsHI1lkwWJp+T0/rQ4xgOrGLv7c3tDU+9ClvVFYydgjE5CihNmk30oIg5kpHc/hkNnWMiCMWZ3DJvdErN18Pd4ZIqWEftAY0PSrJcDLQehKVFIT/n9aecGPUkbLxwtguO6nNOv3pLies7jd32Y5kpX+8QqN4oBCICBmgKlAJRrqao0wb3/nWY68H92HHk7Re6nct',
        '_abck': 'B1D1620173C3DE54189F328008980DDE~0~YAAQda4AF2F5HnWFAQAAXwEziQlhEfymKiUQvAx2/KRYAlkhDQa+0kqnDIm1v7ULL5m5ZQPyDtm7YOIcEtjHvbA7Q87qM9nleCAwlqY5VN8C7A1FHHwkwxGct7+hKBKK9HYxkByvWVHsukprlnzIa7Gr7QVBM9QtmaahtrjyBlstXtitN4XNXMiJ2GggC4yq2E+xoAK4XgYm2cfChY/BN7q9Cklyrb7BY5j9Bk4/wplH48HWNttSF06oRjSAnfIBJwe27aqTBt4GhPPh0bZbctXPKT7d2IXiiUxpHPd8q2Sp0Lzb7MEta5w/MDolvD1800q4OYm1L1MOI0XmL1i2nQTDCwpgnQ/JIUFJZF/YJdc9qPQAidnVER17u6Dtu0G7A0hSdj4q08sa4sZPl10MZMDi1h1dEA==~-1~-1~-1',
        'ITXSESSIONID': 'a38920cd27782a76e3032e00e8ce17a6',
        'IDROSTA': '1ca8058f6a8f:2276d45e94505ec2d5d69a78d',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Fri+Jan+06+2023+23%3A28%3A47+GMT%2B0100+(Ora+standard+dell%E2%80%99Europa+centrale)&version=6.28.0&isIABGlobal=false&hosts=&consentId=f1fd5313-b1f0-477b-a128-c2cb059868f1&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=CH%3BZH&AwaitingReconsent=false',
        'OptanonAlertBoxClosed': '2023-01-06T22:28:47.144Z',
        'storepath': 'it%2Fit',
    }

    headers = {
        'authority': 'www.zara.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'it-IT,it;q=0.9,la;q=0.8',
        'cache-control': 'max-age=0',
        # 'cookie': 'bm_sz=72EA09655327DBC60B819CFF2CCE8420~YAAQfq4AF4x7qQWFAQAAZwYkiRI09psxoScFv30I6AXwrddXNjSPtQH72Y3kMc8utdE08oYb6pocjqjp68kBUthhg3Tx/doJhnPBNkKtDTtF1IGOYsHoq6oDGDu+0pktnfk/qEiRpFHPe9AjQque+6UOgAiKFlQCdbJDBrkSu6Kyng/sjODuxxqtkpdmInm0ofny+OuUkV0Fb8Csx8S2n60hwax4pt+wIFOPYp0VB0UjkoPzPZ9PkH8LlZKs16XLxuvRI2BmtmtMUgbEb1BpX54BZHLnFaHMJr5VFjAWmFrq~3622453~3158832; rid=18e8360a-e5df-40c7-98ba-05972a099d63; cart-was-updated-in-standard=true; bm_mi=5286D7B35E4F2810FD1B6CB41AC388D4~YAAQXa4AF1YDjYCFAQAAJ4MuiRJWk4cJ9ysGmb0V3D9NyEH0hbNwHEsP7L1dnrW0Wa2DogvftHO9EIRiBJx9kQ29VxneS7Z/t8Q50qUxDWiZG6ehqSgbeEZBEiEseV4l0FdGo32cCnuy3M8iM39QIXzLlGDq7A86BxJQM8fHjsnyp2tX2bOYV3NLeBb993SjrjwUnqiUniwCkonqHjeiz74FEdvRXde8cMt4TFEY9IQAd55n5hSqJasJhoV8f9Y3Y/6K+YQidR6FM58qTI0X3J1oE72sNLiUav4lvAIXejvs7QYVRL68L1Q9UZ9LvTM=~1; bm_sv=28F909032E8BE0119F94301A0AF69CB0~YAAQXa4AF20DjYCFAQAAeoguiRL6RSRtE5oCNCtBaYoYM8PcvXSyl47ySQW4V8rVcgubLlqc05GIKPslRC5PnyIhdjdUxXvXFpziMT555T7aQ3jArDW/073j88CMdmB8VM2KkkrV0VI4MUO18dYBYdxIZcjAmpF20lfSvQC6iT1qWDyENzYnlM7H1J335EQHHj0Ku20py2aRx5Js2l6gT8oKH0ANY6+D5cmfhgxfLqlYIECTzCRLNyTANVFhTU8=~1; ak_bmsc=260504C6B78401C0463FE84EC552F1CF~000000000000000000000000000000~YAAQXa4AF7UEjYCFAQAAuc8uiRIbLIXcIdLC2lqFaXPFWbvlFLTf9MJRtaYf7naN7s8z7r8NINtkxP3pvxMdEolkVU7qSiB3pje/ZR1OBi49E37X7dR6mlecdr6hepTqBiufNYWjawAcWh42Nz6VZRt258HHVOMdmddjahm2uchiTXNJEq7gbv1i6wy1cBJ+D4b8Qp3tdI8oOuCtFqwIoTjJ3ASIVqo0/doCzoFiU0nf5dnz03cmRMhouLPwi2fH6bfpn7JEd61lPuNX4isWrd/SW3DGMq2z0mPubsHI1lkwWJp+T0/rQ4xgOrGLv7c3tDU+9ClvVFYydgjE5CihNmk30oIg5kpHc/hkNnWMiCMWZ3DJvdErN18Pd4ZIqWEftAY0PSrJcDLQehKVFIT/n9aecGPUkbLxwtguO6nNOv3pLies7jd32Y5kpX+8QqN4oBCICBmgKlAJRrqao0wb3/nWY68H92HHk7Re6nct; _abck=B1D1620173C3DE54189F328008980DDE~0~YAAQda4AF2F5HnWFAQAAXwEziQlhEfymKiUQvAx2/KRYAlkhDQa+0kqnDIm1v7ULL5m5ZQPyDtm7YOIcEtjHvbA7Q87qM9nleCAwlqY5VN8C7A1FHHwkwxGct7+hKBKK9HYxkByvWVHsukprlnzIa7Gr7QVBM9QtmaahtrjyBlstXtitN4XNXMiJ2GggC4yq2E+xoAK4XgYm2cfChY/BN7q9Cklyrb7BY5j9Bk4/wplH48HWNttSF06oRjSAnfIBJwe27aqTBt4GhPPh0bZbctXPKT7d2IXiiUxpHPd8q2Sp0Lzb7MEta5w/MDolvD1800q4OYm1L1MOI0XmL1i2nQTDCwpgnQ/JIUFJZF/YJdc9qPQAidnVER17u6Dtu0G7A0hSdj4q08sa4sZPl10MZMDi1h1dEA==~-1~-1~-1; ITXSESSIONID=a38920cd27782a76e3032e00e8ce17a6; IDROSTA=1ca8058f6a8f:2276d45e94505ec2d5d69a78d; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Jan+06+2023+23%3A28%3A47+GMT%2B0100+(Ora+standard+dell%E2%80%99Europa+centrale)&version=6.28.0&isIABGlobal=false&hosts=&consentId=f1fd5313-b1f0-477b-a128-c2cb059868f1&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=CH%3BZH&AwaitingReconsent=false; OptanonAlertBoxClosed=2023-01-06T22:28:47.144Z; storepath=it%2Fit',
        'if-none-match': 'W/"f9aa1-xqv4vyd4xQuYk6MuoZnOAQ9g+3g"',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }


    links_list = []


    for page_nr in range(100):
        page = requests.get('https://www.zara.com/it/it/woman-special-edition-l5114.html?page=' + str(page_nr+1),headers=headers)
        # If no page is founded exit
        if page.status_code != 200:
            print(page.status_code)
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


#getLinks()
# print(getLinks()[0][1])



