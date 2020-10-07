import sqlite3
import datetime
now = datetime.datetime.now()

def query(newVer):
    # Databases
    conn = sqlite3.connect("version.db")

    # Create cursor
    c = conn.cursor()

    # Create table
    # c.execute("""CREATE TABLE Version (
    #            Version text,
    #            Time text,
    #            Date text)""")

    # Insert into table
    c.execute("INSERT INTO version VALUES (:Version, :Time, :Date )",
              {
                  "Version": newVer,
                  "Time": f"{now.hour}:{now.minute}",
                  "Date": f"{now.day}-{now.month}-{now.year}"
              }
              )

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()