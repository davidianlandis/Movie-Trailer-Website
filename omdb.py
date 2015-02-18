import urllib,json

class MovieInfo():

    def __init__(self,title):
        self.title = title
        
    def get_movie_info(self):
        conn = urllib.urlopen("http://www.omdbapi.com/?t="+self.title+"&y=&plot=short&r=json")
        output = conn.read()
        #print(output)
        conn.close()
        data = json.loads(output)

        #print("Movie Title: "+data["Title"])
        #print("Year: "+data["Year"])
        #print("Rated: "+data["Rated"])
        #print("Runtime: "+data["Runtime"])
        #print("Actors: "+data["Actors"])
        #print("Poster: "+data["Poster"])
        #print("imdbRating: "+data["imdbRating"])
        #print("imdbID: "+data["imdbID"])

        self.year = data["Year"]
        


rushmore = MovieInfo("Rushmore")
rushmore.get_movie_info()

print(rushmore.year)

