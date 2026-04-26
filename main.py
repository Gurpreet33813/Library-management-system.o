from services.library_service import LibraryService

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

