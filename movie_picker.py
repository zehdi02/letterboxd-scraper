import random

def random_movie_generator(file_name):
    try:
        with open(file_name, 'r') as file:
            movies = file.readlines()
            # Remove empty lines
            movies = [movie.strip() for movie in movies if movie.strip()]  
            if not movies:
                print("No movies found in the file.")
                return

            while True:
                random_movie = random.choice(movies)
                print("Randomly selected movie:\n\t", random_movie)
                user_input = input(f"Do you want to watch '{random_movie}'? (y/n): ")
                if user_input.lower() == "y":
                    print("Enjoy the movie!")

                    # Remove the selected movie from the list
                    movies.remove(random_movie)
                    with open(file_name, 'w') as file:
                        for movie in movies:
                            file.write(movie + '\n')
                    print(f"'{random_movie}' deleted from the list.\n")
                    break
                elif user_input.lower() == "n":
                    print("Choosing another movie...\n")
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

if __name__ == "__main__":
    # file_name = "./popular_movies/horror_movies.txt"
    folder_name = 'All Time Popular Films'
    file_name = "./" + folder_name + "/" + folder_name + "_1.txt"
    random_movie_generator(file_name)
