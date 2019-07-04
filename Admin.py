from datetime import datetime
import sys
with open("books_list.txt",'a+') as f:

    def add_books():
        number=int(input("enter the books to add to library"))
        for i in range(number):
            book_id=(input("enter the book id"))
            book_name=input("enter the book name")
            f.write("\n"),f.write(book_id),f.write(" ")
            f.write(book_name),f.write("\n")


    # add_books()
    def all_books():
        with open("books_list.txt", 'r') as f:
            for i in f:
                print(i,end="")






