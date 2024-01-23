##Steven
from models.__init__ import CURSOR, CONN

class Museum:

    all = {}

    def __init__(self, name, id=None):
        
        self.id = id
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 2: 
            if not hasattr(self, 'name'):
                self._name = value
            else: 
                raise Exception("name is already set and can't be changed.")
        else: 
            raise TypeError("name must be type 'string' and be at least three characters long")


    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of museum instances """
        query = """
            CREATE TABLE IF NOT EXISTS museums (
            id INTEGER PRIMARY KEY,
            name TEXT)
        """
        CURSOR.execute(query)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists museum instances """
        query = """
            DROP TABLE IF EXISTS museums;
        """
        CURSOR.execute(query)
        CONN.commit()


    def save(self):
        """Insert a new row for the current Museum instance into the 'museums' table"""
        query = """
            INSERT INTO museums (name) VALUES (?)
        """
        CURSOR.execute(query, (self.name,))
        CONN.commit()


    @classmethod
    def create(cls, name):
        """ Initialize a new museum instance and save the object to the database """
        museum = cls(name)
        museum.save()
        return museum
    
    
    def update(self):
        """Update the table row corresponding to the current museum instance."""
        query = """
            UPDATE museums
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(query, (self.name, self.id))
        CONN.commit()
    

    def delete(self):
        """Delete the table row corresponding to the current Museum instance,
        delete the dictionary entry, and reassign id attribute"""
        query = """
            DELETE FROM departments
            WHERE id = ?
        """
        CURSOR.execute(query, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def get_all(cls):
        """Return a list containing a museum object per row in the table"""
        query = """
            SELECT *
            FROM museums
        """
        rows = CURSOR.execute(query).fetchall()
        return [cls.instance_from_db(row) for row in rows]