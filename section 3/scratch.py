#import json
#import ast


movie_file = 'moviefile.txt'

movies = []
with open(movie_file, 'r') as input_file:
    for line in input_file:
        movies.append(eval(line))

for movie in movies:
    movie_title = movie["title"]
    movie_director = movie["director"]
    movie_year = movie["year"]

    print(f"Movie: {movie_title}, Director: {movie_director}, Released:  {movie_year}")

"""
data = []

with open(movie_file, "r") as input_file:
    data = ast.literal_eval(input_file.read())
    print(f"{data}")
"""


# define list of movies
"""
movies = [
{'title': 'Gigot', 'director': 'Jackie Gleason', 'year': 1962}
{'title': 'Psycho', 'director': 'Alfred Hitchcock', 'year': 1965}
{'title': 'Star Wars', 'director': 'Stephen Spielberg', 'year': 1979}
{'title': 'Jaws', 'director': "Don't Remember", 'year': 1976}
{'title': 'Rush Hour', 'director': 'Jackie Chan', 'year': '2004'}
{'title': 'Gone With The Wind', 'director': 'Who knows?', 'year': '1939'}
{'title': 'The Wizard of Oz', 'director': 'Somebody', 'year': '1945'}
{'title': 'Saturday Night Feever', 'director': 'Someone Rich', 'year': '1979'}
{'title': 'Movie', 'director': 'Director', 'year': 'some year'}
{'title': 'Nacho Libre', 'director': 'Jack Black', 'year': '2010'}
{'title': 'Kung Fu Panda', 'director': 'Jack Black', 'year': '2013'}
{'title': 'Peter Pan', 'director': "I've forgotten", 'year': '1969'}
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
"""


"""
movies = open(movie_file)
movie_data = json.load(movies)

for movie in movie_data.values():
    print(movie)
"""
