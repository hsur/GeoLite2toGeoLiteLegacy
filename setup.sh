#!/bin/bash

pip install ipaddr pygeoip ipaddress

if [ ! -f csv2dat.py ] ; then
  wget -O csv2dat.py "https://raw.githubusercontent.com/mteodoro/mmutils/master/csv2dat.py"
  patch <<EOF
--- csv2dat.py  2018-07-21 23:42:57.676684062 +0900
+++ csv2dat.py.new      2018-07-21 22:49:21.408238918 +0900
@@ -21,6 +21,8 @@
 cc_idx['uk'] = cc_idx['gb'] #uk / great britain
 cc_idx['sx'] = cc_idx['fx'] #st. martin?

+cc_idx['xk'] = cc_idx['rs'] #Kosovo
+
 def init_logger(opts):
     level = logging.INFO
     handler = logging.StreamHandler()
EOF

fi
