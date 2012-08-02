# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################

def index():
    return dict()

def data():
    word_id = db.word.id
    word_word = db.word.word
    id = db().select(word_id, orderby='<random>', limitby=(0,1))
    id = id[0].id
    word = db(word_id == id).select(word_word)
    word = word[0].word
    return TABLE(*[TR(word)]).xml()


