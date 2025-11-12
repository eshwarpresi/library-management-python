class Book:
    def __init__(self, title, author, isbn, genre, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.quantity = quantity

    def update_quantity(self, new_quantity):
        """Update the quantity of the book"""
        if new_quantity >= 0:
            self.quantity = new_quantity
            return True
        else:
            print("Error: Quantity cannot be negative.")
            return False

    def update_details(self, title=None, author=None, genre=None):
        """Update book details"""
        if title:
            self.title = title
        if author:
            self.author = author
        if genre:
            self.genre = genre

    def is_available(self):
        """Check if book is available for borrowing"""
        return self.quantity > 0

    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {self.genre} - Available: {self.quantity}"

    def to_dict(self):
        """Convert book object to dictionary for easy serialization"""
        return {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'genre': self.genre,
            'quantity': self.quantity
        }
