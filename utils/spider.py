import os
import os.path as osp
import sys
import json
import time
import datetime
from bs4 import BeautifulSoup
import random
from selenium import webdriver
from utils.tools import mkdir_if_missing, write_json, read_json
from datetime import timedelta
class spider():

    def __init__(self,uid,save_dir_json='json',save_by_page=False,t=1):
        self.t = t
        self.uid = uid
        self.user_url = 'https://space.bilibili.com/{}'.format(uid)
        self.save_dir_json = save_dir_json
        self.save_by_page = save_by_page
        options = webdriver.EdgeOptions()
        options.add_argument('--headless')
        self.browser = webdriver.Edge(options=options)
        print('spider init done.')

    def close(self):
        # 关闭浏览器驱动
        self.browser.quit()

    def setcookie(self):

        url = "https://www.bilibili.com/"
        self.browser.get(url)

        cookie_data = [
            {
                "domain": ".bilibili.com",
                "expirationDate": 1741618313,
                "hostOnly": False,
                "httpOnly": False,
                "name": "_uuid",
                "path": "/",
                "sameSite": "None",
                "secure": False,
                "session": False,
                "storeId": "0",
                "value": "A31BFE84-10FB1-DAE8-8112-E43B5101095F8613107infoc"
            },
            {
                "domain": ".bilibili.com",
                "hostOnly": False,
                "httpOnly": False,
                "name": "b_lsid",
                "path": "/",
                "sameSite": "None",
                "secure": False,
                "session": True,
                "storeId": "0",
                "value": "FE4104D61_18E466DBA55"
            },
            {
                "domain": ".bilibili.com",
                "expirationDate": 1741618312.745431,
                "hostOnly": False,
                "httpOnly": False,
                "name": "b_nut",
                "path": "/",
                "sameSite": "None",
                "secure": False,
                "session": False,
                "storeId": "0",
                "value": "100"
            },
            {
                "domain": ".bilibili.com",
                "expirationDate": 1726130635.278878,
                "hostOnly": False,
                "httpOnly": False,
                "name": "bili_jct",
                "path": "/",
                "sameSite": "None",
                "secure": False,
                "session": False,
                "storeId": "0",
                "value": "553c789cfb923b271ad98cd0fe6c0601"
            },
            {
                "domain": ".bilibili.com",
                "expirationDate": 1742114580,
                "hostOnly": False,
                "httpOnly": False,
                "name": "browser_resolution",
                "path": "/",
                "sameSite": "None",
                "secure": False,
                "session": False,
                "storeId": "0",
                "value": "1536-718"
            },
            {
                "domain": ".bilibili.com",
                "hostOnly": False,
                "httpOnly": False,
                "name": "bsource",
                "path": "/",
                "sameSite": "None",
                "secure": False,
                "session": True,
                "storeId": "0",
                "value": "search_google"
            },
            {
                "domain": ".bilibili.com",
                "expirationDate": 1711342773.671319,
                "hostOnly": False,
                "httpOnly": False,
                "name": "buvid_fp",
                "path": "/",
                "sameSite": "None",
                "secure": False,
                "session": False,
                "storeId": "0",
                "value": "781503f1332bc75bb10a715156ec9eec"
            },
            {
                "domain": ".bilibili.com",
                "expirationDate": 1711342772.869384,
                "hostOnly": False,
                "httpOnly": False,
                "name": "buvid3",
                "path": "/",
                "sameSite": "None",
                "secure": False,
                "session": False,
                "storeId": "0",
                "value": "23B0F8A1-EB89-4057-249F-52A455CA812772717infoc"
            },
            {
                "domain": ".bilibili.com",
                "expirationDate": 1729163450.407238,
                "hostOnly": False,
                "httpOnly": False,
                "name": "buvid4",
                "path": "/",
                "sameSite": "None",
                "secure": False,
                "session": False,
                "storeId": "0",
                "value": "FE063E01-C3EF-1D79-0CEA-212E5C4247C573616-023021912-DLQaI8fO0w9Wm8Ce%2FpHEmg%3D%3D"
            },
            {
                "domain": ".bilibili.com",
                "expirationDate": 1741702313,
                "hostOnly": False,
                "httpOnly": False,
                "name": "CURRENT_FNVAL",
                "path": "/",
                "sameSite": "None",
                "secure": False,
                "session": False,
                "storeId": "0",
                "value": "4048"
            },
            {
                "domain": ".bilibili.com",
                "expirationDate": 1726139481,
                "hostOnly": False,
                "httpOnly": False,
                "name": "CURRENT_QUALITY",
                "path": "/",
                "sameSite": "None",
                "secure": False,
                "session": False,
                "storeId": "0",
                "value": "80"
            },
            {
                "domain": ".bilibili.com",
                "expirationDate": 1726130635.278901,
                "hostOnly": False,
                "httpOnly": False,
                "name": "DedeUserID",
                "path": "/",
                "sameSite": "None",
                "secure": False,
                "session": False,
                "storeId": "0",
                "value": "24885965"
            },
            {
                "domain": ".bilibili.com",
                "expirationDate": 1726130635.278919,
                "hostOnly": False,
                "httpOnly": False,
                "name": "DedeUserID__ckMd5",
                "path": "/",
                "sameSite": "None",
                "secure": False,
                "session": False,
                "storeId": "0",
                "value": "d3c909fae5066dae"
            },
            {
                "domain": ".bilibili.com",
                "expirationDate": 1742114580,
                "hostOnly": False,
                "httpOnly": False,
                "name": "enable_web_push",
                "path": "/",
                "sameSite": "None",
                "secure": False,
                "session": False,
                "storeId": "0",
                "value": "DISABLE"
            },
            {
                "domain": ".bilibili.com",
                "expirationDate": 1742114580,
                "hostOnly": False,
                "httpOnly": False,
                "name": "FEED_LIVE_VERSION",
                "path": "/",
                "sameSite": "None",
                "secure": False,
                "session": False,
                "storeId": "0",
                "value": "V8"
            },
            {
                "domain": ".bilibili.com",
                "expirationDate": 1742114580,
                "hostOnly": False,
                "httpOnly": False,
                "name": "header_theme_version",
                "path": "/",
                "sameSite": "None",
                "secure": False,
                "session": False,
                "storeId": "0",
                "value": "CLOSE"
            },
            {
                "domain": ".bilibili.com",
                "expirationDate": 1742114580,
                "hostOnly": False,
                "httpOnly": False,
                "name": "home_feed_column",
                "path": "/",
                "sameSite": "None",
                "secure": False,
                "session": False,
                "storeId": "0",
                "value": "5"
            },
            {
                "domain": ".bilibili.com",
                "expirationDate": 1744643020.198977,
                "hostOnly": False,
                "httpOnly": False,
                "name": "PVID",
                "path": "/",
                "sameSite": "None",
                "secure": False,
                "session": False,
                "storeId": "0",
                "value": "1"
            },
            {
                "domain": ".bilibili.com",
                "expirationDate": 1711342774.169516,
                "hostOnly": False,
                "httpOnly": False,
                "name": "rpdid",
                "path": "/",
                "sameSite": "None",
                "secure": False,
                "session": False,
                "storeId": "0",
                "value": "|(J~lkk|JkYY0J'uY~Y~)k~~J"
            },
            {
                "domain": ".bilibili.com",
                "expirationDate": 1726130635.278804,
                "hostOnly": False,
                "httpOnly": True,
                "name": "SESSDATA",
                "path": "/",
                "sameSite": "None",
                "secure": True,
                "session": False,
                "storeId": "0",
                "value": "982fd7d7%2C1726130633%2C993e9%2A32CjBAumLShTGUmc7lgLo87BrdIxfYoL99P1BXN7z4ufL1hpEK1kaVxl9y56BHL9jgesoSVkVteVBObHB6SGsyZ2dtNGRRblZKT1FzWTlhREllRm1YaXRoSldrTW9hMHlBWFFfaUk2a1Vhb3lubkQ3N3RWUXJSRW9fQkwwckRaMU5RLXJxWEhLUWZRIIEC"
            },
            {
                "domain": ".bilibili.com",
                "expirationDate": 1726130635.278937,
                "hostOnly": False,
                "httpOnly": False,
                "name": "sid",
                "path": "/",
                "sameSite": "None",
                "secure": False,
                "session": False,
                "storeId": "0",
                "value": "f6lkr6pv"
            },
            {
                "domain": "www.bilibili.com",
                "hostOnly": True,
                "httpOnly": False,
                "name": "bmg_af_switch",
                "path": "/",
                "sameSite": "None",
                "secure": False,
                "session": True,
                "storeId": "0",
                "value": "1"
            },
            {
                "domain": "www.bilibili.com",
                "hostOnly": True,
                "httpOnly": False,
                "name": "bmg_src_def_domain",
                "path": "/",
                "sameSite": "None",
                "secure": False,
                "session": True,
                "storeId": "0",
                "value": "i0.hdslb.com"
            }
        ]

        # 添加cookie
        for cookie in cookie_data:
            self.browser.add_cookie(cookie)
        page_url = self.user_url + '/video?tid=0&page={}&keyword=&order=pubdate'.format(1)
        self.browser.get(page_url)

    def time_convert(self, time_str):
        time_item = time_str.split(':')
        if len(time_item) == 2:  # 分钟:秒形式
            minutes = int(time_item[0])
            seconds = int(time_item[1])
            total_seconds = minutes * 60 + seconds
        elif len(time_item) == 3:  # 小时:分钟:秒形式
            hours = int(time_item[0])
            minutes = int(time_item[1])
            seconds = int(time_item[2])
            total_seconds = hours * 3600 + minutes * 60 + seconds
        else:
            raise ValueError('time format error: {}, x:x or x:x:x expected!'.format(time_str))
        return total_seconds

    def date_convert(self, date_str):
        date_item = date_str.split('-')
        if '小时前' in date_str:
            # 如果包含小时前，直接记录当天时间
            current_time = datetime.datetime.now()
            date_str = current_time.strftime('%Y-%m-%d')  # 返回当天时间的字符串表示形式，仅包含日期
            return date_str
        if '分钟前' in date_str:
            # 如果包含小时前，直接记录当天时间
            current_time = datetime.datetime.now()
            date_str = current_time.strftime('%Y-%m-%d')  # 返回当天时间的字符串表示形式，仅包含日期
            return date_str
        if '昨天' in date_str:
            current_date = datetime.datetime.now()
            # 计算昨天的日期
            yesterday_date = current_date - timedelta(days=1)
            # 将日期格式化为YYYY-MM-DD形式的字符串
            date_str = yesterday_date.strftime('%Y-%m-%d')
            return  date_str
        assert len(date_item) == 2 or len(date_item) == 3, 'date format error: {}, x-x or x-x-x expected!'.format(date_str)
        if len(date_item) == 2:
            year = datetime.datetime.now().strftime('%Y')
            date_str = '{}-{:>02d}-{:>02d}'.format(year, int(date_item[0]), int(date_item[1]))
        else:
            date_str = '{}-{:>02d}-{:>02d}'.format(date_item[0], int(date_item[1]), int(date_item[2]))
        return date_str

    def get_page_num(self):
        page_url = self.user_url + '/video?tid=0&page={}&keyword=&order=pubdate'.format(1)
        self.browser.get(page_url)
        time.sleep(self.t + 2 * random.random())
        html = BeautifulSoup(self.browser.page_source, features="html.parser")
        page_number = html.find('span', attrs={'class': 'be-pager-total'}).text
        user_name = html.find('span', id='h-name').text
        print(page_number)
        return int(page_number.split(' ')[1]), user_name

    def get_videos_by_page(self, idx):
        # 获取第 page_idx 页的视频信息
        urls_page, titles_page, plays_page, dates_page, durations_page,bvs_page = [], [], [], [], [],[]
        page_url = self.user_url + '/video?tid=0&pn={}&keyword=&order=pubdate'.format(idx + 1)
        self.browser.get(page_url)
        time.sleep(self.t + 2 * random.random())
        html = BeautifulSoup(self.browser.page_source, features="html.parser")
        ul_data = html.find('div', id='submit-video-list').find('ul', attrs={'class': 'clearfix cube-list'})

        for li in ul_data.find_all('li'):
            # url & title
            a = li.find('a', attrs={'target': '_blank', 'class': 'title'})
            a_url = 'https:{}'.format(a['href'])
            a_title = a.text
            # pub_date & play
            date_str = li.find('span', attrs={'class': 'time'}).text.strip()
            pub_date = self.date_convert(date_str)
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            play_text = li.find('span', attrs={'class': 'play'}).text.strip()
            if '万' in play_text:
                play_text = play_text.replace('万', '')  # 去除 '万'
                play = int(float(play_text) * 10000)  # 将数字转换为整数，并乘以 10000
            else:
                play = int(play_text)  # 没有单位时直接转换为整数
            # duration
            time_str = li.find('span', attrs={'class': 'length'}).text
            duration = self.time_convert(time_str)
            # append
            urls_page.append(a_url)
            titles_page.append(a_title)
            dates_page.append((pub_date, now))
            plays_page.append(play)
            durations_page.append(duration)

        return urls_page, titles_page, plays_page, dates_page, durations_page

    def save(self, json_path, bvs, urls, titles, plays, durations, dates):
        data_list = []
        for i in range(len(urls)):
            result = {}
            result['user_name'] = self.user_name
            result['bv'] = bvs[i]
            result['url'] = urls[i]
            result['title'] = titles[i]
            result['play'] = plays[i]
            result['duration'] = durations[i]
            result['pub_date'] = dates[i][0]
            result['now'] = dates[i][1]
            data_list.append(result)

        print('write json to {}'.format(json_path))
        dir_name = osp.dirname(json_path)
        mkdir_if_missing(dir_name)
        write_json(data_list, json_path)
        print(data_list)
        print('dump json file done. total {} urls. \n'.format(len(urls)))

    def get(self):
        # 获取该 up 主的所有基础视频信息
        print('Start ... \n')
        self.setcookie()
        self.page_num, self.user_name = self.get_page_num()
        while self.page_num == 0:
            print('Failed to get user page num, poor network condition, retrying ... ')
            self.page_num, self.user_name = self.get_page_num()
        print('Pages Num {}, User Name: {}'.format(self.page_num, self.user_name))

        bvs = []
        urls = []
        titles = []
        plays = []
        dates = []
        durations = []   # by seconds

        for idx in range(self.page_num):
            print('>>>> page {}/{}'.format(idx+1, self.page_num))
            urls_page, titles_page, plays_page, dates_page, durations_page = self.get_videos_by_page(idx)
            while len(urls_page) == 0:
                print('failed, try again page {}/{}'.format(idx+1, self.page_num))
                urls_page, titles_page, plays_page, dates_page, durations_page = self.get_videos_by_page(idx)
            bvs_page = [x.split('/')[-2] for x in urls_page]
            print(bvs_page)
            assert len(urls_page) == len(titles_page), '{} != {}'.format(len(urls_page), len(titles_page))
            assert len(urls_page) == len(plays_page), '{} != {}'.format(len(urls_page), len(titles_page))
            assert len(urls_page) == len(dates_page), '{} != {}'.format(len(urls_page), len(dates_page))
            assert len(urls_page) == len(durations_page), '{} != {}'.format(len(urls_page), len(durations_page))
            print('result:')
            print('{}_{}: '.format(self.user_name, self.uid), bvs_page, ', {} in total'.format(len(urls_page)))
            sys.stdout.flush()
            bvs.extend(bvs_page)
            urls.extend(urls_page)
            titles.extend(titles_page)
            plays.extend(plays_page)
            dates.extend(dates_page)
            durations.extend(durations_page)
            if self.save_by_page:
                json_path_page = osp.join(self.save_dir_json, '{}_{}'.format(self.user_name, self.uid), 'primary', 'page_{}.json'.format(idx+1))
                self.save(json_path_page, bvs_page, urls_page, titles_page, plays_page, durations_page, dates_page)

        json_path = osp.join(self.save_dir_json, '{}_{}'.format(self.user_name, self.uid), 'primary', 'full.json')
        self.save(json_path, bvs, urls, titles, plays, durations, dates)

    def get_url(self, url):
        self.browser.get(url)
        time.sleep(self.t + 2 * random.random())
        html = BeautifulSoup(self.browser.page_source, features="html.parser")

        video_data = html.find('div', id='viewbox_report').find_all('span')
        play = int(video_data[1]['title'][4:])
        danmu = int(video_data[2]['title'][7:])
        date = video_data[3].text

        multi_page = html.find('div', id='multi_page')
        if multi_page is not None:
            url_type = 'playlist'
            pages = multi_page.find('span', attrs={'class': 'cur-page'}).text
            page_total = int(pages.split('/')[-1])
        else:
            url_type = 'video'
            page_total = 1

        return play, danmu, date, url_type, page_total

    def get_detail(self):
        print('Start to get detailed information for each url.')
        if self.save_by_page:
            data = []
            for idx in range(self.page_num):
                json_path = osp.join(self.save_dir_json, '{}_{}'.format(self.user_name, self.uid), 'primary',
                                     'page_{}.json'.format(idx + 1))
                data_page = read_json(json_path)
                for j, item in enumerate(data_page):
                    url = item['url']
                    print('>>>> page {}/{}, No. {}/{}'.format(idx + 1, self.page_num, j + 1, len(data_page)))
                    play, danmu, date, url_type, page_total = self.get_url(url)
                    # print(play, danmu, date, url_type, page_total)
                    assert page_total > 0, page_total
                    if page_total == 1:
                        assert url_type == 'video', (url_type, page_total)
                        data_page[j]['play'] = play
                        data_page[j]['danmu'] = danmu
                        data_page[j]['pub_date'] = date
                        data_page[j]['type'] = url_type
                        data_page[j]['num'] = page_total
                    else:
                        assert url_type == 'playlist', (url_type, page_total)
                        data_page[j]['play'] = play
                        data_page[j]['danmu'] = danmu
                        data_page[j]['pub_date'] = date
                        data_page[j]['type'] = url_type
                        data_page[j]['num'] = page_total

                json_path_save = osp.join(self.save_dir_json, '{}_{}'.format(self.user_name, self.uid), 'detailed',
                                          'page_{}.json'.format(idx + 1))
                print('write json to {}'.format(json_path_save))
                write_json(data_page, json_path_save)
                print('dump json file done. total {} urls. \n'.format(len(data_page)))
                data.extend(data_page)

            json_path_save = osp.join(self.save_dir_json, '{}_{}'.format(self.user_name, self.uid), 'detailed',
                                      'full.json')
            print('write json to {}'.format(json_path_save))
            write_json(data, json_path_save)
            print('dump json file done. total {} urls. \n'.format(len(data)))
        else:
            json_path = osp.join(self.save_dir_json, '{}_{}'.format(self.user_name, self.uid), 'primary', 'full.json')
            data = read_json(json_path)
            for j, item in enumerate(data):
                url = item['url']
                print('>>>> No. {}/{}'.format(j + 1, len(data)))
                play, danmu, date, url_type, page_total = self.get_url(url)
                assert page_total > 0, page_total
                if page_total == 1:
                    assert url_type == 'video', (url_type, page_total)
                    data[j]['play'] = play
                    data[j]['danmu'] = danmu
                    data[j]['pub_date'] = date
                    data[j]['type'] = url_type
                    data[j]['num'] = page_total
                else:
                    assert url_type == 'playlist', (url_type, page_total)
                    data[j]['play'] = play
                    data[j]['danmu'] = danmu
                    data[j]['pub_date'] = date
                    data[j]['type'] = url_type
                    data[j]['num'] = page_total

            json_path_save = osp.join(self.save_dir_json, '{}_{}'.format(self.user_name, self.uid), 'detailed',
                                      'full.json')
            print('write json to {}'.format(json_path_save))
            write_json(data, json_path_save)
            print('dump json file done. total {} urls. \n'.format(len(data)))

    def read_json_data(self):
        json_path = os.path.join(self.save_dir_json, '{}_{}'.format(self.user_name, self.uid), 'primary', 'full.json')
        if os.path.exists(json_path):
            with open(json_path, 'r', encoding='utf-8-sig') as f:
                json_data = json.load(f)
            return json_data
        else:
            return {'error': 'JSON file not found'}