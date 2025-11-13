import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import re

movie_list = []
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0"
}#引号要在一行

for i in range(0, 250, 25):#range(起始，终止，步长)，不是[]
    response = requests.get(f"https://movie.douban.com/top250?start={i}&filter=", headers=headers)#要加f，将列表转为字符串
    soup = BeautifulSoup(response.text, 'html.parser') #text属性返回的是字符串形式的响应体，htlm.parser是解析器
    
    items = soup.find_all('div', class_='info')#find_all返回的是列表，所以接着遍历整个电影项列表，找到所有电影项
    
    for item in items:
        # 电影名称
        title_span = item.find('span', class_='title')#找第一个
        movie_name = title_span.text if title_span else "未知"
        
        # 评分
        rating_span = item.find('span', class_='rating_num')
        rating = rating_span.text if rating_span else "0.0"
        
        # 评价人数
        comment_span = item.find_all('span')[-1]  # 评价人数通常是最后一个span
        comment_num = "0"
        for span in item.find_all('span'):
            if '人评价' in span.text:
                comment_num = span.text.replace('人评价', '')#去掉多余的字符
                break
        
        # 导演信息
        info_div = item.find('div', class_='bd')
        director_info = "未知"
        if info_div:
            info_p = info_div.find('p')
            if info_p:
                infos = info_p.get_text(strip=True).split('\n')#分割字符串，返回列表
                if len(infos) > 0:
                    director_line = infos[0]
                    # 使用正则表达式提取导演信息
                    director_match = re.search(r'导演:\s*([^\s]+)', director_line)#search找到一个结果就返回，+是重复一次或多次
                    if director_match:
                        director_info = director_match.group(1)
        
        movie_dict = {
            "电影名称": movie_name,
            "评分": rating,
            "评价人数": comment_num,
            "导演": director_info,
        }
        movie_list.append(movie_dict)
    
    time.sleep(2)  # 防止爬取过快被封ip
    response.close()

def save_to_excel():
    df = pd.DataFrame(movie_list)
    # 确保评价人数是数字类型
    df["评价人数"] = pd.to_numeric(df["评价人数"], errors="coerce").fillna(0).astype(int)
    
    # 保存到Excel文件
    excel_path = "豆瓣电影Top250数据.xlsx"
    df.to_excel(excel_path, index=False, engine="openpyxl")
    print(f"数据已成功保存到：{excel_path}")
    print(f"共爬取到 {len(movie_list)} 部电影数据")

save_to_excel()