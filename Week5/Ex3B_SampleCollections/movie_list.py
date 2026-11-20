# Movie list
movie1 = "real_steel"
movie2 = "notebook"

# List of favorite movies
favorite_movies = [movie1, movie2]

len(movie1)
len(movie2)

# 3. Use the len() function to print the descriptive statement
print(f"The list {favorite_movies} includes my top {len(favorite_movies)} favorite movies")

# 4. Print a sorted list two ways 
# (Note: make sure that your list items aren’t already in alphabetical order to start with, or you won’t notice any difference)

print(sorted(favorite_movies))
print(favorite_movies)
# I notice that the sorted list is in alphabetical order, while the original list remains unchanged.

favorite_movies.sort()
print(favorite_movies)
# I notice that the list is now sorted in alphabetical order permanently.

movie3 = "top_gun"
favorite_movies.append(movie3)
print(favorite_movies)
# I notice that the new movie has been added to the list. 
