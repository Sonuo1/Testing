import mysql.connector
import os

# Retrieve environment variables
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

try:
    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host=db_host,
        port=db_port,
        database=db_name,
        user=db_user,
        password=db_password
    )

    cursor = connection.cursor()

    # Sample data insertion
    data = {
        'name': 'John Doe',
        'email': 'john@example.com'
    }

    insert_query = "INSERT INTO your_table_name (name, email) VALUES (%(name)s, %(email)s)"
    cursor.execute(insert_query, data)

    # Commit the changes
    connection.commit()

    print("Data inserted successfully")

except mysql.connector.Error as error:
    print("Error inserting data:", error)

finally:
    # Close the cursor and connection
    if connection:
        cursor.close()
        connection.close()
