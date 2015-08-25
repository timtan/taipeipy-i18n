# -*- coding: utf-8 -*-
#!/usr/bin/python

import gettext 
import os.path

current_dir = os.path.dirname(os.path.abspath(__file__))

gettext.install('example', localedir=current_dir)

print( _('Hello!')) 
print( _('World!')) 
