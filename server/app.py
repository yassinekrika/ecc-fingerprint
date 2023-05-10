# Backend app
from flask import Flask, request
import mysql.connector

# Create a Flask app
app = Flask(__name__)

# Create a mysql connection object
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="yassg4mer",
        password="1234567890",
        database="fingerprint"
    )
except mysql.connector.Error as e:
    print(e)

# Create a cursor object to execute queries
cursor = conn.cursor()

# Define a route to handle post requests
@app.route("/post", methods=["POST"])
def post():
    # Get the data from the request body
    data = request.get_json()

    # Print the data
    # print(data)

    # Insert the data into the mysql table
    sql = "INSERT INTO user (id, username, fingerprint) VALUES (NULL, %s, %s)"
    val = (data["username"], data["fingerprint"])
    cursor.execute(sql, val)
    conn.commit()

    # Return a success message
    return "Post request received and handled successfully!"

# Run the app
if __name__ == "__main__":
    app.run()