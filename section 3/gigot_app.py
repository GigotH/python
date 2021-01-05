# Incomplete app!
"""--------------------------
NOTES:

Store movies in a list, which means when the application ends, the list of movies is gone.




--------------------------"""
def get_movie_from_user():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movie = {"title": title, "director": director, "year": year}

    return movie


def add_movie(movie):
    with open(movie_file, 'a') as filehandle:
        filehandle.write('%s\n' % movie)


def list_movies():
    # temporary, until I can get nicer formatted output

    filehandle = open(movie_file, 'r')
    movie_list = filehandle.read()
    print(movie_list)
    filehandle.close()

    # with open(movie_file, 'r') as filehandle:
    #     for movie in filehandle:
    #         print(movie)

    # movie_list = filehandle.read()
    # print()
    # print(f"Length of movie_list: {len(movie_list)}")
    # print()
    # for movie in movie_list:
    #     print(f"Length of movie: {len(movie)}")

        # print(f"Title: {movie['title']}, Director: {movie['director']}, Released: {movie['year']}")
        # print(f"Title: {movie['title']}, Director: {movie['director']}, Released: ")
    #print(movie_list)
 


movie_file = 'moviefile.txt'
MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


# You may want to create a function for this code




# movies.append({
#     'title': title,
#     'director': director,
#     'year': year
# })


# Create other functions for:
#   - listing movies
#   - finding movies


# And another function here for the user menu
selection = input(MENU_PROMPT)
while selection != 'q':
    if selection == "a":
        add_movie(get_movie_from_user())
    elif selection == "l":
        list_movies()
    elif selection == "f":
        pass
    else:
        print('Unknown command. Please try again.')

    selection = input(MENU_PROMPT)


# Remember to run the user menu function at the end!