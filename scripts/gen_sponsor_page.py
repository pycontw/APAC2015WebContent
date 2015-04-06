#!/usr/bin/python

import jinja2
import csv
import logging
import codecs
from collections import defaultdict
from gcloud import storage
from jinja2 import Template
template = Template(open('sponsor_page.html').read())


bucket = storage.get_bucket(
    "pycon-apac-2015",
    "living-bio"
)


def upload_image(filename):
    try:
        key = bucket.upload_file(filename)
        key.make_public()
        return key.public_url
    except:
        return 'http://storage.googleapis.com/pycon-apac-2015/%s' % filename

def import_application():
    level_orders = ["Platinum", "Gold", "Silver", "Bronze", "Media", "Other"]
    sponsor_categories = defaultdict(list)
    with open('application.csv') as ifile:
        ireader = csv.DictReader(ifile)

        for row in ireader:
            if not row['Sponsor Package']: continue
            level = row['Sponsor Package'].split()[0]
            if level not in level_orders:
                logging.warning("not recognize level %s", level)
                continue

            name = row["Sponsor Name"].decode('utf8')
            logo = upload_image(row["Sponsor Logo Image"])
            description = row["Sponsor Description"].decode('utf8')

            sponsor_categories[level].append({
                "name": name,
                "level": level,
                "logo": logo,
                "description": description
            })

    sponsor_categories = [{
        "level":k,
        "sponsors": sponsor_categories[k]
    } for k in level_orders]

    html = template.render(sponsor_categories=sponsor_categories)
    with open('sponsor_page.gen.html', 'w') as ofile:
        ofile.write(html.encode('utf8'))


if __name__ == '__main__':
    import clime; clime.start(debug=True)
