# -*- coding: utf-8 -*-
from application import app
from route.api import *


def main():
    app.run(host='0.0.0.0', port=app.config.get('API_SERVER_PORT'), debug=True)


if __name__ == '__main__':
    try:
        import sys
        sys.exit(main())
    except Exception as e:
        app.logger.info(e)
