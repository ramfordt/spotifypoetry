'''
Created on Aug 5, 2014

@author: ramsysafadi
'''
from spotify_poetry.app.models import Track
from spotify_poetry.app.helpers import SpotifyHelper

class SpotifyPoet:
    _spotify_helper = SpotifyHelper()  
    
    def __init__(self):
        self._spotify_helper = SpotifyHelper()  
    
    def sing_verse(self, verses):
        # search all possible arrangements and populate search cache if missing
        # brute force approach - very fast if properly parallelized and primed 
        # Somewhat appropriate for an I/O bound situation but inefficient with CPU and Memory
        # TODO: find a smarter way to do this
        self._spotify_helper.batch_track_search(verses.possible_track_names)
        
        best_arrangement = None
        best_missing_words = 0
        # best_track_list_size = 0

        # running on the assumption that the optimal solution is
        # 1) minimizing unmatched words is most important
        # 2) minimizing the track list size is second most important 
        #
        # possible arrangements are pre-sorted by partition_util so that the
        # arrangements with the least number of tracks (i.e., optimal solution)
        # are included first
        for arrangement in verses.possible_arrangements :
            tracks = []
            # track_list_size = len(arrangement)
            missing_words = 0
            for track_name in arrangement:
                track_details = self._spotify_helper.search_track(track_name)
                if track_details == None :
                    missing_words += len(track_name.split())
                    tracks.append(Track(track_name, None)) # create empty track
                else :
                    tracks.append(track_details)

            # prioritize the first elements in the list of possible arrangements to take advantage of pre-sort
            if best_arrangement == None or missing_words < best_missing_words :
                best_arrangement = tracks
                best_missing_words = missing_words
                # best_track_list_size = track_list_size

            # take a shortcut since possible_arrangements were pre-ordered based on least number of tracks 
            if missing_words == 0 :
                return best_arrangement      
            
        return best_arrangement;   

    def sing_poem(self, poem):
        track_list = []
        for verse in poem.verses :
            track_list.append(self.sing_verse(verse));
        return track_list
