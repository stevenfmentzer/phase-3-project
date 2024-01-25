from models.__init__ import CURSOR, CONN
from datetime import datetime

class Art:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

class Request:
    def __init__(self, description, id=None):
        self.id = id
        self.description = description

class Exhibition:

    all = {}
    def __init__(self, name, art_id, museum_id, start_date, end_date, status=False, id=None):

        self.name = name
        self.art_id = art_id
        self.museum_id = museum_id
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else: 
            raise TypeError("")

    @property
    def art_id(self):
        return self._art_id

    @art_id.setter
    def art_id(self, value):
        if isinstance(value, int): 
            self._art_id = value

    @property
    def museum_id(self):
        return self._museum_id

    @museum_id.setter
    def museum_id(self, value):
        if isinstance(value, int):
            self._museum_id = value
        else: 
            raise TypeError("")

    @property
    def start_date(self):
        return self._start_date

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        date_format = "%Y-%m-%d"
        if isinstance(value, str) and len(value) > 0:
            try:
                datetime_object = datetime.strptime(value, date_format)
                self._start_date = value
            except ValueError as e:
                raise ValueError(f"Error parsing start date: {e}. Date must be in the format 'YYYY-MM-DD'.")
        else: 
            raise ValueError("Date must be a non-empty string in the format 'YYYY-MM-DD'.")

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        date_format = "%Y-%m-%d"
        if isinstance(value, str) and len(value) > 0:
            try:
                datetime_object = datetime.strptime(value, date_format)
                self._end_date = value
            except ValueError as e:
                raise ValueError(f"Error parsing end date: {e}. Date must be in the format 'YYYY-MM-DD'.")
        else: 
            raise ValueError("Date must be a non-empty string in the format 'YYYY-MM-DD'.")

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of exhibition instances """
        query = """
            CREATE TABLE IF NOT EXISTS exhibitions (
                id INTEGER PRIMARY KEY,
                name TEXT,
                art_id INTEGER,
                museum_id INTEGER, 
                start_date DATE,
                end_date DATE,
                status INTEGER,
                FOREIGN KEY (museum_id) REFERENCES museums(id),
                FOREIGN KEY (art_id) REFERENCES arts(id)
            )
        """
        CURSOR.execute(query)
        CONN.commit()

    @classmethod
    def create(cls, name, art_id, museum_id, start_date, end_date, status=False):
        """ Initialize a new exhibition instance, save the object to the database, and return it """
        exhibition = cls(name, art_id, museum_id, start_date, end_date, status)
        exhibition.save()
        return exhibition
    
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Exhibit instances """
        sql = """
            DROP TABLE IF EXISTS exhibitions;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert a new row for the current Exhibition instance into the 'exhibitions' table"""
        query = """
            INSERT INTO exhibitions (name, art_id, museum_id, start_date, end_date, status)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        CURSOR.execute(query, (self.name, self.art_id, self.museum_id, self.start_date, self.end_date, self.status))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self




    def update_by_name(self):
        """Update the all rows corresponding to the current Exhibition name."""
        sql = """
            UPDATE exhibitions
            SET name = ?, start_date = ?, end_date = ?, status = ? 
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.start_date, self.end_date, self.status, self.id))
        CONN.commit()




    @classmethod
    def get_all(cls):
        """ Return a list containing an exhibition object per row in the table """
        query = """
            SELECT *
            FROM exhibitions
        """
        rows = CURSOR.execute(query).fetchall()
        return set([cls.instance_from_db(row) for row in rows])

    @classmethod
    def get_by_name(cls, name):
        """ Return Exhibition object(s) with matching name """
        query = """
            SELECT *
            FROM exhibitions
            WHERE name is ?
        """
        rows = CURSOR.execute(query, (name,)).fetchall()
        return [cls.instance_from_db(row) for row in rows] if rows else None
    
    @classmethod
    def get_by_museum_id(cls, museum_id):
        """ Return Exhibition object(s) with matching museum_id """
        query = """
            SELECT *
            FROM exhibitions
            WHERE museum_id = ?
        """
        rows = CURSOR.execute(query, (museum_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows] if rows else None
    
    @classmethod
    def instance_from_db(cls, row):
        """Return an Exhibit object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        exhibit = cls.all.get(row[0])
        if exhibit:
            # ensure attributes match row values in case local object was modified
            exhibit.name = row[1]
            exhibit.art_id = row[2]
            exhibit.museum_id = row[3]
            exhibit.start_date = row[4]
            exhibit.end_date = row[5]
            exhibit.status = row[6]
        else:
            # not in dictionary, create new instance and add to dictionary
            exhibit = cls(row[1], row[2], row[3], row[4], row[5], row[6])
            exhibit.id = row[0]
            cls.all[exhibit.id] = exhibit
        return exhibit
    
