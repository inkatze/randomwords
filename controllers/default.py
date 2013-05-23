# -*- coding: utf-8 -*-

def index():
    return dict()

def random():
    row = db(db.word).select(
        db.word.word, orderby='<random>', limitby=(0,1)).first()
    return row.word


