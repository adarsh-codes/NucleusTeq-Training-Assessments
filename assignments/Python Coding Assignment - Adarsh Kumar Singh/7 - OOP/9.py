class Library:
    def __init__(self, books=None, members=None):
        self.books = books if books else []
        self.members = members if members else []

    def register_member(self, name):
        self.members.append(name)
        print(f"Member '{name}' registered.")

    def add_book(self, name):
        self.books.append(name)
        print(f"Book '{name}' added to the library.")

    def issue_book(self, book_name, member_name):
        if book_name not in self.books:
            print(f"Book '{book_name}' not available.")
        elif member_name not in self.members:
            print(f"Member '{member_name}' not registered.")
        else:
            self.books.remove(book_name)
            print(f"Book '{book_name}' issued to {member_name}.")

    def return_book(self, book_name):
        self.books.append(book_name)
        print(f"Book '{book_name}' returned to the library.")

    def list_books(self):
        print("Books available in the library:")
        for book in self.books:
            print("-", book)

    def list_members(self):
        print("Registered members:")
        for member in self.members:
            print("-", member)

lib = Library()
lib.add_book("The Alchemist")
lib.add_book("Three Idiots")

lib.register_member("Adarsh")
lib.register_member("Ayush")

lib.issue_book("Three Idiots", "Adarsh")
lib.return_book("Three Idiots")

lib.list_books()
lib.list_members()
