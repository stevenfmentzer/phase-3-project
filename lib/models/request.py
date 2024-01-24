from models.__init__ import CURSOR, CONN
from models.owner import Owner
from models.art import Art
from models.exhibition import Exhibition


class Request:
    all = []

    def __init__(self, art_id, owner_id, exhibition_name, approved, id=None):
        self.id = id
        self.art_id = art_id
        self.owner_id = owner_id
        self.exhibition_name = exhibition_name
        self.approved = approved

    def __repr__(self):
        return f"<Request {self.id}: Art {self.art_id.name}, Owner {self.owner_id.name}, Exhibition {self.exhibition_id.name}, Approved {self.approved}>"

    @property
    def art(self):
        return self._art_id

    @art.setter
    def art(self, art_id):
        if isinstance(art_id, int) and Art.find_by_id(art_id):
            self._art_id = art_id
        else:
            raise ValueError("art_id must reference an art in the database")

    @property
    def owner(self):
        return self._owner_id

    @owner.setter
    def owner(self, owner_id):
        if isinstance(owner_id, int) and Owner.find_by_id(owner_id):
            self._owner_id = owner_id
        else:
            raise ValueError("owner_id must reference an owner in the database")

    @property
    def exhibition(self):
        return self._exhibition_name

    @exhibition.setter
    def exhibition(self, exhibition_name):
        if isinstance(exhibition_name, str) and Exhibition.get_by_name(exhibition_name):
            self._exhibition_name = exhibition_name
        else:
            raise ValueError(
                "exhibition_name must reference an exhibition in the database"
            )

    @property
    def approved(self):
        return self._approved

    @approved.setter
    def approved(self, approved):
        if isinstance(approved, bool):
            self._approved = approved
        else:
            raise ValueError("approved must be a boolean")

    @classmethod
    def create_table(cls):
        # Create a new table requests
        sql = """
    CREATE TABLE IF NOT EXISTS requests (
    id INTEGER PRIMARY KEY,
    art_id INTEGER,
    owner_id INTEGER,
    exhibition_name TEXT,
    approved INTEGER, 
    FOREIGN KEY (art_id) REFERENCES arts(id),
    FOREIGN KEY (owner_id) REFERENCES owners(id)
    )
    """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        # Drop the table requests
        sql = """
    DROP TABLE IF EXISTS requests;
    """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
    INSERT INTO requests (art_id, owner_id, exhibition_name, approved)
    VALUES (?, ?, ?, ?)
    """

        CURSOR.execute(
            sql, (self.art_id, self.owner_id, self.exhibition_name, self.approved)
        )
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        # Update the request in DB
        sql = """
    UPDATE requests
    SET art_id = ?, owner_id = ?, exhibition_name = ?, approved = ?
    WHERE id = ?
    """
        CURSOR.execute(
            sql,
            (self.art_id, self.owner_id, self.exhibition_name, self.approved, self.id),
        )
        CONN.commit()

    def delete(self):
        # Delete the request from DB

        sql = """
    DELETE FROM requests
    WHERE id = ?
    """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, art_id, owner_id, exhibition_name, approved):
        # Initialize a new request instance and save it into the DB
        request = cls(art_id, owner_id, exhibition_name, approved)
        request.save()
        return request

    @classmethod
    def find_by_id(cls, id):
        # Return request by id
        sql = """
    SELECT *
    FROM requests
    WHERE id = ?
    """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    


    @classmethod
    def get_all(cls):
        """Return a list containing a Request object per row in the table"""
        sql = """
            SELECT *
            FROM requests
        """

        rows = CURSOR.execute(sql).fetchall()
        requests = [cls(row[1], row[2], row[3], row[4], id=row[0]) for row in rows]
        return requests
    @classmethod
    def find_by_museum_id(cls, id):
        # Return request by id
        sql = """
    SELECT *
    FROM requests
    WHERE id = ?
    """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def get_all(cls):
        """Return a list containing a Request object per row in the table"""
        sql = """
            SELECT *
            FROM requests
        """

        rows = CURSOR.execute(sql).fetchall()
        requests = [cls(row[1], row[2], row[3], row[4], id=row[0]) for row in rows]
        return requests

    @classmethod
    def find_by_museum_id(cls, id):
        # Return request by id
        sql = """
    SELECT *
    FROM requests
    WHERE id = ?
    """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
