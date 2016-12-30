#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import, print_function

import sys
import os
import tempfile, shutil
import re

try:
    from urllib.parse import unquote
except ImportError:
    from urllib import unquote

from epub_utils import epub_zip_up_book_contents





# the plugin entry point
def run(bk):
    for (_id, href) in bk.text_iter():
        html = None
        try:
            html = bk.readfile(_id)
        except Exception as e:
            print(e)
            print("Invalid MANIFEST!")
            print("You may fix content.opf file from you Epub: remove or rename record for:\n%s" % href)
            continue
        #html = text_type(html, 'utf-8')
        imgs = re.findall(r'(<img.*src=\"(\S+)\".*/>)', html)
        if(len(imgs)>0):
            for img,fi in imgs:
                print('-------')
                print(img)
                newnode='<div class="duokan-image-single"><img src="'+fi+'" alt=""/></div>'
                html = html.replace(img, newnode)
                print(newnode)
                print(fi)
                print('-------')
            bk.writefile(_id, html)
                #print(img,fi)
    return 0

def main():
    print("I reached main when I should not have\n")
    return -1

if __name__ == "__main__":
    sys.exit(main())
