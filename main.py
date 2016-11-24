import logging

from flask import Flask, request, send_from_directory
from werkzeug.routing import BaseConverter


app = Flask(__name__)


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


app.url_map.converters['regex'] = RegexConverter


@app.route('/')
def render_():
    return send_from_directory('', 'html/index.html')


@app.route('/<regex(".+"):filename>')
def render(filename):
    # return send_from_directory('', filename)
    try:
        # myfilename = str(list(request.args)[0])
        print('html/' + filename)
        return send_from_directory('',  'html/' + filename)
    except:
        # return str(request.args)
        return send_from_directory('', 'html/' + '404.html')


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8081, debug=True)
