#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
import codecs
import json
from pymongo import MongoClient
"""
Uploads a json flie to a MongoDB instance.
"""
MongoClient("mongodb://localhost:27017")
db = client.yucatan_osm

def main():
    pass

if __name__ == "__main__":
    main()
