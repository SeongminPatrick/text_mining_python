"""
트위터 스트리밍 API(https://dev.twitter.com/streaming/overview)를 이용하여
트윗을 수집한다.
"""

import sys
import ujson
from twython import TwythonStreamer


CONSUMER_KEY = "d8sHRLlyVNUe3Cp22zrwrDd6L"
CONSUMER_SECRET = "sOt1L8uh0Nr9NSblkkQ0nbSuCqHRos8Lbtnk3L8uM8TtevTpLd"
ACCESS_TOKEN = "212537147-tSG3YEctBNTC9O7OPHFZvkHN80OjBKg1ayJgufcu"
ACCESS_TOKEN_SECRET = "PilXo6onRQOwrjOWElaBLGP1udZasSHrWVjuNKTmsXRBO"


class MyStreamer(TwythonStreamer):
    """트위터 스트리머 클래스"""

    def on_success(self, data):
        """스트리밍이 성공했을 때 수집한 데이터를 인쇄한다."""
        
        tweet = ujson.dumps(data, ensure_ascii=False)
        tweet_cp949 = tweet.encode("cp949", errors="ignore")
        tweet = tweet_cp949.decode("cp949")
        print(tweet)
        

    def on_error(self, status_code, data):
        """스트리밍 오류가 발생했을 때 상태 코드를 인쇄한다."""

        print(status_code)

        
def main():
    streamer = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, 
                          ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    streamer.statuses.filter(track="트와이스,에이핑크,마마무")
    
#
# 실행
#

main()
