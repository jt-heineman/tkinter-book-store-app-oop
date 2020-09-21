import sqlite3

class Database:

    def __init__(self,db):
        self.conn=sqlite3.connect(db) #if db does not exist, it is created
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)") # REAL -> float
        self.conn.commit()   
        #conn.close() # comment the close to make it open

    def view(self):
        #conn=sqlite3.connect("books.db") #already created while init
        #cur=conn.cursor()
        self.cur.execute("SELECT * FROM book") 
        tableresult=self.cur.fetchall() 
        #self.conn.close()
        return tableresult
    
    def insert(self, title, author, year, isbn):
        #conn=sqlite3.connect("books.db") 
        #cur=conn.cursor()
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title, author, year, isbn))
        self.conn.commit()
        #self.conn.close()

    def search(self, title="", author="", year="", isbn=""): #passing empty strings as default values
        #conn=sqlite3.connect("books.db") 
        #cur=conn.cursor()
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title, author, year, isbn)) #not best practice in production environment, allow injections
        tableresult=self.cur.fetchall() #returned as a List[]
        #self.conn.close()
        return tableresult

    def delete(self, id): #expects the id, generated once user select item in the list, and list generate a tuple with id 
        #conn=sqlite3.connect("books.db")
        #cur=conn.cursor()
        self.cur.execute("DELETE FROM book WHERE id=?",(id,)) #extra comma needed 
        self.conn.commit()
        #self.conn.close()

    #def update(id, title="", author="", year="", isbn=""):
    def update(self, id, title, author, year, isbn):
        #conn=sqlite3.connect("books.db") #if db does not exist, it is created
        #cur=conn.cursor()
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title, author, year,isbn,id)) #extra comma needed 
        self.conn.commit()
        #self.conn.close()

    def __del__(self):
        self.conn.close()

   