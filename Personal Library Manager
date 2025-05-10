import json
import os

LIBRARY_FILE = "library.json"

# Book attributes:
# Title (str), Author (str), Publication Year (int), Genre (str), Read (bool)

# Load library from JSON file
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as f:
            return json.load(f)
    return []

# Save library to JSON file
def save_library(library):
    with open(LIBRARY_FILE, "w") as f:
        json.dump(library, f, indent=4)

# Add a book
def add_book(library):
    print("\n--- Add a Book ---")
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    try:
        year = int(input("Publication Year: ").strip())
    except ValueError:
        print("Invalid year. Book not added.\n")
        return
    genre = input("Genre: ").strip()
    read_input = input("Have you read it? (yes/no): ").strip().lower()
    read = read_input == 'yes'

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(book)
    print(f"\nBook '{title}' added successfully.\n")

# Remove a book by title
def remove_book(library):
    print("\n--- Remove a Book ---")
    title = input("Enter the title to remove: ").strip().lower()
    removed = False
    for book in library[:]:
        if book["title"].lower() == title:
            library.remove(book)
            print(f"Book '{book['title']}' removed.\n")
            removed = True
    if not removed:
        print("No book with that title found.\n")

# Search by title or author
def search_books(library):
    print("\n--- Search for a Book ---")
    keyword = input("Enter title or author to search: ").strip().lower()
    matches = [book for book in library
               if keyword in book["title"].lower() or keyword in book["author"].lower()]
    if matches:
        print(f"\nFound {len(matches)} book(s):\n")
        for book in matches:
            print_book(book)
    else:
        print("No matching books found.\n")

# Display all books
def display_books(library):
    print("\n--- All Books in Library ---")
    if not library:
        print("Library is empty.\n")
        return
    for i, book in enumerate(library, start=1):
        print(f"\nBook #{i}")
        print_book(book)

# Display statistics
def display_statistics(library):
    print("\n--- Library Statistics ---")
    total = len(library)
    if total == 0:
        print("Library is empty.\n")
        return
    read = sum(1 for book in library if book["read"])
    percent_read = (read / total) * 100
    print(f"Total books: {total}")
    print(f"Books read: {read} ({percent_read:.2f}%)\n")

# Print one book
def print_book(book):
    print(f"Title: {book['title']}")
    print(f"Author: {book['author']}")
    print(f"Year: {book['year']}")
    print(f"Genre: {book['genre']}")
    print(f"Read: {'Yes' if book['read'] else 'No'}")

# Menu
def main():
    library = load_library()

    while True:
        print("\n====== Personal Library Menu ======")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_books(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
