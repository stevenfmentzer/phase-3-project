# from __init__ import CURSOR, CONN
from models.__init__ import CURSOR, CONN

class Owner:

    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    def __repr__(self):
        return f"<Owner {self.id}: {self.name}>"

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of owner instances """
        sql = """
            CREATE TABLE IF NOT EXISTS owners (
            id INTEGER PRIMARY KEY,
            name TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Owner instances """
        sql = """
            DROP TABLE IF EXISTS owners;
        """
        CURSOR.execute(sql)
        CONN.commit()


    def save(self):
        """ Insert a new row with the name values of the current Owner instance.
        Update object id attribute using the primary key value of new row.
        """
        sql = """
            INSERT INTO owners (name)
            VALUES (?)
        """

        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name):
        """ Initialize a new Owner instance and save the object to the database """
        owner = cls(name)
        owner.save()
        return owner
    
    
    def update(self):
        """Update the table row corresponding to the current Owner instance."""
        sql = """
            UPDATE owners
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()
    

    def delete(self):
        """Delete the table row corresponding to the current Owner instance"""
        sql = """
            DELETE FROM owners
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()