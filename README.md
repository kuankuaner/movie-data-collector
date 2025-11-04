# movie-data-collector
English A Python-based web scraper that automatically collects data from Douban Movie Top 250, including movie titles, ratings, number of reviews, and director information. The scraped data is saved as an Excel file for further analysis.  
一个基于 Python 的网页爬虫工具，用于自动采集豆瓣电影 Top 250 的数据，包括电影名称、评分、评价人数和导演信息。采集结果将保存为 Excel 文件，便于后续分析与使用。
markdown

# movie-data-collector 🎬
这是一个用于爬取豆瓣电影 Top 250 榜单数据的 Python 脚本。通过模拟浏览器请求，自动抓取每部电影的**名称、评分、评价人数和导演信息**，并将结果保存为 Excel 文件。

 主要功能
- 📊 自动翻页抓取全部 250 部电影数据
- 🎯 提取电影名称、评分、评价人数、导演信息
- 💾 数据自动保存为 Excel 格式
- ⏱️ 设置请求间隔，避免被封 IP
  安装使用
1. 克隆项目：
```bash
git clone https://github.com/your-username/douban-movie-scraper.git
cd douban-movie-scraper
```
2、安装依赖：
```bash
pip install requests beautifulsoup4 pandas openpyxl
```
3、运行脚本：
```bash
python ds.py
```
4、查看生成的 豆瓣电影Top250数据.xlsx 文件

技术栈
Python - 编程语言
Requests - HTTP 请求库
BeautifulSoup - HTML 解析库
Pandas - 数据处理和 Excel 导出

数据字段
字段名	描述	示例
电影名称	电影的中文名称	肖申克的救赎
评分	豆瓣评分	9.7
评价人数	参与评分的人数	2843856
导演	电影导演	弗兰克·德拉邦特

注意事项
请遵守豆瓣网站的 robots.txt 协议
仅用于学习和研究，请勿用于商业用途
合理设置请求间隔，避免对服务器造成压力


# movie-data-collector 🎬
Project Description
A Python web scraper that automatically collects data from Douban Movie Top 250, including movie titles, ratings, number of reviews, and director information. The scraped data is exported to Excel for further analysis.

Features
📊 Auto-pagination to scrape all 250 movies

🎯 Extracts movie title, rating, review count, and director

💾 Saves data in Excel format

⏱️ Includes delay between requests to avoid being blocked

 Installation & Usage
1、Clone the repository:

```bash
git clone https://github.com/your-username/douban-movie-scraper.git
cd douban-movie-scraper
```
2、Install dependencies:
```bash
pip install requests beautifulsoup4 pandas openpyxl

```
3、Run the script:
```bash
python ds.py
```
4、Check the generated 豆瓣电影Top250数据.xlsx file

Tech Stack
Python - Programming language
Requests - HTTP library
BeautifulSoup - HTML parsing
Pandas - Data processing and Excel export


Notes
Please comply with Douban's robots.txt
For learning and research purposes only
Set reasonable request intervals to avoid overloading the server
