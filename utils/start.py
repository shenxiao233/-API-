import os
import os.path as osp
import argparse
from utils.spider import spider


def main(args):
    bilibili_spider = spider(args.uid, args.save_dir, args.save_by_page, args.time)
    bilibili_spider.get()
    data = bilibili_spider.read_json_data()
    return data
    if args.detailed:
       bilibili_spider.get_detail()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--uid', type=str, default='495003013')
    parser.add_argument('--save_dir', type=str, default='json')
    parser.add_argument('--save_by_page', action='store_true', default=False)
    parser.add_argument('--time', type=int, default=2, help='waiting time for browser.get(url) by seconds')
    parser.add_argument('--detailed', action='store_true', default=False)
    args = parser.parse_args()
    print(args)

    main(args)

