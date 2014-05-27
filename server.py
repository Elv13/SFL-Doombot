#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)

def print_header():
   return "<pre>\
#                                   --SFL--                                  #\n\
#        /¯¯¯¯\  /¯¯¯¯\ /¯¯¯¯\  /¯¯¯\_/¯¯¯\   /¯¯¯¯¯\  /¯¯¯¯\ |¯¯¯¯¯¯¯|      #\n\
#       / /¯\ | /  /\  \  /\  \| /¯\  /¯\  |  | |¯| | |  /\  | ¯¯| |¯¯       #\n\
#      / /  / |/  | |  | | |  || |  | |  | |  |  ¯ <  |  | | |   | |         #\n\
#     / /__/ / |   ¯   |  ¯   || |  | |  | |  | |¯| | |  |_| |   | |         #\n\
#    |______/   \_____/ \____/ |_|  |_|  |_|  \_____/  \____/    |_|         #\n\
#                                                                            #\n\
# copyright:   Savoir-Faire Linux (2012)                                     #\n\
# author:      Emmanuel Lepage Vallee <emmanuel.lepage@savoirfairelinux.com> #\n\
# description: This script perform stress tests to trigger rare race         #\n\
#               conditions or ASSERT caused by excessive load. This script   #\n\
#               should, in theory, never crash or end the sflphone daemon    #\n\
<pre>"

@app.route("/")
def hello():
    return print_header()

if __name__ == "__main__":
    app.run()
