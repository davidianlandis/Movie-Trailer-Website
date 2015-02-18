import webbrowser,os

# load a main page layout into a string to do our replacements with
layout_fh = open("layout.html")
layout = layout_fh.read()
layout_fh.close()

# movie specific layout
movie_tile_content = '''
<div class="movie-tile col-md-6 col-lg-4 text-center" data-imdb-id="{imdbID}" data-imdb-rating="{imdbRating}" data-movie-year="{Year}" data-movie-runtime="{Runtime}" data-movie-rated="{Rated}" data-movie-actors="{Actors}" data-trailer-youtube-id="{youtubeID}" data-movie-box-art-url="{Poster}" data-movie-synopsis="{Plot}" data-toggle="modal" data-target="#movie-info">
    <img src="{Poster}" width="220" height="342">
    <h2>{Title}</h2>
</div>
'''

# create_tiles
#    parameter array of objects movies
#    returns string of html
def create_tiles(movies):
    html = ''
    print("Building the movie tiles...")
    for movie in movies:
        html += movie_tile_content.format(
            Title=movie.data["Title"],
            imdbID=movie.data["imdbID"],
            imdbRating=movie.data["imdbRating"],
            Year=movie.data["Year"],
            Runtime=movie.data["Runtime"],
            Rated=movie.data["Rated"],
            Actors=movie.data["Actors"].encode('utf8'), #some actor names contain non-ascii characters
            Poster=movie.data["Poster"],
            Plot=movie.data["Plot"],
            youtubeID=movie.data["youtubeID"]
        )
        print(movie.data["Title"]+" built.")
    return html

# create_page
#    parameter array of objects movies
#    return none - open browser
def create_page(movies):
    tiles = create_tiles(movies)
    #print(tiles)
    print("Creating the movie page...")

    #create the html file
    html_file = open('daves_favorite_movies.html','w')

    #insert the tiles where they belong in the layout
    final_content = layout.format(
        title_for_layout="Dave's favorite movies",
        movie_tiles=tiles
    )

    #write content and close it
    html_file.write(final_content)
    html_file.close()

    #open the html file in the browser
    webbrowser.open('file://'+os.path.abspath(html_file.name))


       
