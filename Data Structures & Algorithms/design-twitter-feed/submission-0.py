import heapq
from collections import defaultdict
from typing import List
class Twitter:

    def __init__(self):
        self.time = 0
        self.tweet = defaultdict(list)
        self.following = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        self.tweet[userId].append((self.time, tweetId))
    
    def getNewsFeed(self, userId: int) -> List[int]:
        heap =[]
        users = self.following[userId]|{userId}
        for u in users:
            for t in self.tweet[u]:
                heapq.heappush(heap, t)
                if len(heap)>10:
                    heapq.heappop(heap)
        feed = [ben for _, ben in sorted(heap, reverse=True)]
        return feed
                


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId!= followeeId:
            self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
