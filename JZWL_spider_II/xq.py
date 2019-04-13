import requests
import csv
import json

start_url = "https://xueqiu.com/service/v5/stock/screener/quote/list?page=1&size=1000&order=desc&orderby=percent&order_by=percent&market=US&type=us&_=1555119938562"
headers = {
    "Accept": "*/*",
    "Host": "xueqiu.com",
    "Referer": "https://xueqiu.com/hq",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}

def spider(url, headers):
    rsp = requests.get(url, headers=headers)
    j = json.loads(rsp.content)
    lists = j["data"]["list"]
    csvList = list()
    for i in lists:
        if i["chg"] == None:
            i["chg"] = '-'
        if i['percent'] == None:
            i['percent'] = '-'
        if i['volume'] == None:
            i['volume'] = '-'
        if i['amount'] == None:
            i['amount'] = '-'
        if i['turnover_rate'] == None:
            i['turnover_rate'] = '-'
        if i['dividend_yield'] == None:
            i['dividend_yield'] ='-'
        if i['market_capital'] == None:
            i['market_capital'] = '-'

        csvList.append([i['symbol'], i['name'], i['current'],
                     i['chg'], i['percent'], i['current_year_percent'],
                     i['volume'], i['amount'], i['turnover_rate'],
                     i['pe_ttm'], i['dividend_yield'], i['market_capital']])

    with open("data.csv", 'w') as f:
        c = csv.writer(f, delimiter=' ')
        c.writerow(['股票代码', '股票名称', '当前价',
                    '涨跌额', '涨跌幅', '年初至今',
                    '成交量', '成交额', '换手率',
                    '市盈率(ＴＴＭ)', '股息率', '市值'])
        c.writerows(csvList)




if __name__ == '__main__':
    spider(start_url, headers)