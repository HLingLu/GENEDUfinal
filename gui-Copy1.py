#!/usr/bin/env python
# coding: utf-8

# In[80]:


#import tkinter as tK
from tkinter import *

import test
test


# In[1]:


import test
test=test.HI(input)
test.do(input) #ouput


# In[8]:


import test
import requests
from bs4 import BeautifulSoup
import json
#url編碼
import urllib
#import tkinter as tK
from tkinter import *
# test=test.HI("掃地機器人")

def printtxt():
    A = en.get()
    show.insert('insert',A)
    
shopee = Tk() #建立主視窗
shopee.title("省小錢花大錢")
#keyword = en.get()
# 標題\大小\ICON、顏色\透明度\置頂
# 設定視窗大小
shopee.geometry("800x500") # 寬*高 #+決定位置
shopee.minsize(width= 400,height = 200)
shopee.maxsize(width= 800,height = 500)
# 固定的話叫做resizable
# icon 
shopee.iconbitmap("management.ico")
## 背景顏色
shopee.config(background="#FF8800")
## 透明度 
shopee.attributes("-alpha",1) #1-0之間
# 置頂
shopee.attributes("-topmost",1)

#img = PhotoImage(file="shopee.png")

en = Entry()

                
#A = en.get()
show = Text(bg='#FF8800', fg='red',width=60 ,height=60 ,relief='flat',wrap="word")



lb = Label(bg="#FF8800",text="便宜蝦皮哪裡買",fg="white",
           font=('Arial Rounded MT', 36))
lb.pack()   
lb2 = Label(bg="#FF8800",text="請輸入你要查找的商品",fg="white")
lb2.pack()  

# entry
en.pack()
# AA="掃地機器人"

lb3 = Label(text="  ",background="#FF8800")
lb3.pack()  

btn = Button(text="GO!",fg="#FF5511",command = printtxt)
btn.config(width =5,height=3) #是以網格設計
#btn.config(image= img)
#btn.config(command = aaa) 點下按鈕的指令
#btn.config() 
btn.pack()

lb4 = Label(text="  ",background="#FF8800")
lb4.pack()  


scroll = Scrollbar(command=show.yview)

#info_show.config(text = a,b,c,d,e,f,g,h,i,j)
show.pack()
#info_show = Label(text="")
#info_simport requests
#,command =printtxt

shopee.mainloop()


# In[5]:



shopee = Tk() #建立主視窗
shopee.title("省小錢花大錢")
#keyword = en.get()
# 標題\大小\ICON、顏色\透明度\置頂
# 設定視窗大小
shopee.geometry("800x500") # 寬*高 #+決定位置
shopee.minsize(width= 400,height = 200)
shopee.maxsize(width= 800,height = 500)
# 固定的話叫做resizable
# icon 
shopee.iconbitmap("management.ico")
## 背景顏色
shopee.config(background="#FF8800")
## 透明度 
shopee.attributes("-alpha",1) #1-0之間
# 置頂
shopee.attributes("-topmost",1)

#img = PhotoImage(file="shopee.png")

en = Entry(show=None)
show = Text(bg='#FF8800', fg='red',width=60 ,height=60 ,relief='flat',wrap="word")

lb = Label(bg="#FF8800",text="便宜蝦皮哪裡買",fg="white",
           font=('Arial Rounded MT', 36))
lb.pack()   
lb2 = Label(bg="#FF8800",text="請輸入你要查找的商品",fg="white")
lb2.pack()  

# entry
en.pack()
AA="掃地機器人"

lb3 = Label(text="  ",background="#FF8800")
lb3.pack()  

btn = Button(text="GO!",fg="#FF5511")
btn.config(width =5,height=3) #是以網格設計
#btn.config(image= img)
#btn.config(command = aaa) 點下按鈕的指令
#btn.config() 
btn.pack()

lb4 = Label(text="  ",background="#FF8800")
lb4.pack()  


scroll = Scrollbar(command=show.yview)
#command =gen_item
#info_show.config(text = a,b,c,d,e,f,g,h,i,j)
show.pack()
#info_show = Label(text="")
##info_simport requests
#print(AAAA.Output)
#print("hi")


# In[33]:


import requests
from bs4 import BeautifulSoup
import json
#url編碼
import urllib
#import tkinter as tK
from tkinter import *


# In[4]:


import os
path="./downloads/"
pth="/content/drive/MyDrive/mycolab/people/"
os.chdir(path)


# In[ ]:



# #function
# def gen_item():
#     keyword = en.get()
#     limit = 50 #回傳數量
#     max_price = 100000 #最高價格
#     rate = 4 #4星以上
#     headers = {
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
#     'x-api-source': 'pc',
#     'referer': f'https://shopee.tw/search?keyword={urllib.parse.quote(keyword)}'}

# #cookies
#     s = requests.Session()
#     url = 'https://shopee.tw/api/v4/search/product_labels'
#     r = s.get(url, headers=headers)
# #print(r)

# #搜尋頁網址
#     url = f"https://shopee.tw/api/v4/search/search_items/?by=relevancy&keyword={urllib.parse.quote(keyword)}&limit={limit}&newest=0&order=desc&page_type=search&price_max={max_price}&rating_filter={rate}&version=2"
#     re = s.get(url, headers=headers)
# #print(re)

# #確認資料無誤
#     if re.status_code == requests.codes.ok:
#         data = re.json()

# #總資料數
#     totalcount = data['query_rewrite']['ori_total_count']
# #分頁（蝦皮每頁包含五十筆資料 ref:https://ithelp.ithome.com.tw/articles/10232930)
#     total_pg = (totalcount // 50) + 1
#     data['totalPage'] = total_pg
#     a = (f"total count: {totalcount}")
#     b = (f"total page: {total_pg}")
    
# #對每個分頁爬蟲
#     for num in range(0, total_pg):
#         #print("\nPage", num)
#         pg_url = f"https://shopee.tw/api/v4/search/search_items/?by=relevancy&keyword={urllib.parse.quote(keyword)}&limit=50&newest={num*50}&order=desc&page_type=search&version=2"
#         #page = num + 1
    
#         resp = requests.get(pg_url, headers=headers)
#         doc = resp.json()
#         position = 0
#         count = 0
    
#     #擷取分頁內每個商品的資訊
#         for d in doc['items']:
#             print("hi")
#             #print(d)
#             productid = d['item_basic']['itemid']
#             name = d['item_basic']['name']
#             shopid = d['item_basic']['shopid']
#             item_url = f"https://shopee.tw/product/{shopid}/{productid}" #商品網址

#         #商品名稱和網址
#             c= name
#             d= item_url
        
#         #商品內頁
#             re_item_url = f"https://shopee.tw/api/v4/item/get?itemid={productid}&shopid={shopid}" #get的網址
#             re_item = requests.get(re_item_url, headers=headers)
#             imf = re_item.json()
#             #print(imf)
        
#         # 運費優惠內頁#
#             re_shipping_url = f"https://shopee.tw/api/v4/pdp/get_shipping?buyer_zipcode=&city=%E5%A4%A7%E5%AE%89%E5%8D%80&district=&itemid={productid}&shopid={shopid}&state=%E8%87%BA%E5%8C%97%E5%B8%82&town=" #get的網址
#             re_shipping = requests.get(re_shipping_url, headers=headers)
#             ims = re_shipping.json()
        
#         #每個細項名稱+運費#
#             for i, item in enumerate(ims['data']['ungrouped_channel_infos']):
#                 e = f"  第{i+1}種運送方式  {str(item['name'])}   運費{int(item['min_price']/100000)}元"
            
        
#         #每個細項名稱+賣場優惠卷+價格
#             for i, item in enumerate(imf['data']['shop_vouchers']):
#                 if item['discount_value'] != None and item['discount_value'] > 0:
#                     f = f"  第{i+1}張折價券  滿{int(item['min_spend']/100000)}  折底{int(item['discount_value']/100000)}元"
#                 elif item['discount_percentage'] != None and item['discount_percentage'] > 0:
#                     g = f"  第{i+1}張折價券  滿{int(item['min_spend']/100000)}  打{int(100 - item['discount_percentage'])}折  最高折抵{int(item['discount_cap']/100000)}元"
        
#         #組合優惠
#             if imf['data']['bundle_deal_info'] != None:
#                 h =f"  組合優惠：{imf['data']['bundle_deal_info']['bundle_deal_label']}"
    
#             for i, item in enumerate(imf['data']['models']):
#             #過濾已經沒貨的
#                 if item['stock'] == 0:
#                     continue
#                 if len(imf['data']['models']) == 1:
#                     i= f"\tprice: {int(item['price']/100000)}\tstock: {item['stock']}"
#                 else:
#                     j = f"\t{item['name']} price: {int(item['price']/100000)}\tstock: {item['stock']}"

#     # show.insert(END,a)
    
#,'b','c','d','e','f','g','h','i','j'

#def bbb[]:
    #t= en.get()
# label


# In[ ]:


ㄋ

