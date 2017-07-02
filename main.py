from flask import Flask, jsonify, Response

from settings import RSS_CHANNELS

app = Flask(__name__)


@app.route('/rss/<channel_name>.xml', methods=['POST', 'GET'])
def rss(channel_name):
    channel = None
    for c in RSS_CHANNELS:
        if c['name'] == channel_name:
            channel = c
    if channel is None:
        return jsonify({'detail': 'channel not found'})

    try:
        with open('cache/%s.xml' % channel_name, 'r', encoding='utf-8') as f:
            atom = f.read()
    except Exception as e:
        print(e)
        return jsonify({'detail': 'channel xml not found'})

    return Response(response=atom, content_type='application/xml')


if __name__ == '__main__':
    app.run(debug=True)
