#!/usr/bin/env python

import datetime
import os
from jinja2 import Environment, FileSystemLoader
import csv

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

template = env.get_template('t.md')
template.globals['now'] = datetime.datetime.utcnow


with open('mitre.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(spamreader, None)  # skip the headers
    for row in spamreader:
        t = {"id":row[0],"name":row[1],"description":row[2],"url":row[3],"tactics":row[5].split(','),"parent":row[6]}

        result = template.render(technique=t)
        with open(os.path.join("output",t["id"]+".md"), "w") as fh:
            fh.write(result)