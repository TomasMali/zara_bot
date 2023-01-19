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
        'bm_sz': 'F9C51C7875F4E7FCA66F8C097E61D14E~YAAQBocQAmplEXaFAQAAoPdnyxIk+0rV8CLajcoPZTOBPre6AIjvlqBDPXobUrliujRR3C8R3EMNbprv2d+IJsLbIPZXu0YoJ7cdhD/HiQO45ut55pk0WFGpoCy1bHMuwAkf9fC88baYMBhlgMqLHKmmpn8zGxhjm0c/6asAuTIZmTPlXFRQZz6U/2og41C+rZPE30olW+sn//uy5hRZmLN7/DBICv8Sk3RtP4qFstrZkrW+tft3jW+lbUtJbwmf2ItV23cpdKNqb8AjaobUkrw6JZ+ha91YPphummXLexvT~3159619~4535361',
        'cart-was-updated-in-standard': 'true',
        'bm_mi': 'ABCB2EA78B51442D9D9F0E38EC659BE4~YAAQBocQAmVsEXaFAQAAcL5oyxKQyxYs16D1z+jbCyIP1tD932UmMjjwx0+zczYEoqYf0elbuxKH297sHsamW8fD38SlVBO6fPdii6h1HqCwDXzq6o3FD8lOBqsIrUZ7TcpsPwIrFo86pBwRKmpSOCCj+TEVrGlY4Kw0d781E+US49oj+GMZabsOHEKc4D9UrzBLY/R2GaoOd5qeuMawdS4iao9ZmsruBeWxBDq35acx3A/IyP15tUa9kq5lyS1qzPf2yJsuEvPgAm0sYnpJWGZCRGYTlB4m9HGSkwab4/CpxsN2TT+hzMARXb+VxkwzVjqmEOBo0dd0grFDwuaRhlj/xuheZ25EPcSHvUGzt34=~1',
        'bm_sv': '8243029438CA497B44A97007B8D147D6~YAAQBocQAtptEXaFAQAA1/JoyxJM+PENKjf0iP2ICFla1sC6g/xnzMRpqoeioPwX2/GcBahUj/u/DBkimGIjw0EJiI++9ERfUoo8NHo/oVtLee4VhaKNEBkDjvN3d7/FvVCiqIyg00jWS/fS3BtEadVnk4kPW/mkP5ZJ/wXgFAWtLlnNKOzaIV8F6mFIEU8c94qqR8o8FkbF4CuVmZrI4j5s6LR/DLMsKmAe6OYjnYnC14wztawi8Th2g8VInmw=~1',
        'ITXSESSIONID': 'b7997086b8649f22dd009a774b3396da',
        'IDROSTA': '437e9f12f077:2fddafe87800b3ccb975bf77d',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+Jan+19+2023+20%3A20%3A55+GMT%2B0100+(Ora+standard+dell%E2%80%99Europa+centrale)&version=6.28.0&isIABGlobal=false&hosts=&consentId=78e8f2ca-2010-49be-a2fe-125a232b071d&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=IT%3B34&AwaitingReconsent=false',
        '_abck': '3E6AFB0791922E22A17904BBE6F2A5E1~0~YAAQWAsVAr2xy5uFAQAARGh7ywlsCXCeUnh3G/1KfKtrTDy+R3QSZGftppe3uJsCO/rSTUblSqP1HTV+8jfp/Sut2Q5XqF890AbEloDpz/rr+Cthd/61/wJn+TYRxioOuYU8QeM1+PiiZUkubOEgPdybtfp5htY6hd6kU9JX07nOZsSAKsyKtLBpaepusHaGtbxdTIxnj6qug5e1GYm9WSk5JGDpOtXMWb351IdcwtIrZpdgQUw+ycP0J3sabMkiEjPfKpyY23Z9pqu0/Kja20aoUsGtuFw80nIaWvsuYR6k71QGWuG2NfUimNzzFLmht8vEqG72NEzeQpYGB+F8cRVoh9GeiHt06OcTcNIXrBk1wUUsWrhgd3IiWka0SMpA3CfBPfuIFr4t2SWV2ojHgIQ06NUc~-1~-1~-1',
        'ak_bmsc': '50BAF0B313E3395FE4D8039AD8132BCC~000000000000000000000000000000~YAAQWAsVAt60y5uFAQAAYa57yxKEp7zYyb4HUlKqHRPU9wvvjm5dHpaqEuTgRgH1TKvuGVrLErOd8T1G2ej0HyuiON42SsVxbASd1cyiYlBih5QH3v30vgCVW/SnVuZdlbRBbfuPbm1nQlUhIAA2+ybOZNG6hEeGX12mI/4cR6NR6gxv5Pj+eMhzuEbj/qnVnxJiaenQdGz+/P7fhlxONnDjfcJgfj2l53LZMWDuwnMIx88zin8exhLnGZ/vApKu5BsukgFoaWwojemzJ977Q5kUHPpXwEdY/BWcyF6zsvWM0dlXJUYVIWsRMpfV47pvwWn+M1ZBbSoUKATOnEiblz5XcqTffsBJs3k0hydXhvb4aXa1hu/6ZSsO3DlbK5+DNaobW++GWXtB+/Y47RWtza0A0U2WzrHWZSkcgEHnRPjyFj43P5aQ5l+2BcX3Ij/VhNNRqDttVMHtw0WBDyeKWHEFgXCbAfZXBTR+PjRHQTf1nsgBK7XDZZ/D/Wd0nqA5Bx7AtdgKLOyUjlM3Mw0gFwmNoB0Y5TouAwuAcgl8MnZ2UUSzcqe9rbg=',
    }

    headers = {
        'authority': 'www.zara.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'it-IT,it;q=0.9,la;q=0.8',
        # 'cookie': 'rid=21fbe0fa-f2fa-4691-8120-75054458243e; storepath=it%2Fit; OptanonAlertBoxClosed=2023-01-18T22:45:01.565Z; migrated=true; bm_sz=F9C51C7875F4E7FCA66F8C097E61D14E~YAAQBocQAmplEXaFAQAAoPdnyxIk+0rV8CLajcoPZTOBPre6AIjvlqBDPXobUrliujRR3C8R3EMNbprv2d+IJsLbIPZXu0YoJ7cdhD/HiQO45ut55pk0WFGpoCy1bHMuwAkf9fC88baYMBhlgMqLHKmmpn8zGxhjm0c/6asAuTIZmTPlXFRQZz6U/2og41C+rZPE30olW+sn//uy5hRZmLN7/DBICv8Sk3RtP4qFstrZkrW+tft3jW+lbUtJbwmf2ItV23cpdKNqb8AjaobUkrw6JZ+ha91YPphummXLexvT~3159619~4535361; cart-was-updated-in-standard=true; bm_mi=ABCB2EA78B51442D9D9F0E38EC659BE4~YAAQBocQAmVsEXaFAQAAcL5oyxKQyxYs16D1z+jbCyIP1tD932UmMjjwx0+zczYEoqYf0elbuxKH297sHsamW8fD38SlVBO6fPdii6h1HqCwDXzq6o3FD8lOBqsIrUZ7TcpsPwIrFo86pBwRKmpSOCCj+TEVrGlY4Kw0d781E+US49oj+GMZabsOHEKc4D9UrzBLY/R2GaoOd5qeuMawdS4iao9ZmsruBeWxBDq35acx3A/IyP15tUa9kq5lyS1qzPf2yJsuEvPgAm0sYnpJWGZCRGYTlB4m9HGSkwab4/CpxsN2TT+hzMARXb+VxkwzVjqmEOBo0dd0grFDwuaRhlj/xuheZ25EPcSHvUGzt34=~1; bm_sv=8243029438CA497B44A97007B8D147D6~YAAQBocQAtptEXaFAQAA1/JoyxJM+PENKjf0iP2ICFla1sC6g/xnzMRpqoeioPwX2/GcBahUj/u/DBkimGIjw0EJiI++9ERfUoo8NHo/oVtLee4VhaKNEBkDjvN3d7/FvVCiqIyg00jWS/fS3BtEadVnk4kPW/mkP5ZJ/wXgFAWtLlnNKOzaIV8F6mFIEU8c94qqR8o8FkbF4CuVmZrI4j5s6LR/DLMsKmAe6OYjnYnC14wztawi8Th2g8VInmw=~1; ITXSESSIONID=b7997086b8649f22dd009a774b3396da; IDROSTA=437e9f12f077:2fddafe87800b3ccb975bf77d; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Jan+19+2023+20%3A20%3A55+GMT%2B0100+(Ora+standard+dell%E2%80%99Europa+centrale)&version=6.28.0&isIABGlobal=false&hosts=&consentId=78e8f2ca-2010-49be-a2fe-125a232b071d&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=IT%3B34&AwaitingReconsent=false; _abck=3E6AFB0791922E22A17904BBE6F2A5E1~0~YAAQWAsVAr2xy5uFAQAARGh7ywlsCXCeUnh3G/1KfKtrTDy+R3QSZGftppe3uJsCO/rSTUblSqP1HTV+8jfp/Sut2Q5XqF890AbEloDpz/rr+Cthd/61/wJn+TYRxioOuYU8QeM1+PiiZUkubOEgPdybtfp5htY6hd6kU9JX07nOZsSAKsyKtLBpaepusHaGtbxdTIxnj6qug5e1GYm9WSk5JGDpOtXMWb351IdcwtIrZpdgQUw+ycP0J3sabMkiEjPfKpyY23Z9pqu0/Kja20aoUsGtuFw80nIaWvsuYR6k71QGWuG2NfUimNzzFLmht8vEqG72NEzeQpYGB+F8cRVoh9GeiHt06OcTcNIXrBk1wUUsWrhgd3IiWka0SMpA3CfBPfuIFr4t2SWV2ojHgIQ06NUc~-1~-1~-1; ak_bmsc=50BAF0B313E3395FE4D8039AD8132BCC~000000000000000000000000000000~YAAQWAsVAt60y5uFAQAAYa57yxKEp7zYyb4HUlKqHRPU9wvvjm5dHpaqEuTgRgH1TKvuGVrLErOd8T1G2ej0HyuiON42SsVxbASd1cyiYlBih5QH3v30vgCVW/SnVuZdlbRBbfuPbm1nQlUhIAA2+ybOZNG6hEeGX12mI/4cR6NR6gxv5Pj+eMhzuEbj/qnVnxJiaenQdGz+/P7fhlxONnDjfcJgfj2l53LZMWDuwnMIx88zin8exhLnGZ/vApKu5BsukgFoaWwojemzJ977Q5kUHPpXwEdY/BWcyF6zsvWM0dlXJUYVIWsRMpfV47pvwWn+M1ZBbSoUKATOnEiblz5XcqTffsBJs3k0hydXhvb4aXa1hu/6ZSsO3DlbK5+DNaobW++GWXtB+/Y47RWtza0A0U2WzrHWZSkcgEHnRPjyFj43P5aQ5l+2BcX3Ij/VhNNRqDttVMHtw0WBDyeKWHEFgXCbAfZXBTR+PjRHQTf1nsgBK7XDZZ/D/Wd0nqA5Bx7AtdgKLOyUjlM3Mw0gFwmNoB0Y5TouAwuAcgl8MnZ2UUSzcqe9rbg=',
        'referer': 'https://www.zara.com/it/it/woman-series-serie70-l3288.html?v1=2105810',
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
        'v1': '2105810',
    }





    links_list = []


    for page_nr in range(10):
        page =  requests.get(
                   'https://www.zara.com/it/it/woman-series-serie70-l3288.html',
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



