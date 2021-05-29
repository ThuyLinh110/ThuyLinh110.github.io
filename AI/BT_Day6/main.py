import requests
import codecs
from bs4 import BeautifulSoup
import json
import pandas

data_url="https://beautygarden.vn/danh-muc/cham-soc-da.html"

def save_url_to_json(url_list, file):
    with open(file,'w',encoding='utf-8') as f:
        json.dump(url_list,f,indent=2,ensure_ascii=False)

#get all url of products    --> get list urls 
def get_all_url_products(url):
    url_list=[]
    i=1
    url_link=url+"?&page="+str(i)
    response =requests.get(url_link)
    soup=BeautifulSoup(response.content,features="html.parser")
    infor_products=soup.find_all(class_="pd-box")
    while infor_products !=[] :
        for tag in infor_products:
           el = tag.find('a',href=True)
           if el['href']:
              url_list.append(el['href'])
        i+=1
        url_link=url+"?&page="+str(i)
        response =requests.get(url_link)
        soup=BeautifulSoup(response.content,features="html.parser")
        infor_products=soup.find_all(class_="pd-box")
    return url_list

    
# get full url of products   --> save to product_data.json   
def pre_handler():
    product_urls= get_all_url_products(data_url)
    product_urls=['https://beautygarden.vn'+ x for x in product_urls]
    save_url_to_json(product_urls,'product_data.json')

pre_handler()
#load full url from product_data.json and get data of product  --> save to list_data_with_product.json
with open('product_data.json','r') as f:
    data=json.load(f)
list_data=[]
for x in data:
    page=requests.get(x)
    soup=BeautifulSoup(page.content,features="html.parser")   
    try:
        new_data={
            'url': x,
            "brand": soup.find(class_="hanc").text.strip(),
            "name product": soup.find('h1',class_="title-Product").text.strip(),
            "price before sale": soup.find(class_="price-drop").find(class_="issale").text.strip(),
            "sale off": soup.find(class_="price-drop").find(class_="persale").text.strip(),
            "price after sale": soup.find('div',class_="price-drop").find('span').text.strip(),      
        }
        list_data.append(new_data)
    except Exception as e:
        print('Exeption 2: ' , e)   
save_url_to_json(list_data,'list_data_with_product.json')  

     

