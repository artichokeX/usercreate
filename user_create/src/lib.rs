use rusqlite::{Connection, Result};

#[derive(Debug)]
pub struct User {
    pub id: i32,
    pub first_name: String,
    pub last_name: String,
    pub age: i32,
    pub department: String,
}


pub fn database(connection: &Connection) -> Result<()> {
    let conn = connection;

    conn.execute(
        "CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            age INTEGER,
            department TEXT
            )",
            (),
            )?;

    Ok(())
}

pub fn insert(connection: &Connection, fname: String, lname: String, age: i32, dept: String) -> Result<()> {
    let conn = connection;
    let insert = "INSERT INTO user (first_name, last_name, age, department) VALUES (?,?,?,?)";

    conn.execute(insert, (&fname, &lname, &age, &dept))?;

    Ok(())
}

pub fn remove(connection: &Connection, id: i32) -> Result<()> {
    let conn = connection;
    let remove = format!("DELETE FROM user WHERE ID = {}", &id);
    let command = remove.as_str();
    conn.execute(command, ())?;
    Ok(())
}

pub fn fetch(connection: &Connection) -> Result<()> {
    let conn = connection;
    let mut fetch = conn.prepare("SELECT * FROM user")?;

    let user_iter = fetch.query_map([], |row| {
        Ok(User {
            id: row.get(0)?,
            first_name: row.get(1)?,
            last_name: row.get(2)?,
            age: row.get(3)?,
            department: row.get(4)?
        })
    })?;

    for user in user_iter {
        println!("Found User {:?}", user.unwrap());
    }
    Ok(())
}
