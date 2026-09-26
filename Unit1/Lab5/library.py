class library:
    def __init__(self):
        self.users = []
        self.books = []

    def add_user(self, user):
        self.users.append(user)

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(book.show_book_info())

    def borrow_book(self, book, user):
        if book.availble:
            book.availble = False
            print(f"Book '{book.title}' borrowed by {user.name}")
        else:
            print(f"Book '{book.title}' is already borrowed")

    def return_book(self, book):
        if not book.availble:
            book.availble = True
            print(f"Book '{book.title}' has been returned")
        else:
            print(f"Book '{book.title}' was not borrowed")