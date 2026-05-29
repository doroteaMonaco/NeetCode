from collections import defaultdict
import heapq
from typing_extensions import List

from git import List

class Twitter:

    def __init__(self):
        self.userTweet = defaultdict(list)
        self.userFollower = defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweet[userId].append((self.timestamp, tweetId))
        self.timestamp -= 1
         

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        followees = self.userFollower[userId] | {userId} # include self tweets
        
        for followeeId in followees:
            if self.userTweet[followeeId]: # if the followee has tweets
                index = len(self.userTweet[followeeId]) - 1 # start with the most recent tweet
                timestamp, tweetId = self.userTweet[followeeId][index] # get the most recent tweet
                heapq.heappush(minHeap, (timestamp, tweetId, followeeId, index)) # push the most recent tweet of each followee into the min heap
        
        res = []
        while minHeap and len(res) < 10:
            timestamp, tweetId, followeeId, index = heapq.heappop(minHeap) # get the most recent tweet from the min heap
            res.append(tweetId)
            
            if index > 0: # if there are more tweets from the same followee
                next_index = index - 1 # get the next most recent tweet index
                next_timestamp, next_tweetId = self.userTweet[followeeId][next_index]
                heapq.heappush(minHeap, (next_timestamp, next_tweetId, followeeId, next_index))
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollower[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
            if followeeId in self.userFollower[followerId]:
                self.userFollower[followerId].remove(followeeId)

#Time Complexity: O(N log k) where N is the total number of tweets from the followees and k is the number of followees. In the worst case, if a user follows all other users, N can be equal to the total number of tweets in the system. The log k factor comes from the heap operations.
#Space Complexity: O(k) where k is the number of followees. In the worst case, if a user follows all other users, the space complexity can be O(U) where U is the total number of users in the system.


#Other solution
class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        if len(self.tweetMap[userId]) > 10:
            self.tweetMap[userId].pop(0)
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followMap[userId].add(userId) # include self tweets
        if len(self.followMap[userId]) >= 10:
            maxHeap = []
            for followeeId in self.followMap[userId]:
                if followeeId in self.tweetMap:
                    index = len(self.tweetMap[followeeId]) - 1
                    count, tweetId = self.tweetMap[followeeId][index]
                    heapq.heappush(maxHeap, [-count, tweetId, followeeId, index - 1])
                    if len(maxHeap) > 10:
                        heapq.heappop(maxHeap)
            while maxHeap:
                count, tweetId, followeeId, index = heapq.heappop(maxHeap)
                heapq.heappush(minHeap, [-count, tweetId, followeeId, index]) # push the top 10 tweets from maxHeap to minHeap
        else:
            for followeeId in self.followMap[userId]:
                if followeeId in self.tweetMap:
                    index = len(self.tweetMap[followeeId]) - 1
                    count, tweetId = self.tweetMap[followeeId][index]
                    heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
#Time Complexity: O(n) for each getNewsFeed call, O(1) for the others methods where n is the total number of tweets from the followees. In the worst case, if a user follows all other users, n can be equal to the total number of tweets in the system. The heap operations are O(log k) where k is the number of followees, but since we are only interested in the top 10 tweets, we can consider it as O(1) for simplicity.
#Space Complexity: O(N*m + N*m +n) where N is the number of users and m is the maximum number of tweets per user (10 in this case). The first term O(N*m) is for storing the tweets, the second term O(N*m) is for storing the follow relationships, and the third term O(n) is for the heap used in getNewsFeed.