import datetime
import database
menu = """
Please select one of the following options:
1)add new movie
2) View upcoming movies
3)View all movies
4)add watched movie
5)View watched movies
7)Exit
Your selection : 
"""
def prompt_add_movie():
    title = input("input hte title")
    release_date = input("release date(dd-mm-yyyy)")
    parsed_date = datetime.datetime.strptime(release_date,"%d-%m-%Y")
    timestamp = parsed_date.timestamp()
    database.add_movie(title,timestamp)
welcome = "welcome to the watchlist app!"
print(welcome)
database.create_tables()

def print_movielist(heading,movies):
    print(f"{heading} movies ---")
    
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[1])
        human_date = movie_date.strftime("%d %b %Y") 
        print(f"{movie[0]} ({human_date})")
    print("----\n")


    
while((user_input := input(menu)) !="7"):
    if user_input=="1":
        prompt_add_movie()
        print("adding....")
    elif user_input =="2":
        movie =  database.get_movies(True)
        print_movielist("upcoming",movie)
    elif user_input == "3":
        movie =  database.get_movies()
        print_movielist("All",movie)
    elif user_input == "4":
        movie_title = input("enter the movie you have watched:")
        database.watch_movie(movie_title)
    elif user_input == "5":
        movies = database.get_watched_movies()
        print_movielist("watched",movies)
    else:
        print("invalid")