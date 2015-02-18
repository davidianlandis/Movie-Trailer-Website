import urllib,json

class Movie():

    """ Creates a movie object. Method to get movie info from open movie database """

    # title and youtube_id are passed when a new instance is created
    def __init__(self,title,youtube_id):
        self.title = title
        self.youtubeID = youtube_id
        self.data = {}

    # this gets movie info from the open movie database api
    def get_movie_info(self):
        conn = urllib.urlopen("http://www.omdbapi.com/?t="+self.title+"&y=&plot=short&r=json")
        output = conn.read()
        conn.close()
        # don't let the program error out if we can't find a movie
        try:
            self.data = json.loads(output)
            self.data["youtubeID"] = self.youtubeID #provided by me
        except ValueError, e:
            #set this same data point to false if we get no JSON so the program can handle it
            self.data["Response"] = "False="+str(e)
