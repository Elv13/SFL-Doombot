#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
import config
app = Flask(__name__)

def print_banner():
   return "<pre>\
##############################################################################\n\
#                                   --SFL--                                  #\n\
#        /¯¯¯¯\  /¯¯¯¯\ /¯¯¯¯\  /¯¯¯\_/¯¯¯\   /¯¯¯¯¯\  /¯¯¯¯\ |¯¯¯¯¯¯¯|      #\n\
#       / /¯\ | /  /\  \  /\  \| /¯\  /¯\  |  | |¯| | |  /\  | ¯¯| |¯¯       #\n\
#      / /  / |/  | |  | | |  || |  | |  | |  |  ¯ <  |  | | |   | |         #\n\
#     / /__/ / |   ¯   |  ¯   || |  | |  | |  | |¯| | |  |_| |   | |         #\n\
#    |______/   \_____/ \____/ |_|  |_|  |_|  \_____/  \____/    |_|         #\n\
#                                   MASTER                                   #\n\
##############################################################################\n\
</pre>"

def print_head(body):
   return "<html><head><title>DoomBot</title></head><body>%s\
<br /><div>Copyright Savoir-faire Linux (2012-2014)</div></body></html>" \
   % body

def print_options():
   return "<table>\n\
      <tr><td>directory </td><td><code>%s</code></td></tr>\n\
      <tr><td>script    </td><td><code>%s</code></td></tr>\n\
      <tr><td>cont      </td><td><code>%s</code></td>/tr>\n\
      <tr><td>command   </td><td><code>%s</code></td></tr>\n\
      </table>" % (str(config.directory), str(config.script and "true" or "false")
                   , str(config.cont and "true" or "false"), str(config.command))

@app.route("/")
def hello():
    return print_head(
       #Print the banner
       print_banner () +
       print_options()
       
       #Print the recent issues
    )

#if __name__ == "__main__":
