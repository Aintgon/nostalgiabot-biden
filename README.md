# nostalgiabot-biden
Content for the Biden Campaign / Administration Nostalgia Bot

This repository has the raw data that feeds into the "Biden Nostalgia" twitter bot, which can be found here: https://twitter.com/BidenNostalgia.

It includes an archive of the actual images, fetched from Flickr, for safe keeping in case their API changes or the photos are put in a less-accessible place.

"memories-campaign.json" and "memories-whitehouse.json" contain all of the metadata, captions, and other bits that are assembled into the twitter caption.

The data in here is fetched by code running via GitHub Actions in the https://github.com/tomcook/nostalgiabot repo that randomly selects a photo and posts it to Twitter on a schedule.
