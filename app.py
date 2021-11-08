import sqlite3
import requests
from bs4 import BeautifulSoup

c = sqlite3.connect("web-label.db")
session = requests.Session()

def crawl_label(label_input):
    url = "https://www.familug.org/search/label/"
    c.execute("CREATE TABLE {} (name TEXT, url TEXT);".format(label_input))
    res = session.get(url + label_input)
    html_soup = BeautifulSoup(res.text,"html.parser")
    title_link_container_ = html_soup.find_all('div', class_ = 'post hentry')
    title = [name.h3.a.text for name in title_link_container_]
    links = [data.h3.a['href'] for data in title_link_container_]
    data = list(zip(title,links))
    for label in data:
        c.execute("INSERT INTO {} VALUES (?,?)".format(label_input),label)
        c.commit()

def crawl_10_home(input_number):
    url = "https://www.familug.org/search?updated-max=2021-04-14T22:15:00%2B07:00&max-results={}".format(input_number)
    res = session.get(url)
    c.execute("CREATE TABLE Home (name TEXT, url TEXT);")
    html_soup_Home = BeautifulSoup(res.text,"html.parser")
    title_container_home = html_soup_Home.find_all('div', class_ = 'post hentry')
    title_home = [name.h3.a.text for name in title_container_home]
    links_home = [data.h3.a['href'] for data in title_container_home]
    data_Home = list(zip(title_home,links_home))
    for label in data_Home:
        c.execute("INSERT INTO Home VALUES (?,?)",label)
        c.commit()

def main():
    lst = ["Python", "Command", "sysadmin"]
    for i in lst:
        crawl_label(i)
    number = "10"
    crawl_10_home(number)

if __name__ == "__main__":
    main()