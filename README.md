dnsDynamicManager
=================
Project github:https://github.com/shendl1978/dnsDynamicManager.git
Writer:Edward Shen(Shanghai,China)
Writer's blog:http://blog.csdn.net/shendl
Writer's github wiki:https://github.com/shendl1978/blog/wiki/_pages
Writer's email: shendl1978@gmail.com


dns dynamic tool for www.dnsdynamic.org

1,Compile:
./setup.py build

2,install:
sudo ./setup.py  install

3,build rpm:
sudo ./setup.py bdist_rpm

usage:
dnsManager --help
Usage: dnsManager [options]

Copyright 2014 user_name (organization_name)
Licensed under the Apache License 2.0
http://www.apache.org/licenses/LICENSE-2.0

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -u USERNAME, --username=USERNAME
                        username on https://www.dnsdynamic.org/
  -p PASSWORD, --password=PASSWORD
                        password on https://www.dnsdynamic.org/
  -d DNS, --dns=DNS     dns on https://www.dnsdynamic.org/
  -v, --verbose         set verbosity level [default: none]

