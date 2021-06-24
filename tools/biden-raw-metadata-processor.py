#!/usr/local/bin/python3

import json
import pprint
from unidecode import unidecode

x = []

photo_disclaimer = "This official White House photograph is being made available only for publication by news organizations and/or for personal use printing by the subject(s) of the photograph. The photograph may not be manipulated in any way and may not be used in commercial or political materials, advertisements, emails, products, promotions that in any way suggests approval or endorsement of the President, the First Family, or the White House"

photographers = {'Adam Schultz': '@schultzinit',
                 'Cameron Smith': '@_photocam',
                 'Carlos Fyfe': 'Carlos Fyfe',
                 'Chandler West': '@chandler_west_',
                 'Cheriss May': '@cherissmay',
                 'Chuck Kennedy': '@ChuckKennedyDC',
                 'David Lienemann': '@dcclphoto',
                 'Katie Ricks': 'Katie Ricks',
                 'Kevin Lowery': '@kevloweryphoto',
                 'Lawrence Jackson': '@images_jackson',
                 'Stephanie Chasez': '@StephanieChasez'}

named_npcs = {'Joe Biden': '@JoeBiden',
              'Kamala Harris': '@KamalaHarris',
              'Jen Psaki': '@jrpsaki',
              'Dr. Jill Biden': '@DrBiden',
              'Susan Rice': '@AmbassadorRice',
              'John Kerry': '@JohnKerry'}

with open('/Users/tcook/repo/nostalgiabot-biden/memories-whitehouse-raw.json', 'r') as f:
    m = json.load(f)
    for p in m:
        photo = {}

        filename  = p['url_o'].split('/')[-1]
        bucketing = filename[:3]
        photo['title'] = p['id']
        photo['datetaken'] = p['datetaken']
        photo['source'] = p['url_o']
        photo['photo_url'] = f"https://github.com/tomcook/nostalgiabot-biden/raw/main/photos/whitehouse/{bucketing}/{filename}"
        photo['flickr_url'] = f"https://www.flickr.com/photos/whitehouse/{p['id']}/"

        # Remove the legal disclaimer attached to *most* photo captions
        photo['caption'] = unidecode(p['description']['_content'].replace(photo_disclaimer, ''))

        # Extract the name of the photographer and add new metadata for their twitter handle
        try:
            photo_credit = photo['caption'].split('(')[-1]
            photo['caption'] = photo['caption'].replace(photo_credit, '').rstrip(' (').rstrip()
            photo['photographer'] = photo_credit.replace('Courtesy Photo by ','').replace('Official White House Photo by ','').translate({ord(x): '' for x in [')','(','.',"\n"]}).rstrip()
        except IndexError:
            #print(photo)
            continue
        try:
            if photo['photographer'] in photographers:
                photo['photographer'] = photographers[photo['photographer']]
            else:
                photo['photographer'] = "@WhiteHouse"
        except KeyError:
            continue

        # Replace proper nouns of people that appear often in captions with their twitter handles
        for name, handle in named_npcs.items():
            photo['caption'] = photo['caption'].replace(name, handle)

        x.append(photo)

print(json.dumps(x, indent=2))