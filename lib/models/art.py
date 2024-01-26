from models.__init__ import CURSOR, CONN
from models.owner import Owner


class Art:
    all = {}

    def __init__(self, owner_id, name, artist, cost, id=None):
        self.id = id
        self.owner_id = owner_id
        self.name = name
        self.artist = artist
        self.cost = cost
        
    def __repr__(self):
        owner_name = Owner.find_by_id(self.owner_id).name

        return (
            f"<Art {self.id}: {self.name}, Artist: {self.artist}, Cost: {self.cost} "
            + f"Owner: {owner_name} >"
        )
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )
    @property
    def artist(self):
        return self._artist
    @artist.setter
    def artist(self, artist):
        if isinstance(artist, str) and len(artist):
            self._artist = artist
        else:
            raise ValueError(
                "Artist must be a non-empty string"
            )
    @property
    def cost(self):
        return self._cost
    @cost.setter
    def cost(self, cost):
        if isinstance(cost, int) and cost > 0:
            self._cost = cost
        else:
            raise ValueError("Cost must be greater than zero")
    
    @property
    def owner_id(self):
        return self._owner_id
    @owner_id.setter
    def owner_id(self, owner_id):
        if Owner.find_by_id(owner_id):
            self._owner_id = owner_id
        else:
            raise ValueError(
                "owner_id must reference a owner in the database")
    

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of art instances """
        sql = """
            CREATE TABLE IF NOT EXISTS arts (
            id INTEGER PRIMARY KEY,
            owner_id INTEGER,
            name TEXT,
            artist TEXT,
            cost INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Art instances """
        sql = """
            DROP TABLE IF EXISTS arts;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        
        sql = """
                INSERT INTO arts (owner_id, name, artist, cost)
                VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.owner_id, self.name, self.artist, self.cost))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Art instance."""
        sql = """
            UPDATE arts
            SET owner_id = ?, name = ?, artist = ?, cost = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.owner_id, self.name,
                             self.artist, self.cost, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Art instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM arts
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None


    @classmethod
    def create(cls, owner_id, name, artist, cost):
        """ Initialize a new art instance and save the object to the database """
        owner = Owner.find_by_id(owner_id)
        if owner:
            art = cls(owner_id, name, artist, cost)
            art.save()
            return art
        else:
            raise ValueError("owner_id must reference an owner in the database")

    
    @classmethod
    def instance_from_db(cls, row):
        """Return an Art object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        art = cls.all.get(row[0])
        if art:
            # ensure attributes match row values in case local instance was modified
            art.owner_id = row[1]
            art.name = row[2]
            art.artist = row[3]
            art.cost = row[4]
        else:
            # not in dictionary, create new instance and add to dictionary
            art = cls(row[1], row[2], row[3], row[4])
            art.id = row[0]
            cls.all[art.id] = art
        return art
    @classmethod
    def get_all(cls):
        """Return a list containing one Art object per table row"""
        sql = """
            SELECT *
            FROM arts
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """Return Art object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM arts
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        """Return Art object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM arts
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def find_owner(self):
        owner_name = Owner.find_by_id(self.owner_id).name
        return owner_name

    
# ipdb.set_trace()

    
