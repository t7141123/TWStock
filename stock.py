#This tool is to catch Taiwan stock information.
import requests
import pandas as pd

def crawl_Dividend_Report(url, stockNo):
    
    form_data = {
        'encodeURIComponent':1,
        'step':1,
        'firstin':1,
        'off':1,
        'co_id':stockNo,
        'TYPEK':"all"
    }

    r = requests.post(url,form_data)
    html_df = pd.read_html(r.text)[1].fillna("")

    fp = open("stock.txt", "a")
    fp.write(str(html_df)+'/n')
    fp.close()

    return html_df

crawl_Dividend_Report("https://mops.twse.com.tw/mops/web/ajax_t05st09", 2330)

