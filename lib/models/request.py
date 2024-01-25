from models.__init__ import CURSOR, CONN
from models.owner import Owner
from models.art import Art
from models.exhibition import Exhibition


class Request:
    all = {}

    def __init__(self, art_id, owner_id, exhibition_name, approved, id=None):
        self.id = id
        self.art_id = art_id
        self.owner_id = owner_id
        self.exhibition_name = exhibition_name
        self.approved = approved

    def __repr__(self):
        return f"<Request {self.id}: Art {self.art_id.name}, Owner {self.owner_id.name}, Exhibition {self.exhibition_id.name}, Approved {self.approved}>"

    # @property
    # def art(self):
    #     return self.art_id

    # @art.setter
    # def art(self, art_id):
    #     if isinstance(art_id, int) and Art.find_by_id(art_id):
    #         self.art_id = art_id
    #     else:
    #         raise ValueError("art_id must reference an art in the database")

    # @property
    # def owner(self):
    #     return self.owner_id

    # @owner.setter
    # def owner(self, owner_id):
    #     if isinstance(owner_id, int) and Owner.find_by_id(owner_id):
    #         self.owner_id = owner_id
    #     else:
    #         raise ValueError("owner_id must reference an owner in the database")

    @property
    def exhibition(self):
        return self.exhibition_name

    @exhibition.setter
    def exhibition(self, exhibition_name):
        if isinstance(exhibition_name, str):
            self.exhibition_name = exhibition_name
        else:
            raise ValueError(
                "exhibition_name must reference an exhibition in the database"
            )

    @property
    def approved(self):
        return self._approved

    @approved.setter
    def approved(self, approved_val):
        print(approved_val)
        if isinstance(approved_val, int):
            self._approved = approved_val
        else:
            raise ValueError("approved must be an integer", type(approved_val))

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

    ####################### IGOR'S METHODS HERE
    @classmethod
    def instance_from_db(cls, row):
        """Return a Request object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        request = cls.all.get(row[0])
        if request:
            # ensure attributes match row values in case local object was modified
            request.art_id = row[1]
            request.owner_id = row[2]
            request.exhibition_name = row[3]
            request.approved = row[4]
        else:
            # not in dictionary, create new instance and add to dictionary
            request = cls(row[1], row[2], row[3], row[4])
            request.id = row[0]
            cls.all[request.id] = request
        return request

    @classmethod
    def get_all_requests_by_owner_id(cls, owner_id):
        """Return a list containing a Request object per row in the table"""
        sql = """
            SELECT *
            FROM requests
            WHERE owner_id = ?
        """

        rows = CURSOR.execute(sql, (owner_id,)).fetchall()
        # requests = [cls(row[1], row[2], row[3], row[4], id=row[0]) for row in rows]
        return rows

    @classmethod
    def get_all_not_approved_requests_by_owner_id(cls, owner_id):
        """Return a list containing a Request object per row in the table"""
        sql_query = """
            SELECT *
            FROM requests
            WHERE owner_id = ? AND approved = 0
        """

        rows = CURSOR.execute(sql_query, (owner_id,)).fetchall()
        # requests = [cls(row[1], row[2], row[3], row[4], id=row[0]) for row in rows]
        return rows

    @classmethod
    def get_all_request_details_by_request_id(cls, request_id):
        """Return a list containing a Request object per row in the table"""
        sql_query = """
            SELECT
                requests.id AS request_id,
                requests.exhibition_name,
                requests.approved,
                owners.name AS owner_name,
                arts.name AS art_name,
                arts.artist,
                museums.name AS museum_name,
                exhibitions.start_date,
                exhibitions.end_date
            FROM
                requests
            JOIN
                owners ON requests.owner_id = owners.id
            JOIN
                arts ON requests.art_id = arts.id
            JOIN
                exhibitions ON requests.exhibition_name = exhibitions.name
            JOIN
                museums ON exhibitions.museum_id = museums.id
            WHERE
                requests.id = ?;
            """

        row = CURSOR.execute(sql_query, (request_id,)).fetchone()
        # requests = [cls(row[1], row[2], row[3], row[4], id=row[0]) for row in rows]
        return row
