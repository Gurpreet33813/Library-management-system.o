# ======================================
# Library Management System_2
# ======================================

from datetime import datetime

# ===============================
# Book Class
# ===============================
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False
        self.issued_to = None
        self.issue_date = None
        self.days_issued = 0

# ===============================
# Fine Calculator
# ===============================
def calculate_fine(extra_days):
    fine = 0
    rate = 10
    week = 1

    while extra_days > 0:
        days_in_week = min(7, extra_days)
        fine += days_in_week * rate
        extra_days -= days_in_week

        week += 1
        rate *= week

    return fine

# ===============================
# Library Service
# ===============================
class LibraryService:
    def __init__(self):
        self.books = {}

    def add_book(self):
        print("\n--- Add Book ---")
        book_id = input("Enter Book ID: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")

        if book_id in self.books:
            print(" Book already exists!\n")
        else:
            self.books[book_id] = Book(book_id, title, author)
            print(" Book added successfully!\n")

    def view_books(self):
        print("\n--- Book List ---")

        if not self.books:
            print("No books available.\n")
            return

        for book in self.books.values():
            status = "Issued" if book.is_issued else "Available"
            print(f"ID: {book.book_id} | {book.title} | {book.author} | {status}")
        print()

    def issue_book(self):
        print("\n--- Issue Book ---")
        book_id = input("Enter Book ID: ")

        if book_id not in self.books:
            print(" Book not found!\n")
            return

        book = self.books[book_id]

        if book.is_issued:
            print(" Book already issued!\n")
            return

        student_name = input("Enter Student Name: ")

        try:
            days = int(input("Enter number of days: "))
        except ValueError:
            print(" Invalid input! Enter a number.\n")
            return

        book.is_issued = True
        book.issued_to = student_name
        book.issue_date = datetime.now()
        book.days_issued = days

        print("\n Book issued successfully!")
        print("\n Fine Policy:")
        print("1st week: Rs 10/day")
        print("2nd week: Rs 20/day")
        print("3rd week: Rs 60/day")
        print("Further weeks continue multiplying\n")

    def return_book(self):
        print("\n--- Return Book ---")
        book_id = input("Enter Book ID: ")

        if book_id not in self.books:
            print(" Book not found!\n")
            return

        book = self.books[book_id]

        if not book.is_issued:
            print(" Book was not issued!\n")
            return

        return_date = datetime.now()
        issued_days = (return_date - book.issue_date).days

        extra_days = issued_days - book.days_issued

        if extra_days > 0:
            fine = calculate_fine(extra_days)
            print(f"\n Late Return! Fine = Rs {fine}")
        else:
            print("\n Returned on time. No fine!")

        # Reset
        book.is_issued = False
        book.issued_to = None
        book.issue_date = None
        book.days_issued = 0

        print(" Book returned successfully!\n")

# ===============================
# Main Program
# ===============================
def main():
    library = LibraryService()

    while True:
        print("====== Library Management System ======")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            library.add_book()
        elif choice == '2':
            library.view_books()
        elif choice == '3':
            library.issue_book()
        elif choice == '4':
            library.return_book()
        elif choice == '5':
            print("Thank you for using the system!")
            break
        else:
            print(" Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()

