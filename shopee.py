import requests
from bs4 import BeautifulSoup
import json
#url編碼
import urllib

keyword = input("請輸入關鍵字:")
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

#總資料數
totalcount = data['query_rewrite']['ori_total_count']
#分頁（蝦皮每頁包含五十筆資料 ref:https://ithelp.ithome.com.tw/articles/10232930)
total_pg = (totalcount // 50) + 1
data['totalPage'] = total_pg
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
        name = d['item_basic']['name']
        shopid = d['item_basic']['shopid']
        item_url = f"https://shopee.tw/product/{shopid}/{productid}" #商品網址
        #print(f"shopid: {shopid}   productid: {productid}")
        print(name)
        print(item_url)
        
        #商品內頁
        re_item_url = f"https://shopee.tw/api/v4/item/get?itemid={productid}&shopid={shopid}" #get的網址
        re_item = requests.get(re_item_url, headers=headers)
        imf = re_item.json()
        #print(imf)
        
        #每個細項名稱+價格
        for i, item in enumerate(imf['data']['models']):
            if len(imf['data']['models']) == 1:
                print(f"\tprice: {int(item['price']/100000)}")
            else:
                print(f"\t{item['name']} price: {int(item['price']/100000)}")
