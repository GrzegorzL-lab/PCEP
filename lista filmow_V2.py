favorite_movies = []

while True:
    print("\n What would you like to do?")
    print("1. Add a movie")
    print("2. Remove a movie")
    print("3. Show favorite movies")
    print("4. Quit")

    choice = input("Choose an option (1/2/3/4): ")

    if choice == "1":
        while True:
          movie = input("Enter the movie name: ")
          favorite_movies.append(movie)
          again = input("Add another? (Yes/No): ")
          if again.lower() != "yes":
              break # V1: Asking for a movie name to add to the list
                    # Staying in the loop if user wants to add another one
                    # Then user goes back to the main menu if they typed in "no"
        
    elif choice == "2":
        while True:
          movie = input("Enter the movie name to remove: ").strip()
          if movie in favorite_movies:
              favorite_movies.remove(movie)
              print(f"Removed '{movie}' from the list.")
          else:
              print(f"'{movie} is not in your list.")
          again = input("Remove another? (Yes/No): ")
          if again.lower() != "yes":
              break
            # V1: Asking for the movie name to remove from the list
            # staying in the loop if user wants to keep removing, going back to main menu when user types "no"
            # V2: Added error handling and removed leading/trailing from the movie string with .strip()

    elif choice == "3":
        if favorite_movies:
            for i, movie in enumerate(favorite_movies, start =1):
                print(f"{i}. {movie}")
        else:
            print("Your favorite movie list is empty")
            # V1: Simply printing the movie names list, going back to main menu after a "no"
            # V2: Added error handling, removed redundant loop, added minor listing improvement with enumerate()

    elif choice == "4":
        print("Good bye!")
        break

    else:
        print("Wrong number, try again.")
