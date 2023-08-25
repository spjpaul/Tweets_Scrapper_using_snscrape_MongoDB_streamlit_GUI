# scrapper.py

import snscrape.modules.twitter as snt

def scrap(hash, limit, sdate, edate):
    result = []
    tweets = enumerate(snt.TwitterSearchScraper(f'{hash} since:{sdate} until:{edate}').get_items())
    for tweet in tweets:
        if len(result) >= limit:
            break
        result.append({
            "date": tweet.date,
            "id": tweet.id,
            "url": tweet.url,
            "content": tweet.content,
            "user": tweet.user.username,
            "reply_count": tweet.replyCount,
            "retweet_count": tweet.retweetCount,
            "language": tweet.lang,
            "source": tweet.sourceUrl,
            "like_count": tweet.likeCount,
        })
    scrapd = pd.DataFrame(result)
    return scrapd
