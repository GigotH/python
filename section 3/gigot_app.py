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
    movie_file = 'moviefile.txt'

    #  create list of dictionaries from file.
    movies = []
    with open(movie_file, 'r') as input_file:
        for line in input_file:
            movies.append(eval(line))

    # iterate through list of dictinaries, printing each
    for movie in movies:
        movie_title = movie["title"]
        movie_director = movie["director"]
        movie_year = movie["year"]

        print(f"Movie: {movie_title}, Director: {movie_director}, Released:  {movie_year}")


def get_search_type():
    srch_type = ""
    while srch_type != 't' and srch_type != 'd' and srch_type != 'y':
        srch_type = input("\nEnter 't' to search by Title, 'd' to search by Director name or 'y' to search by Year:  ")
    
    return srch_type


def search_movies(search_type):
    search_string = ""
    while search_string == "":
        if search_type == "t":
            search_string = input("Enter the Title of the movie for which you want to search:  ")
            searching_for = "title"
        elif search_type == "d":
            search_string = input("Enter the Director of the movie for which you want to search:  ")
            searching_for = "director"
        else:
            search_string = input("Enter the Release Year of the movie for which you want to search:  ")
            searching_for = "year"
            if not isinstance(searching_for, int):
                print(f"The year must be an integer.  You entered {search_string}.  Please try again")
                search_string = ""
        
        print(f"\nPerforming case insensitivie {searching_for.title()} search for the string \"{search_string}\"\n")
    
    try:
        movie_file = 'moviefile.txt'
        #  create list of dictionaries from file.
        movies = []
        with open(movie_file, 'r') as input_file:
            for line in input_file:
                movies.append(eval(line))

        results_found = 'False'
        for movie in movies:
            movie_title = movie["title"]
            movie_director = movie["director"]
            movie_year = movie["year"]

            if search_type == "t":
                if search_string.lower() in movie_title.lower():
                    print(f"Found {search_string} in Movie Title: \"{movie_title}\"")
                    results_found = 'True'
            elif search_type == "d":
                if search_string.lower() in movie_director.lower():
                    print(f"Found {search_string} in Director Name: {movie_director} (Movie Title: \"{movie_title}\")")
                    results_found = 'True'
            else:
                if search_string.lower() in str(movie_year):
                    print(f"The Movie: \"{movie_title}\" was released in {search_string} ")
                    results_found = 'True'

        if results_found == "False":
            print(f"There were no results found for your {searching_for.title()} search for \"{search_string}\"\n")


            # print(f"Movie: {movie_title}, Director: {movie_director}, Released:  {movie_year}")

    except:
        print("There was a problem!")



"""
        filehandle = open(movie_file, 'r')
        movie_list = filehandle.read()
        for movie in movie_list:
            if search_string in movie:
                print(f"Found {search_string} in {movie}.")
            else:
                print(f"Did NOT find {search_string} in {movie}.")
"""


"""
MAIN CODE SECTION:
"""

movie_file = 'moviefile.txt'
MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie or 'q' to quit: "
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
        search_type = get_search_type()
        search_movies(search_type)
    else:
        print('Unknown command. Please try again.')

    selection = input(MENU_PROMPT)


# Remember to run the user menu function at the end!