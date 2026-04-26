from models.book import Book
from utils.fine_calculator import calculate_fine

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

        print(" Book returned successfully!\n)
