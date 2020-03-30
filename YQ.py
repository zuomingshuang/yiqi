import requests
import pandas as pd

def get_html():
    url='https://ncov-cdn.sndo.com/quarantine/getQuarantineAll.djson'
    data={'2020-02-19-17-10':''}
    res=requests.get(url=url,params=data)
    html=res.json()
    return html

def html_parse():
    html=get_html()
    datas=html['data']
    for data in datas:
        p = data.get('p')   #省份
        c =data.get('c')    #城市
        d = data.get('d')   #区
        a = data.get('a')   #小区
        tn = data.get('tN')    #确诊人数
        print(p+c+d+a+str(tn)+'例')
        data_dict['省份'].append(p)
        data_dict['城市'].append(c)
        data_dict['区'].append(d)
        data_dict['小区'].append(a)
        data_dict['确诊人数'].append(tn)


if __name__=='__main__':
    data_dict={
        '省份':[],
        '城市': [],
        '区': [],
        '小区': [],
        '确诊人数': [],
    }
    html_parse()
    pd.DataFrame(data_dict).to_excel('全国疫情数据.xlsx',index=False)