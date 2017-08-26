# -*- coding: utf-8 -*-
"""
[root@gd02-zabbix-db-research python_api]# ./app.py --help
usage: app.py [-h] [-t] [-u] [-s SCHEDULER] [-p PERSISTENT] [-r REALSERVER]
              [-f FLOAPINGIP] [-g] [-m] [-S SRCPORT] [-R DESTPORT]

optional arguments:
  -h, --help            show this help message and exit
  -t, --tcp             tcp service
  -u, --udp             udp service
  -s SCHEDULER, --scheduler SCHEDULER
                        one of rr|wrr|lc|wlc|lblc|lblcr|dh|sh|sed|nq,the
                        default scheduler is wlc
  -p PERSISTENT, --persistent PERSISTENT
                        persistent service, default:1500
  -r REALSERVER, --realserver REALSERVER
                        server-address is host (and port) Example: -r '1.1.1.1
                        2.2.2.2 3.3.3.3'
  -f FLOAPINGIP, --floapingip FLOAPINGIP
                        vip address of lvs
  -g, --gatewaying      gatewaying (direct routing)
  -m, --masquerading    masquerading (NAT)
  -S SRCPORT, --srcport SRCPORT
                        listen on floapip port
  -R DESTPORT, --destport DESTPORT
                        listen on realserver port

"""
#!/apps/svr/python/python
# Terry zeng <terry.zeng@xxx.com>
#
#  2014 04 10



import argparse

#### 参数调用说明
parser = argparse.ArgumentParser()
parser.add_argument('-t','--tcp', help='tcp service',action='store_true')
parser.add_argument('-u', '--udp', help='udp service', action='store_true')
parser.add_argument('-s', '--scheduler', help='one of rr|wrr|lc|wlc|lblc|lblcr|dh|sh|sed|nq,the default scheduler is wlc')
parser.add_argument('-p', '--persistent', help='persistent service, default:1500', type = int)
parser.add_argument('-r', '--realserver', help="server-address is host (and port) Example: -r '1.1.1.1 2.2.2.2 3.3.3.3'", type = str )
parser.add_argument('-f', '--floapingip', help='vip address of lvs' )
parser.add_argument('-g', '--gatewaying', help='gatewaying (direct routing)',action='store_true')
parser.add_argument('-m','--masquerading', help='masquerading (NAT)', action='store_true')
parser.add_argument('-S','--srcport', help='listen on floapip port', type = int )
parser.add_argument('-R','--destport', help='listen on realserver port', type = int )
args = parser.parse_args()
