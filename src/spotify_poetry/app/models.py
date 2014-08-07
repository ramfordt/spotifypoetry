'''
Created on Aug 5, 2014

@author: ramsysafadi
'''
import string

from spotify_poetry.app.utils.partition_util import string_partition


class Poem:
    poem = ''
    verses = []
    
    def __init__(self, poem):
        self.poem = poem;
        self.verses = []
        # split poem into verses
        poem_lines = poem.splitlines(False)
        for line in poem_lines :
            self.verses.append(Verse(line))

class Verse:
    verse = ''
    possible_track_names = []
    possible_arrangements = []
    
    def __init__(self, verse):
        self.verse = verse;
        try :
            # capitalization should not matter
            verse_str = verse.lower()
            # get rid of extra spaces '''        
            verse_str = verse_str.strip()
            # get rid of punctuation like , . etc
            verse_str = "".join(l for l in verse_str if l not in string.punctuation)
            # compute possible substring combinations (i.e., track names) from the verse
            # i.e., For "Slap Chop Rap"
            #    possible_track_names = "Slap Chop Rap", "Slap Chop", "Chop Rap", "Slap", "Chop", "Rap"
            #    possible_arrangements = "Slap Chop Rap", "Slap Chop" + "Rap", "Slap" + "Chop Rap", "Slap Chop Rap"
            song_partitions = string_partition(verse_str)
            self.possible_track_names = song_partitions['tracks']
            self.possible_arrangements = song_partitions['tuples']
        except Exception as e:
            print "Error occurred with verse " + verse + " - " + e

class Track:
    track_json = None
    name = ""
    artists = ""
    album = ""
    id = ""
    
    def __init__(self, track_name, track_json):
        self.name = track_name
        if track_json != None :
            self.track_json = track_json 
            artist_names = []
            for artist in track_json['artists'] :
                artist_names.append(artist['name'])
            self.artists = ", ".join(artist_names)
            self.album = track_json['album']['name']
            href = track_json['href']
            self.id = href.split(":")[2]
   
    def __str__(self):
        message = '' 
        if (self.track_json == None) :
            message = self.name + " [song not found]"
        else :
            message = "'" + self.name + "' by " + self.artists + " [" + self.album + "]"
        return message.encode('ascii','ignore') 
