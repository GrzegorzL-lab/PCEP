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
              break #asking for a movie name to add to the list
                  #and staying in the loop if user wants to add another one
                  #then goes back to the main menu if users types in "no"
        
    elif choice == "2":
        while True:
          movie = input("Enter the movie name to remove: ")
          favorite_movies.remove(movie)
          again = input("Remove another? (Yes/No): ")
          if again.lower() != "yes":
              break #asking for the movie name to remove from the list
                    #staying in the loop if user wants to keep removing
                    #going back to main menu when user types "no"

    elif choice == "3":
        while True:
          print(favorite_movies)
          again = input("Want to see the list again?(Yes/No):")
          if again.lower() != "yes":
             break #simply printing the movie names list, going back to main menu after a no

    elif choice == "4":
        print("Good bye!")
        break

    else:
        print("Wrong number, try again.")
