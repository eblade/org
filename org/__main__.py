#!/usr/bin/env python3

import os
import bottle
from samtt import init

from . import web
from . import card


WEB = 'web'
JS = os.path.join(WEB, 'js')
CSS = os.path.join(WEB, 'css')


if __name__ == '__main__':
    db = init('sqlite:////tmp/test.sqlite')
    db.create_all()

    app = bottle.Bottle()

    # Static files
    app.route('/', 'GET',
              lambda: bottle.static_file('index.html', root=WEB))
    app.route('/js/<fn>.js', 'GET',
              lambda fn: bottle.static_file(fn + '.js', root=JS))
    app.route('/css/<fn>.css', 'GET',
              lambda fn: bottle.static_file(fn + '.css', root=CSS))

    # Cards
    app.route('/card', 'POST',
              web.create(card.create_card, card.Card))
    app.route('/card/<id:int>', 'GET',
              web.fetch(card.get_card_by_id))

    bottle.debug()
    app.run(hostname='localhost', port=8080)
