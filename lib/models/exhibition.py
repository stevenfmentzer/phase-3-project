##Steven
from models.__init__ import CURSOR, CONN
from datetime import datetime

class Art:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Request:
    def __init__(self, id, description):
        self.id = id
        self.description = description

class Exhibition:

    all = {}
    __all_names = set()
    
    def __init__(self, name, art_id, museum_id, start_date, end_date, status = False, id=None):

        self.id = id
        self.name = name
        self.art_id = art_id
        self.museum_id = museum_id
        self.start_date = start_date
        self.end_date = end_date
        self.status = status

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            ## Must be changed if to allow updating instance
            if value not in Exhibition.__all_names:
                Exhibition.__all_names.add(value)
                self._name = value
            else: 
                raise Exception("This exhibition name already exists. Please choose another name.")
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

    @start_date.setter
    def start_date(self, value):
        date_format = "%Y-%m-%d"
        if isinstance(value, str) and len(value) > 0:
            try:
                datetime_object = datetime.strptime(value, date_format)
                self._start_date = datetime_object
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
                self._end_date = datetime_object
            except ValueError as e:
                raise ValueError(f"Error parsing end date: {e}. Date must be in the format 'YYYY-MM-DD'.")
        else: 
            raise ValueError("Date must be a non-empty string in the format 'YYYY-MM-DD'.")


    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if isinstance(value, bool):
            self._status = value
        else: 
            raise TypeError("")

    ##---------    

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
        exhibition = cls(name=name, art_id=art_id, museum_id=museum_id, start_date=start_date, end_date=end_date, status=status)
        exhibition.save()
        return exhibition

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists exhibition instances """
        query = """
            DROP TABLE IF EXISTS exhibitions;
        """
        CURSOR.execute(query)
        CONN.commit()

    
    def save(self):
        """Insert a new row for the current Exhibition instance into the 'exhibitions' table"""
        query = """
            INSERT INTO exhibitions (name, art_id, museum_id, start_date, end_date, status)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        # Execute the main query to insert exhibition details
        CURSOR.execute(query, (str(self._name), int(self._art_id), int(self._museum_id), str(self._start_date), str(self._end_date), int(self._status)))
        CONN.commit()

        # Get the id of the newly inserted row
        exhibition_id = CURSOR.lastrowid

        CONN.commit()

    @classmethod
    def get_all(cls):
        """ Return a list containing a exhibition object per row in the table """
        query = """
            SELECT *
            FROM exhibitions
        """
        rows = CURSOR.execute(query).fetchall()
        return set([cls.instance_from_db(row) for row in rows])
    
    @classmethod
    def get_by_name(cls, name):
        """ Return an Exhibition object with matching name """
        query = """
            SELECT *
            FROM exhibitions
            WHERE exhibitions.name = ?
        """
        rows = CURSOR.execute(query, (name,)).fetchall()
        return cls.instance_from_db(rows[0]) if rows else None
    
    # @classmethod
    # def get_all_art(cls, exhibition_id):
    #     """Retrieve all art associated with a specific exhibition."""
    #     query = """
    #         SELECT art.*
    #         FROM art
    #         JOIN exhibition_art ON art.id = exhibition_art.art_id
    #         WHERE exhibition_art.exhibition_id = ?
    #     """
    #     rows = CURSOR.execute(query, (exhibition_id,)).fetchall()
    #     return [Art.instance_from_db(row) for row in rows]

    # @classmethod
    # def get_all_requests(cls, exhibition_id):
    #     """Retrieve all requests associated with a specific exhibition."""
    #     query = """
    #         SELECT request.*
    #         FROM request
    #         JOIN exhibition_request ON request.id = exhibition_request.request_id
    #         WHERE exhibition_request.exhibition_id = ?
    #     """
    #     rows = CURSOR.execute(query, (exhibition_id,)).fetchall()
    #     return [Request.instance_from_db(row) for row in rows]
    


    # def update(self):
    #     """Update the table row corresponding to the current exhibition instance."""
    #     query = """
    #         UPDATE exhibitions
    #         SET name = ?
    #         WHERE id = ?
    #     """
    #     CURSOR.execute(query, (self.name, self.id))
    #     CONN.commit()
    

    # def delete(self):
    #     """Delete the table row corresponding to the current Exhibition instance,
    #     delete the dictionary entry, and reassign id attribute"""
    #     query = """
    #         DELETE FROM departments
    #         WHERE id = ?
    #     """
    #     CURSOR.execute(query, (self.id,))
    #     CONN.commit()

    #     # Delete the dictionary entry using id as the key
    #     del type(self).all[self.id]

    #     # Set the id to None
    #     self.id = None