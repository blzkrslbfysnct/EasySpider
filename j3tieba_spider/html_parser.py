from bs4 import BeautifulSoup
import re
import urllib.parse as urlparse
class HtmlParser(object):

    def _get_new_data(self, page_url, soup):
        res_data = {}
        res_data['url'] = page_url
        ##关键词
        #<title>云音乐飙升榜 - 排行榜 - 网易云音乐</title>
        ###网易云不会爬  有ifream页面    改为爬贴吧
        ######li为贴吧列表
        title_node = soup.findAll('li',class_=" j_thread_list clearfix")##不能直接找最里面的 退而求其次
        # print(title_node)
        tits = []
        for tit in title_node:
            #https://tieba.baidu.com
            # print(tit.find('span',class_ = 'tb_icon_author')['title'])
            url = tit.find('a',href = re.compile('/p/\d'))['href']#/p/5364408968
            # print(tit.find('span',class_ = 'threadlist_rep_num center_text').get_text())  #浏览次数
            tits.append({'tit':tit.find('a',href = re.compile('/p/\d')).get_text(),
                         'url':'https://tieba.baidu.com' + url,
                         'name':tit.find('span',class_ = 'tb_icon_author')['title'],
                         'score':tit.find('span',class_ = 'threadlist_rep_num center_text').get_text()})
            # print(tit.find('a',href = re.compile('/p/\d')).get_text())
        res_data['title'] = tits
        # print(res_data['title'])
        #把标题列表以及连接,和加入到了title中

        return res_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        #/#/song?id=512359558 这个爬不成  尴尬
        #//tieba.baidu.com/f?kw=%E5%89%91%E7%BD%913&ie=utf-8&pn=100
        #找到翻页的列表
        links = soup.find_all('a',href = re.compile(r'/f\?kw=%E5%89%91%E7%BD%913&ie=utf-8&pn=\d'))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls


    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont,'html.parser', from_encoding = 'utf-8')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data



