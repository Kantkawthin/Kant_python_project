'''
#fetch all the available books in the library   - displayBooks()
#add new books  - addBook()
#Keep a track of borrowed book  - lendBook()
#Update the details based on the return books  - returnBook()

#display book
#Lend book
#Add book
#Return book
'''

#4 function in class Library
class Library:
    def __init__(self,booksList,name,lendDict):
        self.booksList = booksList
        self.name     = name
        self.lendDict = lendDict     # create dictionary {key:value}

    def displayBooks(self):
        print(f'We have the following books in our library: {self.name}')
        for book in self.booksList:
            print(book)
            
    def showLendedBooks(self):
        if len(self.lendDict) == 0:  # Check if no books are lent out
            print("No books are currently lent out.")
        else:
            print("\nLent books and users:\n")
            for book, user in self.lendDict.items():
                print(f'Book: "{book}", User: "{user}"')

    def addBook(self,book):
        if book in self.booksList:
            print('Book already exit')
        else:
            self.booksList.append(book)
            #also add to the database
            bookDatabase = open(dataBaseName,'a')   #a => append mode
            bookDatabase.write('\n')
            bookDatabase.write(book)  #add book to database
            print('Book added')

    def removeBook(self,book):
        if book in self.booksList:
            self.booksList.remove(book) #remove from the in-memory booksList
            #remove from the library booksList Database
            bookDatabase = open(dataBaseName,'r')
            lines = bookDatabase.readlines() #read books from database
            bookDatabase = open(dataBaseName,'w')
            for line in lines:
                if line.strip()!=book:
                    bookDatabase.write(line)
            print(f'"{book}" Book is remove from the library')
        else:
            print(f'"{book}" Book is not available in library')
            

    def lendBook(self,book,user):
        if book in self.booksList:
            if book not in self.lendDict.keys():
                self.lendDict.update({book:user})
                #also add to the database
                lendDatabase = open('lendBook.txt','a')   #a => append mode
                lendDatabase.write('\n')
                lendDatabase.write(f'{book}, {user}')  #lend book to database
                print('Book lended. Database update') 
            else:
                print(f'Sorry, book is already lended by {self.lendDict[book]}')
        else:
            print("we don't have this book in our library")

    def returnBook(self,book):
        if book in self.lendDict.keys():
            self.lendDict.pop(book)
            #also delete from lendBook.txt database file
            lendDatabase = open('lendBook.txt','r')
            lines = lendDatabase.readlines() # Read all lines in the file
            lendDatabase = open('lendBook.txt','w') #overwrite the lines
            for line in lines:
                if book not in line:  # Write back all lines except the returned book
                    lendDatabase.write(line)
            print('Return Book successfully')
        else:
            print('The book does not exit in Lending Database')


#main function
def main():
    while (True):
        print(f'\nWelcome to the {library.name} library. Following are options:')
        choice = '''
        1. Display Books
        2. Lend a book
        3. Add a book
        4. Return a book
        5. Show lend book
        6. Remove book from library
        '''
        print(choice)

        userInput = input('Press Q to quit or C to continue: ')
        #User choose C
        if userInput=="C" or userInput=="c":

            #choose above options
            userChoice = int(input('Select an option to continue: '))
            #Display book                 
            if userChoice==1:
                library.displayBooks()
            #Lend a book                 
            elif userChoice==2:
                book = input('Enter the book name you want to lend: ')
                user = input('Enter your name: ')
                library.lendBook(book,user)
            #Add a book
            elif userChoice==3:
                book = input('Enter the name of the book you want to add: ')
                library.addBook(book)
            #Return a book
            elif userChoice==4:
                book = input('Enter the name of the book you want to return: ')
                library.returnBook(book)
            #Show currently lent books and users
            elif userChoice==5:
                library.showLendedBooks()
            #Remove a book from the library
            elif userChoice==6:
                book = input('Enter the name of the book you want to remove: ')
                library.removeBook(book)
            #the user choose out of the option
            else:
                print('Please choose a valid option')

        #User choose Q
        elif userInput=="Q" or userInput=="q":
            break
        #User write the other words instead of Q and C
        else:
            print('Please enter a valid option')

#database
if __name__ == '__main__':
    
    #for display books in the library 
    booksList =[]
    dataBaseName = input('Enter the name of the database file with extension: ')
    bookDatabase = open(dataBaseName,'r')   #r => read mode
    for book in bookDatabase:
        booksList.append(book.strip())

    # for display books in lend section
    lendDict = {}
    lendDatabase = open('lendBook.txt', 'r')
    for line in lendDatabase:
        line = line.strip()  # Remove any leading/trailing whitespace
        if line:  # Check if the line is not empty
            # Ensure that the line has exactly 2 values (book, user)
            if ', ' in line:
                parts = line.split(', ')
                if len(parts) == 2:
                    book, user = parts
                    lendDict.update({book: user})
                else:
                    print(f"Skipping malformed line: {line}")
            else:
                print(f"Skipping malformed line (no comma): {line}")
    
    lendDatabase.close()

        
    #create object name " library "
    library = Library(booksList,'PythonX',lendDict)
    main()

