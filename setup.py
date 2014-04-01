#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2014年3月30日

@author: Edward Shen  
'''

#if __name__ == '__main__':
#    pass
from setuptools import setup, find_packages
setup(
    name = "dnsManager",
    version = "1.0",
    packages = find_packages(),
    entry_points = {
      #  'setuptools.installation': [
      #      'eggsecutable = modifyImage.modifyImage:main',
        #],
                     'console_scripts': [
            'dnsManager = com.shendl.dnsdynamic.dnsManager:main',
            
        ],
    }
)
