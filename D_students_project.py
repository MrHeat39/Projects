NumBook = int(input("Enter how many books you have: "))
Books = []
pages = []

for i in range(NumBook):
    NameOfBook = input(f"give me name of the book {i+1}: ")
    NumberOFpages = int(input("give me how many pages in this book: "))
    
    Books.append(NameOfBook)
    pages.append(NumberOFpages)

def Mid(pages):
    return sum(pages) / len(pages)

Books.sort()
pages.sort()

print(Books)
print(pages)