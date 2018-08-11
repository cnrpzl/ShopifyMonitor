import requests
import json
import random
import time
from bs4 import BeautifulSoup as bs
from datetime import datetime
from colorama import Fore, Back, Style, init
import multiprocessing
import twitter
import discord
import asyncio
client = discord.Client()

########@CNRPZL########
#I have learned a lot from reading source code, and hopefully people will learn something from this, even if it is amateurish. Hit my twitter if you have any ideas, @CNRPZL GL
########@CNRPZL########

####GLOBAL VARIBLES####
discurl = "https://discordapp.com/api/webhooks//"
keywords = ["NIKE", "THE TEN"]
keywords2 = ["TRAVIS", "SCOTT"]
keywords3 = ["JORDAN", "QUAI"]
keywords4 = ["REACT", "BONE"]
keywords5 = ["YEEZY", "BOOST"]
keywords6 = ["THE 10", "PRESTO"]
keywords7 = ["OFF", "WHITE", "PRESTO"]
keywords8 = ["OFF", "WHITE", "JORDAN"]
keywords10 = ["PARRA", "SPIRIDON"]
keywords11 = ["PARRA", "AIR MAX"]
msg2 = None
listtest = [keywords, keywords2, keywords3, keywords4, keywords5, keywords6, keywords7, keywords8, keywords10, keywords11]
size = "4.5"
z = 0
random_size = False
s = requests.session()
#s.config['keep_alive'] = False
product = None
continueaftercheckout = True
sku = None
siteurls = ["sitehere.com", "sitehere.com"]
proxies = {
  'http': 'proxieshere',
  'https': 'proxieshere',
}
####GLOBAL VARIBLES####
########@CNRPZL########

def get_list_of_products(siteurl):
    #print("get li")
    try:
        prod_get= s.get("http://" + siteurl + "/products.json", timeout=3)
        products_json = json.loads(prod_get.text)
        products = products_json["products"]
        return products
    except:
        return False

def keyword_search(products, keywords):
    #print("Keysearch")
    #try:
    stopex = 0
    for product in products:
        keys = 0
        stopex += 1
        for keyword in keywords:
            if keyword.upper() in product["title"].upper():
                keys += 1
            if keys == len(keywords):
                #print(product["title"])
                return product
        if stopex == len(products):
                #print("TEST")
            return False

    if product == None:
        return False

    #except:
        #print("KS Exception")
        #return False

def find_size(product, size, siteurl):
    #print("find_size")
    global msg2
    try:
        for variant in product["variants"]:
            # print(variant['id'])
            if size in variant["title"] and variant['available'] != False and random_size == False:
                print("Size: " + variant['title'] + " " + product['title'] + " is in stock!")
                try:
                    LUL = product['handle']
                    twitter.sendtotwitter(str(product['title']) + " is in stock! " + "https://" + siteurl + "/products/" + str(LUL))
                except:
                    # print("Failed")
                    pass
                return variant['id']
        variants = []
        for variant in product["variants"]:
            LUL = product['handle']
            if variant['available'] != False:
                variants.append(variant["id"])
                # print(len(variants))
            if variant['available'] == False:
                pass
            if len(variants) != 0:
                variant = str(random.choice(variants))
                # print(variants)
                print((product['title'] + " is in stock!"))
                try:
                    msg = product['title'] + " " + siteurl
                    if msg != msg2:
                        msg2 = product['title'] + " " + siteurl
                        requests.post(discurl, data={"content":product['title'] + " is in stock! " + "https://" + siteurl + "/products/" + str(LUL)})
                        twitter.sendtotwitter(product['title'] + " is in stock! " + "https://" + siteurl + "/products/" + str(LUL))
                    else:
                        pass
                except:
                    pass
                return variant
        else:
            print("No sizes in stock for " + product['title'])
            return None
    except:
        print("Find size exception")
        return None
    else:
        print("No sizes in stock for " + product['title'])
        return None


def main(s, cartlink):
    return False
    #This is where a checkout function would go

def testfunc(keylist):
    global s
    t2 = time.time()
    t2
    global z
    global msg2
    products = get_list_of_products(siteurls[z])
    if products == False:
        print("Could not retrieve " + siteurls[z] + "...")
        s = requests.session()
        return None
    x = 0
    cartlink = None
    for y in listtest:
        ks = keyword_search
        findsize = find_size
        mainz = main
        if ks(products, listtest[x]) != False:
            if findsize(ks(products, listtest[x]), size, siteurls[z]) != None:
                #cartlink = "https://" + siteurls[z] + "/cart/" + str(findsize(s, ks(s, products, listtest[x]), size)) + ":1"
                if main(s, cartlink) == False:
                    x += 1
                    break
                else:
                    if continueaftercheckout == True:
                        x += 1
                        continue
                    else:
                        print("Checked out, stopping program...")
            else:
                x += 1
        else:
            #print("No products found for - " + str(listtest[x]))
            x += 1
    print(siteurls[z])
    z += 1
    #print(len(siteurls))
    if z == len(siteurls):
        t3 = time.time()
        t3
        print("--- %s seconds ---" % (t3 - t2))
        z = 0
        return None


while True:
    testfunc(listtest)
