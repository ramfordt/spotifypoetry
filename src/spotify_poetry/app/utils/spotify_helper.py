'''
Created on Aug 5, 2014

@author: ramsysafadi
'''
from datetime import datetime

from gevent.queue import Queue

from spotify_poetry.app.utils.geevent_util import batch_query, query_url
from spotify_poetry.app.models import Track


class SpotifyHelper:
    _search_cache = {}
    
    def __init__(self):
        self.trackTree = []    
        
    def search_track(self, track_name):
        if track_name in self._search_cache :
            return self._search_cache[track_name]
        return None
        
    def batch_track_search(self, track_names):
        return self._batch_track_search_parallel(track_names)

    # parallel search
    def _batch_track_search_parallel(self, track_names):
        start = datetime.now()
        requests = []
        for track in track_names :
            if track not in self._search_cache :
                request_string = "http://ws.spotify.com/search/1/"+'track.json?q='+track.replace(' ', '+')+'&page=1'
                requests.append(request_string)
        results = batch_query(requests)
        end = datetime.now()
        elapsed = end - start
        #print ("-=-=-=-=-= done with asynch batch: " + str(elapsed) + " -=-=-=-=-==")
        self._cache_results(results)

    # serial search
    def _batch_track_search_serial(self, track_names):
        start = datetime.now()
        resultQueue = Queue()
        for track in track_names :
            if track not in self._search_cache :
                request_string = "http://ws.spotify.com/search/1/"+'track.json?q='+track.replace(' ', '+')+'&page=1'
                query_url(request_string, resultQueue)
        resultQueue.put(StopIteration)        
        results = []
        for data in resultQueue :
            results.append(data)
        end = datetime.now()
        elapsed = end - start
        #print ("-=-=-=-=-= done with synch batch: " + str(elapsed) + " -=-=-=-=-==")
        self._cache_results(results)
    
    def _cache_results(self, results):
        for data in results :
            # debug:
            #print (str(data["info"]["num_results"]) + " results from '" + data["info"]["query"])
            trackName = data["info"]["query"]
            self._search_cache[trackName] = None;
            if (data["info"]["num_results"] > 0) :
                for trackJson in data["tracks"]:
                    if trackJson['name'].lower() == trackName :
                        self._search_cache[trackName] = Track(trackName, trackJson);
