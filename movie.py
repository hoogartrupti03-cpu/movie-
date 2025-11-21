import sys

# Default values
default_movie = "Kantara"
default_duration = "3"
default_language = "Kannada"
default_price = "300"

# sys.argv structure:
# sys.argv[0] -> script name
# sys.argv[1] -> movie name
# sys.argv[2] -> duration
# sys.argv[3] -> language
# sys.argv[4] -> ticket price

# Assign values using defaults if arguments are missing
movie_name = sys.argv[1] if len(sys.argv) > 1 else default_movie
duration = sys.argv[2] if len(sys.argv) > 2 else default_duration
language = sys.argv[3] if len(sys.argv) > 3 else default_language
ticket_price = sys.argv[4] if len(sys.argv) > 4 else default_price

# Print the movie details card
print("------------ MOVIE DETAILS ------------")
print(f"Movie Name    : {movie_name}")
print(f"Duration      : {duration} hrs")
print(f"Language      : {language}")
print(f"Ticket Price  : ₹{ticket_price}")
print("----------------------------------------")
