import time
import pandas as pd
from bs4 import BeautifulSoup
import requests
from multiprocessing import Pool,current_process
def scraper(args):
    url,index=args
    try:
        response=requests.get(url)
        if response.status_code==200:
            soup=BeautifulSoup(response.content,'html.parser')
            price=soup.find('span',{'itemprop':'price'}).get_text().strip()
            if price:
                print(f"Scraped : {url},  price: {price}")
                return index, price
            else:
                return index, 'No Price Found'
        else:
            print(f"failed to retrieve data from url: {url}")
            print("status code: ", response.status_code)
            return index, None
    except Exception as e:
        print(f'Error accessing {url}: {e}')
        return index, None
def scrape_urls(urls):
    url_with_indices=[(url,i) for i,url in enumerate(urls)]
    with Pool(processes=10) as pool:
        results=pool.map(scraper,url_with_indices)
    return results
def extracting_and_saving(csv):
    df1=pd.read_csv(csv)
    base_url="https://www.abelandcole.co.uk"
    urls=[base_url+href for href in df1['hrefs']]
    start_time=time.time()
    results=scrape_urls(urls)

    today=pd.to_datetime('today').strftime('%Y-%m-%d')
    column_name=f'price_at{today}'

    #check if the column of date already exist
    if column_name not in df1.columns:
        df1[column_name]=None

    for index,price in results:
        df1.at[index,column_name]=price

    final_df = pd.read_csv(csv)
    data = pd.concat((final_df, df1[column_name]), axis=1)
    data.to_csv(csv,index=False)
    print(f"length of results : {len(results)}")
    print(f"length of column name: {len(df1[column_name])}")
    print(f"length of data[column_name] : {len(data[column_name])}")


    end_time=time.time()
    print(f"execution time: {end_time - start_time} seconds")
if __name__ =='__main__':
    extracting_and_saving('aben_and_cole_url_title_all_urls.csv')