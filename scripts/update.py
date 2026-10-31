import urllib.request, xml.etree.ElementTree as ET, json, re
CH = "UC-aD71MgHg2D1y_qubs0Ocg"
url = f"https://www.youtube.com/feeds/videos.xml?channel_id={CH}"
ns = {"a": "http://www.w3.org/2005/Atom", "y": "http://www.youtube.com/xml/schemas/2015"}
root = ET.fromstring(urllib.request.urlopen(url, timeout=30).read())
out = [{"id": e.find("y:videoId", ns).text,
        "title": e.find("a:title", ns).text,
        "date": e.find("a:published", ns).text[:10]} for e in root.findall("a:entry", ns)]
KEYS = re.compile(r"ড্রাইভার|নিয়োগ|চাকরি|চাকুরি|সার্কুলার|লাইসেন্স|driver|job|circular|vacancy|recruit", re.I)
out = [v for v in out if KEYS.search(v["title"])]
json.dump(out, open("data/videos.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(out), "videos saved")
