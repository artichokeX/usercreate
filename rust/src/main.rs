use anyhow::Result;
use dialoguer::Input;
use rusqlite::Connection;

fn main() -> Result<()>{
    let conn = Connection::open("./user.db")?;
    user_create::database(&conn)?;
    let fname = Input::<String>::new()
        .with_prompt("Enter Users First Name")
        .interact_text()?;

    let lname = Input::<String>::new()
        .with_prompt("Enter Users Last Name")
        .interact_text()?;
    
    let age = Input::<i32>::new()
        .with_prompt("Enter Users Age")
        .interact_text()?;

    let dept = Input::<String>::new()
        .with_prompt("Enter Users Department")
        .interact_text()?;

    user_create::insert(&conn, fname, lname, age, dept)?;

    user_create::fetch(&conn)?;
    Ok(())
}
