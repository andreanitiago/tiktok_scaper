import sys
import csv
import os
from TikTokApi import TikTokApi

with TikTokApi() as api:
    tag = api.hashtag(name=sys.argv[1])
    header = ['Id','createdTime','authorId','authorName','authorFollowers','authorFans','authorHeart',
              'authorVideo','authorDigg','musicId','musicName','musicAuthor','musicOriginal', 'Link']
    with open(os.path.expanduser("~/Downloads/tiktok_trending_hashtag.csv"), "w") as out_file:
        writer = csv.writer(out_file)
        writer.writerow(header)
        for video in tag.videos():
            video_get = api.video(id=video.id)
            video_data = video_get.info()
            author = video_data["author"]
            author_stats = video_data["authorStats"]
            music = video_data["music"]
            link = "https://www.tiktok.com/@"+author["uniqueId"]+"/video/"+video.id
            data = [video.id, video_data["createTime"], author["id"],author["uniqueId"], author_stats["followingCount"], 
                    author_stats["followerCount"], author_stats["heartCount"], author_stats["videoCount"], 
                    author_stats["diggCount"], music["id"], music["title"], music["authorName"], music["original"], link]
            print(data)  
            writer.writerow(data)
