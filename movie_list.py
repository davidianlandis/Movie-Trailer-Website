import movie,build

# what are my favorite movies - include youtube id
rushmore = movie.Movie("Rushmore","GxCNDpvGyss")
hot_fuzz = movie.Movie("Hot Fuzz","KOddZELDPmk")
donnie_darko = movie.Movie("Donnie Darko","ZZyBaFYFySk")
a_knights_tale = movie.Movie("A Knight's Tale","zH6U5y086hw")
super_troopers = movie.Movie("Super Troopers","6Wx5GgJhM9Y")
the_dark_knight = movie.Movie("The Dark Knight","yrJL5JxEYIw")

# put into array
movies = [rushmore,hot_fuzz,donnie_darko,a_knights_tale,super_troopers,the_dark_knight]

# movies we successfully got info for will be put into a new array to use when building the web page
movies_with_info = []

# loop through array and get info for each movie (from omdbapi.com) - they don't have trailer info
#     saves info into array movie.data
for movie in movies:
    movie.get_movie_info()
    # omdb returns a True "Response" variable if movie is found. movie class will set to False if we don't get valid JSON
    if movie.data["Response"] == "True":
        # hurray, we got data.  Add this to the array of movies_with_info
        movies_with_info.append(movie)

build.create_page(movies_with_info)
