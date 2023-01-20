# from audioop import lin2ulaw
import requests
from bs4 import BeautifulSoup

#URL = "https://www.zara.com/it/it/woman-sale-l5503.html"


def getLinks():



    cookies = {
        'rid': '21fbe0fa-f2fa-4691-8120-75054458243e',
        'storepath': 'it%2Fit',
        'OptanonAlertBoxClosed': '2023-01-18T22:45:01.565Z',
        'migrated': 'true',
        'bm_sz': '4F81DEF957F0F1FB545D6C50EFC316EB~YAAQFmURAh21Jc6FAQAAU0jbzxI96PC/hVh0VMIiI9C+N+OViQ5QswoBM71jaR3eQ9Onj52MqcxCr2rKJz2Oc7FFDxGB87Nrf/YYJYNmClzt97H5vlnJIbF3xNn0ZF/q1aSp6yEOiAAWtbOp6pCxRzAdHSPCY3eJVjvoGSv8g80n7izFJBXYlUUrtDaW4ikj9zxUWLet2H62LchzCbjMTXbKQ+uRDoqNiVyeApzMuSEC/OVvvn1Hw4LV1xYDGzrYrnA0H4w94MCNI8EpM862JXiFo9Vwn6Ri+ARsuB3jB9nF~4273204~4538935',
        'bm_mi': '061D1F0CEA3474EC36F692657C663E9C~YAAQFmURAjS1Jc6FAQAAzUnbzxLawp8+RLRTbt8ysrjzkZbyTxKSP0Ry3vlfWDDAMbKCDIrKDnUhR4JwRVQ9coLjrjViE2x93y705IhrjIHKVeyWAnizg+9W/s3Byl+LEYUSvucPTY2wKI/y0tzcUn58Vp6Wb53DVjIn5Zq+2LNuPzYMs2UUhanE8CmQ4x3Q/CG2Iv6biIqldG9JXbnNWCS3VJk0qfe+aUOwXphdLoR7CfmD2SkNkiBFu8foE6VqlZ9Y8B/e/FuRE9V3umSXdaKUyG99uofRnvOCfNwOE0i4GL92GccJ4hghdpC4TBU=~1',
        'ITXSESSIONID': 'ad27220a9d834b6fa3a3ac280c8c4b0a',
        'IDROSTA': '6bfb66adb6f9:1c60ef0fb755a418886f40c0b',
        'cart-was-updated-in-standard': 'true',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Fri+Jan+20+2023+16%3A45%3A52+GMT%2B0100+(Ora+standard+dell%E2%80%99Europa+centrale)&version=6.28.0&isIABGlobal=false&hosts=&consentId=78e8f2ca-2010-49be-a2fe-125a232b071d&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=IT%3B34&AwaitingReconsent=false',
        '_abck': '3E6AFB0791922E22A17904BBE6F2A5E1~-1~YAAQJmURAjB2GMOFAQAAdqTdzwmKXJBwsl6qxmagZdfTLc/QzCziVat86Sw5WGOk+pJYMIrudSh9ucDskeD8jYvab1FSrsL/Z+8OTyepjG8Ls4LJw3QMZgLTXEk8vhoPU0W6LLqz5vthDJDSYKYrCHeYflK+HiOytzNpEDnvi4aNrSzF5sfZ0C0Psm7ux2Xgf4/SnS3QXR05yv4XVrG4jULoNm70HYjMPjPPU+x49X9B6OWjYeTmXFOHZ/oMGUYz5l37CAC53CF0Q/r3vOjI9wn4eXy7oyQvfuWM2YxwUQAK5oajjCc3JN1P6qyCxwxS+NKu7ihEtljNeWp76VNYpKlUFHLPajAcR9M/k6RDvHqVWpRxwU1RGRrimJ1f3L62tp3VVhvsgs0wjPh70HH/Rdlqz/zi~0~-1~-1',
        'ak_bmsc': 'DAF1D88845050C877F2745B43615FD61~000000000000000000000000000000~YAAQJmURAjl2GMOFAQAAYqXdzxKoD5eUbeRh9VTy/Mw6WtttbJhueJQA0w/ybektBX5W9fihSYu0j0N96I/H3XCebtApXOE5N38+qNxVyXGIailm3c/WjrdWZEHO0wENQNgZqPOm6FM0mEInP6aBghxmiFgfy+VE2R7T+rFiNVAd884O4BqnnfOpDIgnduWYLxcCD+tA6DfP0Vl/Ypyc4gn/PHs2MKAN+fXI4R+lC2WE/JpF3zqkjw+QXaX4nzQ0IM1OE5i7Bc+fGfJycPmb8Lc80cIeVtgDvItXy/HZnY/84wtE0dwc2sVnELVAUAmSuaB9MzH0KFIFRLNkyvxjkHGne0+8c/xa5lLhoIXuXToA52IFRhbff2hJ5a3EUgXab0Mt2f9a4LxMgwydtNqQ6GuimftoeAneqDPYI6EOI/XEa6ELm3AsbGl4G4MGXoAyK65bJw51jirXFyHftijnNdnHleLHZSLbkit4ydGSA91gjcAS2A==',
        'bm_sv': 'F9EE7264D11CF28D68A6F03714B2FF0F~YAAQJmURAjp2GMOFAQAAYqXdzxItN945go7i2bjwgs35vnQMvbNZehYrnmME5oH6+bsMJyCx38QMOfuf70SiNCixkFPNJxDKoZnzUV0x0YpguAnXeyI9V7uH9VjmSNnhdkihBFIWMmPOltz8FtHUulYtHXcacLv0OcIQgRsXEWMwgq1wNtof84VXDuo5CpgqsUaBus0CO0C1lrAlSQQvW4PMy1HHqCDU1v3gAnX2O9aljaK6CVd6cPYx1kuPHY4=~1',
    }

    headers = {
        'authority': 'www.zara.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'it-IT,it;q=0.9,la;q=0.8',
        # 'cookie': 'rid=21fbe0fa-f2fa-4691-8120-75054458243e; storepath=it%2Fit; OptanonAlertBoxClosed=2023-01-18T22:45:01.565Z; migrated=true; bm_sz=4F81DEF957F0F1FB545D6C50EFC316EB~YAAQFmURAh21Jc6FAQAAU0jbzxI96PC/hVh0VMIiI9C+N+OViQ5QswoBM71jaR3eQ9Onj52MqcxCr2rKJz2Oc7FFDxGB87Nrf/YYJYNmClzt97H5vlnJIbF3xNn0ZF/q1aSp6yEOiAAWtbOp6pCxRzAdHSPCY3eJVjvoGSv8g80n7izFJBXYlUUrtDaW4ikj9zxUWLet2H62LchzCbjMTXbKQ+uRDoqNiVyeApzMuSEC/OVvvn1Hw4LV1xYDGzrYrnA0H4w94MCNI8EpM862JXiFo9Vwn6Ri+ARsuB3jB9nF~4273204~4538935; bm_mi=061D1F0CEA3474EC36F692657C663E9C~YAAQFmURAjS1Jc6FAQAAzUnbzxLawp8+RLRTbt8ysrjzkZbyTxKSP0Ry3vlfWDDAMbKCDIrKDnUhR4JwRVQ9coLjrjViE2x93y705IhrjIHKVeyWAnizg+9W/s3Byl+LEYUSvucPTY2wKI/y0tzcUn58Vp6Wb53DVjIn5Zq+2LNuPzYMs2UUhanE8CmQ4x3Q/CG2Iv6biIqldG9JXbnNWCS3VJk0qfe+aUOwXphdLoR7CfmD2SkNkiBFu8foE6VqlZ9Y8B/e/FuRE9V3umSXdaKUyG99uofRnvOCfNwOE0i4GL92GccJ4hghdpC4TBU=~1; ITXSESSIONID=ad27220a9d834b6fa3a3ac280c8c4b0a; IDROSTA=6bfb66adb6f9:1c60ef0fb755a418886f40c0b; cart-was-updated-in-standard=true; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Jan+20+2023+16%3A45%3A52+GMT%2B0100+(Ora+standard+dell%E2%80%99Europa+centrale)&version=6.28.0&isIABGlobal=false&hosts=&consentId=78e8f2ca-2010-49be-a2fe-125a232b071d&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=IT%3B34&AwaitingReconsent=false; _abck=3E6AFB0791922E22A17904BBE6F2A5E1~-1~YAAQJmURAjB2GMOFAQAAdqTdzwmKXJBwsl6qxmagZdfTLc/QzCziVat86Sw5WGOk+pJYMIrudSh9ucDskeD8jYvab1FSrsL/Z+8OTyepjG8Ls4LJw3QMZgLTXEk8vhoPU0W6LLqz5vthDJDSYKYrCHeYflK+HiOytzNpEDnvi4aNrSzF5sfZ0C0Psm7ux2Xgf4/SnS3QXR05yv4XVrG4jULoNm70HYjMPjPPU+x49X9B6OWjYeTmXFOHZ/oMGUYz5l37CAC53CF0Q/r3vOjI9wn4eXy7oyQvfuWM2YxwUQAK5oajjCc3JN1P6qyCxwxS+NKu7ihEtljNeWp76VNYpKlUFHLPajAcR9M/k6RDvHqVWpRxwU1RGRrimJ1f3L62tp3VVhvsgs0wjPh70HH/Rdlqz/zi~0~-1~-1; ak_bmsc=DAF1D88845050C877F2745B43615FD61~000000000000000000000000000000~YAAQJmURAjl2GMOFAQAAYqXdzxKoD5eUbeRh9VTy/Mw6WtttbJhueJQA0w/ybektBX5W9fihSYu0j0N96I/H3XCebtApXOE5N38+qNxVyXGIailm3c/WjrdWZEHO0wENQNgZqPOm6FM0mEInP6aBghxmiFgfy+VE2R7T+rFiNVAd884O4BqnnfOpDIgnduWYLxcCD+tA6DfP0Vl/Ypyc4gn/PHs2MKAN+fXI4R+lC2WE/JpF3zqkjw+QXaX4nzQ0IM1OE5i7Bc+fGfJycPmb8Lc80cIeVtgDvItXy/HZnY/84wtE0dwc2sVnELVAUAmSuaB9MzH0KFIFRLNkyvxjkHGne0+8c/xa5lLhoIXuXToA52IFRhbff2hJ5a3EUgXab0Mt2f9a4LxMgwydtNqQ6GuimftoeAneqDPYI6EOI/XEa6ELm3AsbGl4G4MGXoAyK65bJw51jirXFyHftijnNdnHleLHZSLbkit4ydGSA91gjcAS2A==; bm_sv=F9EE7264D11CF28D68A6F03714B2FF0F~YAAQJmURAjp2GMOFAQAAYqXdzxItN945go7i2bjwgs35vnQMvbNZehYrnmME5oH6+bsMJyCx38QMOfuf70SiNCixkFPNJxDKoZnzUV0x0YpguAnXeyI9V7uH9VjmSNnhdkihBFIWMmPOltz8FtHUulYtHXcacLv0OcIQgRsXEWMwgq1wNtof84VXDuo5CpgqsUaBus0CO0C1lrAlSQQvW4PMy1HHqCDU1v3gAnX2O9aljaK6CVd6cPYx1kuPHY4=~1',
        'referer': 'https://www.zara.com/it/it/donna-prezzi-speciali-l1314.html?v1=2105311',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }

    params = {
        'v1': '2105311',
    }





    links_list = []


    for page_nr in range(10):
        page = requests.get(
            'https://www.zara.com/it/it/donna-prezzi-speciali-l1314.html',
            params=params,
            cookies=cookies,
            headers=headers,
)
        # If no page is founded exit
        if page.status_code != 200:
            print(page.status_code)
            break

        soup = BeautifulSoup(page.content, "html.parser")
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
                        # print(a['href'])

            # print("\n")


    print(len(links_list))
    return links_list


#getLinks()
#print(getLinks()[0][1])



