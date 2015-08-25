#!/usr/bin/python
# -*- coding: utf-8 -*-

import gettext 
import os.path


current_dir = os.path.dirname(os.path.abspath(__file__))
gettext.install('example', localedir=current_dir)


print(_('Yo'))
print(_('Hello!'))
print(_('World!'))
print(_('Baby'))
