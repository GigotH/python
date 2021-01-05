


movie_file = 'moviefile.json'

# define list of movies
movies = [
    {"title": "Gigot", "director": "Jackie Gleason", "year": 1962},
    {"title": "Psycho", "director": "Alfred Hitchcock", "year": 1965},
    {"title": "Star Wars", "director": "Stephen Spielberg", "year": 1979}
]

# for movie in movies:
#     print(f"{movie['title']} {movie['year']}")
   # print(f"Title: {movie['title']}, Director: {movie['director']}, Released: {movie['year']}")

# for movie in movies:
#     print(f"Title: {movie['title']}, Director: {movie['director']}, Released: {movie['year']}")

with open(movie_file, 'w') as filehandle:
    for movie in movies:
        filehandle.write('%s\n' % movie)

# new_movie = {"title": "Jaws", "director": "Don't Remember", "year": 1976}

# with open(movie_file, 'a') as filehandle:
#     filehandle.write('%s\n' % new_movie)

filehandle = open(movie_file, 'r')
movie_list = filehandle.read()
print(movie_list)
filehandle.close()


