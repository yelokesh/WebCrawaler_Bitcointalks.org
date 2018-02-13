from bs4 import BeautifulSoup as soup
from urllib2 import urlopen as ureq
import urllib2
import re
import pandas as pd
from bs4 import BeautifulSoup as soup
######################################################################################################

def check(container):
    for j in range(len(container)):
        try:
            if container[j]['class'][0] == 'post':
                # print('Yo')
                return 1
        except:
            continue
    # print('lol')
    return 0

###########################################################################################################
def function(url, df):
    #Input URL of the webpage you want to scrap
    my_url = url
    
    #Downloading the webpage
    req = urllib2.Request(my_url, headers={'User-Agent' : "Magic Browser"}) 
    con = urllib2.urlopen( req )
    pagehtml = con.read()
    
    #Using the BeautifulSoup for scrapping
    pagesoup = soup(pagehtml, "html.parser")
    
    #Save all the div with class:item-container
    containers3 = pagesoup.find_all('form', {'id':'quickModForm'})
    container4 = containers3[0].find_all('tr')
    
    n = df.shape[0] 
    for j in range(0,len(container4)):
        df.loc[n] = '-1'
        try:
            cl = container4[j]['class']
            # print j
            cont6 = container4[j].find_all('a', {'class':'message_number'})
            comment_number = cont6[0].text
            df.loc[n][0] = comment_number
            container5 = container4[j].find_all('div')
            flag= 0 
            for i in range(0, len(container5)):
                if check(container5):
                    try:
                        if str(container5[i]['class'][0]) == 'smalltext':
                            date = container5[i].text
                            #print k
                            if flag == 0: 
                                #print('Name:'+date)
                                Activity = container5[i].span.next_sibling.next_sibling.next_sibling
                                Activity = Activity.replace('\t','')
                                Activity = Activity.replace('\n','')
                                Merit = container5[i].span.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
                                Merit = Merit.replace('\t','')
                                Merit = Merit.replace('\n','')
                                try:
                                    Activity = re.findall('Activity: ([0-9]*)', Activity)
                                    Activity = int(Activity[0])
                                    df.loc[n][2] = Activity
                                    Merit = re.findall('Merit: ([0-9]*)', Merit)
                                    Merit = int(Merit[0])
                                    df.loc[n][3] = Merit
                                    df.loc[n][1] = date
                                except:
                                    df.loc[n][2] = '-'
                                    df.loc[n][3] = '-'
                                    df.loc[n][1] = date
                            if flag==1: 
                                #print('Date:'+date)
                                df.loc[n][4] = date
                            flag = 1
                        if str(container5[i]['class'][0]) == 'subject':
                            Subject = container5[i].text
                            df.loc[n][5] = Subject
                        if str(container5[i]['class'][0]) == 'post':
                            try:
                                if str(container5[i].div['class'][0]) == 'quoteheader':
                                    # #print('Yo')
                                    Quoteheader = container5[i].div.text
                                    df.loc[n][7] = Quoteheader
                                    container5[i].div.decompose()
                                    Quote = container5[i].div.text
                                    df.loc[n][6] = Quote
                                    container5[i].div.decompose()
                                    post = container5[i].text
                                    df.loc[n][8] = post
                                    #print post
                            except:
                                post = container5[i].text
                                df.loc[n][8] = post
                                df.loc[n][6] = '-'
                                df.loc[n][7] = '-'
                                #print post
                    except:
                        continue
            # print('yo')
        except:
            continue
        n = n + 1
    return df
######################################################################################################

def scrape(url, df):
    #Input URL of the webpage you want to scrap
    my_url = url
    
    #Downloading the webpage
    req = urllib2.Request(my_url, headers={'User-Agent' : "Magic Browser"}) 
    con = urllib2.urlopen( req )
    pagehtml = con.read()
    
    #Using the BeautifulSoup for scrapping
    pagesoup = soup(pagehtml, "html.parser")
    
    #Save all the div with class:item-container
    containers3 = pagesoup.find_all('form', {'id':'quickModForm'})
    container4 = containers3[0].find_all('tr')
    
    n = df.shape[0]
    for j in range(0,len(container4)):
        df.loc[n] = '-1'
        try:
            cl = container4[j]['class']
            # #print j
            cont6 = container4[j].find_all('a', {'class':'message_number'})
            comment_number = cont6[0].text
            df.loc[n][0] = comment_number
            container5 = container4[j].find_all('div')
            flag= 0 
            for i in range(0, len(container5)):
                if check(container5):
                    try:
                        if str(container5[i]['class'][0]) == 'smalltext':
                            date = container5[i].text
                            #print k
                            if flag == 0: 
                                #print('Name:'+date)
                                Activity = container5[i].span.next_sibling.next_sibling.next_sibling
                                Activity = Activity.replace('\t','')
                                Activity = Activity.replace('\n','')
                                Merit = container5[i].span.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
                                Merit = Merit.replace('\t','')
                                Merit = Merit.replace('\n','')
                                try:
                                    Activity = re.findall('Activity: ([0-9]*)', Activity)
                                    Activity = int(Activity[0])
                                    df.loc[n][2] = Activity
                                    Merit = re.findall('Merit: ([0-9]*)', Merit)
                                    Merit = int(Merit[0])
                                    df.loc[n][3] = Merit
                                    df.loc[n][1] = date
                                except:
                                    df.loc[n][2] = '-'
                                    df.loc[n][3] = '-'
                                    df.loc[n][1] = date
                            if flag==1: 
                                #print('Date:'+date)
                                df.loc[n][4] = date
                            flag = 1
                        if str(container5[i]['class'][0]) == 'subject':
                            Subject = container5[i].text
                            df.loc[n][5] = Subject
                        if str(container5[i]['class'][0]) == 'post':
                            try:
                                if str(container5[i].div['class'][0]) == 'quoteheader':
                                    # #print('Yo')
                                    Quoteheader = container5[i].div.text
                                    df.loc[n][7] = Quoteheader
                                    container5[i].div.decompose()
                                    Quote = container5[i].div.text
                                    df.loc[n][6] = Quote
                                    container5[i].div.decompose()
                                    post = container5[i].text
                                    df.loc[n][8] = post
                                    #print post
                            except:
                                post = container5[i].text
                                df.loc[n][8] = post
                                df.loc[n][6] = '-'
                                df.loc[n][7] = '-'
                                #print post
                    except:
                        continue
            # print('yo')
        except:
            continue
        n = n + 1
    
    p = 1
    cont7 = pagesoup.find_all('a', {'class':'navPages'})
    for i in range(len(cont7)):
        try:
            if int(cont7[i].text) > p:
                df = function(cont7[i]['href'], df)
                p = p + 1 
        except:
            continue
    return df    
#########################################################################################

#Input URL of the webpage you want to scrap
my_url = 'https://bitcointalk.org/index.php?board=1.0'

#Downloading the webpage
req = urllib2.Request(my_url, headers={'User-Agent' : "Magic Browser"}) 
con = urllib2.urlopen( req )
pagehtml = con.read()

#Using the BeautifulSoup for scrapping
pagesoup = soup(pagehtml, "html.parser")

df = pd.DataFrame()
name = []
Date = []
activity = []
merit = []
Comment = []
quote = []
quoteheader = []
comment_no = []
subject = []

df['comment_no'] = comment_no
df['Name'] = name
df['Activity'] = activity
df['Merit'] = merit
df['Date'] = Date
df['Subject'] = subject
df['Quote'] = quote
df['Quoteheader'] = quoteheader
df['Comment'] = Comment

# All the links of topics on a particular page
containers1 = pagesoup.find_all("span", id=re.compile("^msg"))
n = 0

for i in range(len(containers1)):
    df = scrape(str(containers1[i].a['href']), df)
    print(i)
#############################################################################################

# To Remove Ads:
# for i in range(0, df.shape[0]):
#     try:
#         if df.iloc[i,1] == df.iloc[i,2]:
#             df = df.drop(df.index[i])
#     except:
#         continue
 
# Save df in CSV format
df.to_csv('bitcoindiscussion.csv',sep=',',encoding='utf-8')



 

