"""
트위터 검색 API(https://dev.twitter.com/rest/public/search)를 이용하여
트윗을 수집한다.
"""

import ujson
from twython import Twython


CONSUMER_KEY = "d8sHRLlyVNUe3Cp22zrwrDd6L"
CONSUMER_SECRET = "sOt1L8uh0Nr9NSblkkQ0nbSuCqHRos8Lbtnk3L8uM8TtevTpLd"
ACCESS_TOKEN = "212537147-tSG3YEctBNTC9O7OPHFZvkHN80OjBKg1ayJgufcu"
ACCESS_TOKEN_SECRET = "PilXo6onRQOwrjOWElaBLGP1udZasSHrWVjuNKTmsXRBO"


twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN,
                  ACCESS_TOKEN_SECRET)
result = twitter.search(q="문재인")

for status in result["statuses"]:
    tweet = ujson.dumps(status, ensure_ascii=False)
    tweet_cp949 = tweet.encode("cp949", errors="ignore")
    tweet = tweet_cp949.decode("cp949", errors="ignore")
    print(tweet)
