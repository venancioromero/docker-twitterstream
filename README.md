# docker-twitterstream

You need an account of twitter and create an application on https://apps.twitter.com/

Fields required:
 - DOWNLOAD_TIME (in seconds) <-- time that application will be running
 - ACCESS_TOKEN_KEY
 - ACCESS_TOKEN_SECRET 
 - CONSUMER_KEY
 - CONSUMER_SECRET

# RUN:
With this example the container will write tweets by standard output and will write in a file inside the container.

```
docker run \
--rm \
-v $PWD:/output \
-e "DOWNLOAD_TIME=10" \
-e "ACCESS_TOKEN_KEY=your_access_token_key" \
-e "ACCESS_TOKEN_SECRET=your_access_token_secret" \
-e "CONSUMER_KEY=your_consumer_key" \
-e "CONSUMER_SECRET=your_consumer_secret" \
--name twitterstream \
venoty/twitterstream
```
# Example of twits recollected:

{"lang": "en", "text": "I\u2019m so done wit everybody!!", "place": {"full_name": "Alexandria, LA", "url": "https://api.twitter.com/1.1/geo/id/c09ab6ee5a6f7b31.json", "country": "United States", "place_type": "city", "bounding_box": {"type": "Polygon", "coordinates": [[[-92.57133, 31.22783], [-92.57133, 31.35872], [-92.402313, 31.35872], [-92.402313, 31.22783]]]}, "country_code": "US", "attributes": {}, "id": "c09ab6ee5a6f7b31", "name": "Alexandria"}}


{"lang": "und", "text": "\ud83d\udc99 https://t.co/HlO0wrPYpc", "place": {"full_name": "Concei\u00e7\u00e3o de Macabu, Brasil", "url": "https://api.twitter.com/1.1/geo/id/ebd1128779b9e653.json", "country": "Brasil", "place_type": "city", "bounding_box": {"type": "Polygon", "coordinates": [[[-41.973559, -22.275011], [-41.973559, -22.049], [-41.658106, -22.049], [-41.658106, -22.275011]]]}, "country_code": "BR", "attributes": {}, "id": "ebd1128779b9e653", "name": "Concei\u00e7\u00e3o de Macabu"}}


{"lang": "ja", "text": "I'm at \u672d\u5e4c\u99c5 in \u672d\u5e4c\u5e02, \u5317\u6d77\u9053 https://t.co/Adn0eeBKOT", "place": {"full_name": "\u5317\u6d77\u9053 \u672d\u5e4c\u5e02 \u5317\u533a", "url": "https://api.twitter.com/1.1/geo/id/13fbcf4150ce380c.json", "country": "\u65e5\u672c", "place_type": "city", "bounding_box": {"type": "Polygon", "coordinates": [[[141.278862, 43.043466], [141.278862, 43.156913], [141.443664, 43.156913], [141.443664, 43.043466]]]}, "country_code": "JP", "attributes": {}, "id": "13fbcf4150ce380c", "name": "\u672d\u5e4c\u5e02 \u5317\u533a"}}


{"lang": "ja", "text": "\u9774\u306f\u3001ABC\u30de\u30fc\u30c8\u3063\u3066\u3001\u6c7a\u3081\u3066\u307e\u3059\u3002", "place": {"full_name": "\u5343\u8449 \u7fd2\u5fd7\u91ce\u5e02", "url": "https://api.twitter.com/1.1/geo/id/41d9dd520c812894.json", "country": "\u65e5\u672c", "place_type": "city", "bounding_box": {"type": "Polygon", "coordinates": [[[139.986485, 35.652517], [139.986485, 35.70826], [140.085083, 35.70826], [140.085083, 35.652517]]]}, "country_code": "JP", "attributes": {}, "id": "41d9dd520c812894", "name": "\u7fd2\u5fd7\u91ce\u5e02"}}



