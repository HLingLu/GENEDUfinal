#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import requests
from bs4 import BeautifulSoup
import json
#url編碼
import urllib

class HI:
    def __init__(self,Input):
        self.Input=Input
        self.Output=[]
    def do(self):
        keyword = self.nput
        limit = 50 #回傳數量
        max_price = 100000 #最高價格
        rate = 4 #4星以上
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
            'x-api-source': 'pc',
            'referer': f'https://shopee.tw/search?keyword={urllib.parse.quote(keyword)}'
        }

        #cookies
        s = requests.Session()
        url = 'https://shopee.tw/api/v4/search/product_labels'
        r = s.get(url, headers=headers)
        #print(r)

        #搜尋頁網址
        url = f"https://shopee.tw/api/v4/search/search_items/?by=relevancy&keyword={urllib.parse.quote(keyword)}&limit={limit}&newest=0&order=desc&page_type=search&price_max={max_price}&rating_filter={rate}&version=2"
        re = s.get(url, headers=headers)
        #print(re)

        #確認資料無誤
        if re.status_code == requests.codes.ok:
            data = re.json()

        #商城優惠券
        official_url = "https://shopee.tw/api/v2/voucher_wallet/batch_get_vouchers_by_promotion_ids"
        re_official = requests.get(official_url, headers = headers)
        official = re_official.json()



        #總資料數
        totalcount = data['query_rewrite']['ori_total_count']
        #分頁（蝦皮每頁包含五十筆資料 ref:https://ithelp.ithome.com.tw/articles/10232930)
        total_pg = (totalcount // 50) + 1
        data['totalPage'] = total_pg
        self.Output.append(f"total count: {totalcount}")
        print(f"total count: {totalcount}")
        print(f"total page: {total_pg}")

        #對每個分頁爬蟲
        for num in range(0, total_pg):
            #print("\nPage", num)
            pg_url = f"https://shopee.tw/api/v4/search/search_items/?by=relevancy&keyword={urllib.parse.quote(keyword)}&limit=50&newest={num*50}&order=desc&page_type=search&version=2"
            #page = num + 1

            resp = requests.get(pg_url, headers=headers)
            doc = resp.json()
            position = 0
            count = 0

            #擷取分頁內每個商品的資訊
            for d in doc['items']:
                #print(d)
                productid = d['item_basic']['itemid']
                shopid = d['item_basic']['shopid']

                #商品名稱和網址
                name = d['item_basic']['name']
                item_url = f"https://shopee.tw/product/{shopid}/{productid}" #商品網址
                #print(name)
                #print(item_url)

                #商品內頁
                re_item_url = f"https://shopee.tw/api/v4/item/get?itemid={productid}&shopid={shopid}" #get的網址
                re_item = requests.get(re_item_url, headers=headers)
                imf = re_item.json()
                #print(imf)

                # 運費優惠內頁#
                re_shipping_url = f"https://shopee.tw/api/v4/pdp/get_shipping?buyer_zipcode=&city=%E5%A4%A7%E5%AE%89%E5%8D%80&district=&itemid={productid}&shopid={shopid}&state=%E8%87%BA%E5%8C%97%E5%B8%82&town=" #get的網址
                re_shipping = requests.get(re_shipping_url, headers=headers)
                ims = re_shipping.json()
                #print(ims['data'])

                #每個細項名稱+運費#
                ship = {}    # ship = {運送方式: 運費}
                if ims['data']['ungrouped_channel_infos'] == None :
                    ship['沒有適用的物流選項, 請與賣家聯繫確認'] = 'N/A'
                else:
                    for item in ims['data']['ungrouped_channel_infos']:
                        ship[str(item['name'])] = int(item['min_price']/100000)
                        #print(f"  第{i+1}張  {str(item['name'])}運送方式   運費{int(item['min_price']/100000)}元")

                #每個細項名稱+賣場優惠卷+價格
                voucher_discount = []     # voucher_discount = [(min_spend, discount_value)]
                voucher_percent = []      # voucher_percent = [(min_spend, discount_percentage, max_discount)]
                for i, item in enumerate(imf['data']['shop_vouchers']):
                    if item['discount_value'] != None and item['discount_value'] > 0:
                        voucher_discount.append((int(item['min_spend']/100000), int(item['discount_value']/100000)))
                        #print(f"  第{i+1}張折價券  滿{int(item['min_spend']/100000)}  折抵{int(item['discount_value']/100000)}元")
                    elif item['discount_percentage'] != None and item['discount_percentage'] > 0:
                        voucher_percent.append((int(item['min_spend']/100000), int(100 - item['discount_percentage']), int(item['discount_cap']/100000)))
                        #print(f"  第{i+1}張折價券  滿{int(item['min_spend']/100000)}  打{int(100 - item['discount_percentage'])}折  最高折抵{int(item['discount_cap']/100000)}元")

                #組合優惠
                bundle = []
                if imf['data']['bundle_deal_info'] != None:
                    bundle.append(imf['data']['bundle_deal_info']['bundle_deal_label'])
                    #print(f"  組合優惠：{imf['data']['bundle_deal_info']['bundle_deal_label']}")

                #商城
                if imf['data']['is_official_shop'] == True:
                    official_shop = True
                else:
                    official_shop = False

                for i, item in enumerate(imf['data']['models']):
                    #過濾已經沒貨的
                    if item['stock'] == 0:
                        continue

                    #算最低折扣價錢
                    price = int(item['price']/100000)
                    lowest_price = price
                    voucher_use  = "無"
                    for voucher in voucher_discount:
                        if (price >= voucher[0]):
                            price_dis = price - voucher[1]
                            if (price_dis < lowest_price):
                                lowest_price = price_dis
                                voucher_use = f"滿{voucher[0]}  折抵{voucher[1]}元"
                    for voucher in voucher_percent:
                        if (price >= voucher[0]):
                            if (round(price * voucher[1]/100) > price - voucher[2]):
                                price_per = round(price * voucher[1]/100)
                            else:
                                price_per = price - voucher[2]
                            if (price_per < lowest_price):
                                lowest_price = price_per
                                voucher_use = f"滿{voucher[0]} 打{voucher[1]}折 最高折抵{voucher[2]}元"

                    print("----------")
                    if len(imf['data']['models']) == 1:
                        print(f"商品名稱: {name}\n網址: {item_url}")
                    else:
                        print(f"商品名稱: {name}\n網址: {item_url}\n商品選項: {item['name']}")
                    print(f"原價: {price}    折扣後價格: {lowest_price}    庫存: {item['stock']}    所使用優惠券: {voucher_use}")
                    print("運費: ")
                    if (len(ship) != 0):
                        for k in ship.keys():
                            print(f"\t{k}: 運費{ship[k]}元")
                    print("其他優惠: ")
                    if (official_shop == True):
                        print("\t商城優惠券")
                    if (len(bundle) != 0):
                        print("\n\t".join(bundle))
                    else:
                        print("無")



