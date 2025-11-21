import sys

# Check if all arguments are provided
if len(sys.argv) != 5:
    print("Usage: python movie.py <movie_name> <duration> <language> <ticket_price>")
    sys.exit()

# Assign command-line arguments
movie_name = sys.argv[1]
duration = sys.argv[2]
language = sys.argv[3]
ticket_price = sys.argv[4]

# Print movie details card
print("\n====== MOVIE DETAILS CARD ======")
print(f"Movie Name   : {kantara}")
print(f"Duration     : {3}")
print(f"Language     : {kannada}")
print(f"Ticket Price : {300}")
print("================================\n")
