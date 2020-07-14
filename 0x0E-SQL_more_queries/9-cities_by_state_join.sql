-- Write a script that lists all cities contained in the database hbtn_0d_usa.
SELECT c.id, c.name, s.name  FROM states s JOIN cities c ON c.state_id = s.id order by c.id;
