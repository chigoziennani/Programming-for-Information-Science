__author__ = 'Chigozie Nnani, cfnnani@unc.edu, Onyen = cfnnani'

# Importing Python's built-in CSV module, which provides functionality to read from and write to CSV files.
import csv

# Load book and movie collections from CSV files and return them with the maximum ID.
def load_collections():
    book_collection, max_book_id = load_collection("books.csv")
    movie_collection, max_movie_id = load_collection("movies.csv")
    
    if book_collection is None or movie_collection is None:
        return None, None
    
    print("The collections have loaded successfully.")
    return {"books": book_collection, "movies": movie_collection}, max(max_book_id, max_movie_id)

# Load a collection from a CSV file and return it with the maximum ID found.
def load_collection(file_name):
    max_id = -1
    try:
        collection = {}
        with open(file_name, "r") as collection_file:
            reader = csv.DictReader(collection_file)
            for row in reader:
                row["ID"] = int(row["ID"])
                row["Pages"] = int(row.get("Pages", 0))
                row["Year"] = int(row["Year"])
                row["Copies"] = int(row["Copies"])
                row["Available"] = int(row["Available"])
                collection[row["ID"]] = row
                max_id = max(max_id, row["ID"])
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return None, None
    
    return collection, max_id

# Display the main menu and prompt the user for a command.
def prompt_user_with_menu():
    print("\n\n********** Welcome to the Collection Manager. **********")
    print("COMMAND    FUNCTION")
    print("  ci         Check in an item")
    print("  co         Check out an item")
    print("  ab         Add a new book")
    print("  am         Add a new movie")
    print("  db         Display books")
    print("  dm         Display movies")
    print("  qb         Query for books")
    print("  qm         Query for movies")
    print("  x          Exit")
    return input("Please enter a command to proceed: ")

# Display items from a collection in batches of 10, allowing the user to view more or return to the menu.
def display_collection(collection):
    items = sorted(collection.values(), key=lambda x: x["ID"])
    index = 0

    while index < len(items):
        for i in range(index, min(index + 10, len(items))):
            item = items[i]
            print(f"ID: {item['ID']}")
            print(f"Title: {item['Title']}")
            if "Author" in item:
                print(f"Author: {item['Author']}")
            if "Publisher" in item:
                print(f"Publisher: {item['Publisher']}")
            if "Pages" in item:
                print(f"Pages: {item['Pages']}")
            if "Year" in item:
                print(f"Year: {item['Year']}")
            print(f"Copies: {item['Copies']}")
            print(f"Available: {item['Available']}\n")

        index += 10

        if index < len(items):
            user_input = input("Press enter to show more items, or type 'm' to return to the menu: ")
            if user_input.lower() == 'm':
                break
        else:
            input("Press enter to return to the menu...")

# Query a collection based on user input and display matching items.
def query_collection(collection, search_fields):
    query = input("Enter a query string to use for the search: ").lower()
    results = [item for item in collection.values() if any(query in str(item[field]).lower() for field in search_fields)]
    
    for item in results:
        print(f"ID: {item['ID']}")
        for key, value in item.items():
            if key != "ID":
                print(f"{key}: {value}")
        print()

# Check out an item from the collections by reducing its available count.

def check_out(collections):
    item_id = int(input("Enter the ID for the item you wish to check out: "))
    for category in ["books", "movies"]:
        if item_id in collections[category]:
            item = collections[category][item_id]
            if item["Available"] > 0:
                item["Available"] -= 1
                print("Your check out has succeeded.")
                print(f"ID: {item['ID']}")
                for key, value in item.items():
                    if key != "ID":
                        print(f"{key}: {value}")
            else:
                print("No copies of the item are available for check out.")
            return
    print("Invalid ID.")

# Check in an item to the collections by increasing its available count.
def check_in(collections):
    item_id = int(input("Enter the ID for the item you wish to check in: "))
    for category in ["books", "movies"]:
        if item_id in collections[category]:
            item = collections[category][item_id]
            if item["Available"] < item["Copies"]:
                item["Available"] += 1
                print("Your check in has succeeded.")
                print(f"ID: {item['ID']}")
                for key, value in item.items():
                    if key != "ID":
                        print(f"{key}: {value}")
            else:
                print("All copies are already available, so this item cannot be checked in.")
            return
    print("Invalid ID.")

# Add a new book to the collection with user-provided attributes and return the new max ID.
def add_book(books, max_id):
    max_id += 1
    print("Please enter the following attributes for the new book.")
    
    new_book = {
        "ID": max_id,
        "Title": input("Title: "),
        "Author": input("Author: "),
        "Publisher": input("Publisher: "),
        "Pages": int(input("Pages: ")),
        "Year": int(input("Year: ")),
        "Copies": int(input("Copies: ")),
        "Available": 0,
    }
    new_book["Available"] = new_book["Copies"]
    books[max_id] = new_book

    print("You have entered the following data:")
    print(f"ID: {new_book['ID']}")
    for key, value in new_book.items():
        if key != "ID":
            print(f"{key}: {value}")

    input("Press enter to add this item to the collection.  Enter 'x' to cancel.")
    return max_id

# Add a new movie to the collection with user-provided attributes and return the new max ID.
def add_movie(movies, max_id):
    max_id += 1
    print("Please enter the following attributes for the new movie.")
    
    new_movie = {
        "ID": max_id,
        "Title": input("Title: "),
        "Director": input("Director: "),
        "Length": input("Length (e.g., 120 min): "),
        "Genre": input("Genre: "),
        "Year": int(input("Year: ")),
        "Copies": int(input("Copies: ")),
        "Available": 0,
    }
    new_movie["Available"] = new_movie["Copies"]
    movies[max_id] = new_movie

    print("You have entered the following data:")
    print(f"ID: {new_movie['ID']}")
    for key, value in new_movie.items():
        if key != "ID":
            print(f"{key}: {value}")

    input("Press enter to add this item to the collection.  Enter 'x' to cancel.")
    return max_id

# Main function to load collections and handle user commands in a loop.
def main():
    collections, max_id = load_collections()
    if collections is None:
        print("Error loading collections. Exiting.")
        return
    while (command := prompt_user_with_menu()) != "x":
        if command == "ci":
            check_in(collections)
        elif command == "co":
            check_out(collections)
        elif command == "ab":
            max_id = add_book(collections["books"], max_id)
        elif command == "am":
            max_id = add_movie(collections["movies"], max_id)
        elif command == "db":
            display_collection(collections["books"])
        elif command == "dm":
            display_collection(collections["movies"])
        elif command == "qb":
            query_collection(collections["books"], ["Title", "Author", "Publisher"])
        elif command == "qm":
            query_collection(collections["movies"], ["Title", "Director", "Genre"])
        else:
            print("Unknown command.  Please try again.")

main()