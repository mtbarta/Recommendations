import MySQLdb

class Database():
    def connect(self, host, user, passwd, db):
        self.db = MySQLdb.connect(host = host, 
                             port = 3306, 
                             user= user, 
                             passwd = passwd,
                             db = db)
        self.cursor = self.db.cursor();

    def get_ratings(self):
        try:
            self.cursor.execute("SELECT userid,itemid,rating "
                                "FROM ratings")
            return self.cursor.fetchall()
           
        except:
            print "database cursor not set for get_ratings() to read."\
                    "Please make sure Database.connect() is configured."
            return
        
        finally:
            self.cursor.close()
            self.db.close()
        
    def get_movie(self, movie):
        if self.cursor:
            return
        else:
            return