"""
user:recoDBuser
db: recoDB
pwd: recopwd
"""

import MySQLdb

class Database():
    def connect(self, host, user, passwd, db):
        db = MySQLdb.connect(host = host, 
                             port = 3306, 
                             user= user, 
                             passwd = passwd,
                             db = db)
        self.cursor = db.cursor();

    def get_ratings(self):
        if self.cursor:
            self.cursor.execute("SELECT userid,itemid,rating "
                                "FROM ratings")
            return self.cursor.fetchall()
           
        else:
            return
        
    def get_movie(self, movie):
        if self.cursor:
            return
        else:
            return