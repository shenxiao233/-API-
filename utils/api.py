import argparse
from flask import Flask, jsonify, request
from utils.start import main

app = Flask(__name__)


@app.route('/api/crawl', methods=['GET'])
def crawl():
    uid = request.args.get('uid')
    if not uid:
        return jsonify({'error': 'Missing uid parameter'}), 400
    args = {
        'uid': uid,
        'save_dir': 'json',
        'save_by_page': False,
        'time': 1,
        'detailed': False
    }

    args_namespace = argparse.Namespace(**args)

    json_data = main(args_namespace)  # 调用 main 函数
    # 返回爬取结果
    return jsonify(json_data)

if __name__ == '__main__':
    app.run(debug=True)
