# data_formats.py

def to_csv(hash, scrapd):
    scrapd.to_csv(f"{hash}_tweets.csv", index=False)

def to_json(hash, scrapd):
    scrapd.to_json(f"{hash}_tweets.json", orient="records")
