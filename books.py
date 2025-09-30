class Library:
    book_list=[]
    @classmethod
    def entry_book(self, book):
        self.book_list.append(book)
        
class Book:
    def __init__(self, book_id, title, author, availability):
        self.__book_id = book_id
        self._title = title
        self._author = author
        self.__availability = availability
        Library.entry_book(self)

    def borrow_book(self):
        if self.__availability:
            self.__availability=False
            print(f"The book '{self._title}' has been borrowed.")
        else:
            print(f"The book '{self._title}' is currently not available.")
    def return_book(self):
        self.__availability=True
        print(f"The book '{self._title}' has been returned.") 
    def view_book_info(self):
        print(f"Book ID: {self.__book_id}")
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")
        if self.__availability==True:
            print("Availability: Available")
        else:
            print("Availability: Not available")        
            
    def retBookID(self):
        return self.__book_id
    def retBookAvailability(self):
        return self.__availability         
            
book1 = Book("201", "Pride and Prejudice", "Jane Austen", True)
book2 = Book("202", "1984", "George Orwell", False)
book3 = Book("203", "To Kill a Mockingbird", "Harper Lee", True)

def display_menu():
    print("\nLibrary Menu")
    print("1. View All Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")
    
while True:
    display_menu()
    choice=input("Enter your choice (1-4): ")

    if choice=="1":
        if not Library.book_list:
            print("No books in the library.")
        else:
            print("\n")
            for book in Library.book_list:
                book.view_book_info()
                print("\n")
                
    elif choice=="2":
        book_id=input("Enter Book ID to borrow: ")
        found=0
        for book in Library.book_list:
            if book.retBookID()==book_id:
                book.borrow_book()
                found=1
                break
        if found==0:
            print("Book not found.")
           


 
    elif choice=="3":
        book_id=input("Enter Book ID to return: ")
        found=0
        for book in Library.book_list:
            if book.retBookID()==book_id and book.retBookAvailability()==False:
                book.return_book()
                found = 1
                break
            elif book.retBookID()==book_id and book.retBookAvailability()==True:
                print("The book wasn't borrowed.")
                found=1
                break
        if found==0:
            print("Invalid Book ID")
            
    elif choice=="4":
        print("Exiting the system. Goodbye!")
        break
    
    else:
        print("Invalid choice.")
