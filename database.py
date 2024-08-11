import sqlite3
conn = sqlite3.connect("laptopdata.db")

conn.execute("""
                create table laptoprecord(
                    brand varchar(30),
                    category varchar(30),
                    touch_screen varchar(30),
                    operating_system varchar(30),
                    processor_brand varchar(30),
                    processor_name varchar(30),
                    architecture varchar(30),
                    generation varchar(30),
                    ram varchar(30),
                    ssd varchar(30)
                    )
            """)

print("Table successfully created in database!")

conn.commit()
conn.close