# -*- coding: utf-8 -*-

db = DAL('sqlite://words.db')

db.define_table('word', Field('word', 'string', notnull=True, required=True), migrate=False)
