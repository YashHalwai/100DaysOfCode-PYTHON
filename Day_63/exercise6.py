# Exercise 6 - Library Management System in Python | Python Tutorial - Day #64

# https://www.youtube.com/watch?v=mlDZTSH2FFc&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=64

class Library:
  books = ["Warrior's Dream", "Ethiopia Knight"]
  noofbooks = 2

  def __init__(self):
    if(self.noofbooks != len(self.books)):
      print('Your program has got some error fix it.')
            

  def show(self):
    print(self.books)
    print('Total books: ',self.noofbooks)

  def add(self, bookName):
    self.books.append(bookName)
    self.noofbooks += 1

  def delete(self, bookName):
    self.books.remove(bookName)
    self.noofbooks -= 1

    
book = Library()
#Adds a book
book.add("Safeena's Kitchen")
book.show()
#Deletes a book
book.delete("Warrior's Dream")
book.show()