# -*- coding: utf-8 -*-
import os

tables = {

    'zh_TW.UTF-8': {

        'hello_world': "Hi 世界"

    },

    'en_US.UTF-8': {

        'hello_world': "Hello World "

    },
}

lang = os.getenv('LANG')
table = tables[lang]

print(table['hello_world'])

