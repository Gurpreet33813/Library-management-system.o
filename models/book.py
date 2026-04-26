class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False
        self.issued_to = None
        self.issue_date = None
        self.days_issued = 0
