import mysql.connector

class Mysqls:
    def __init__(self, user='Aman', password='123456'):
        self.user = user
        self.password = password
        self.mydb = None

    
    def connect(self):
        try:
            print(f"Connecting to MySQL server with user={self.user}, password={self.password}")
            self.mydb = mysql.connector.connect(host='localhost', user=self.user, password=self.password)
            print("Connected successfully!")
        except mysql.connector.Error as err:
            print(f"Error connecting to the database: {err}")
            
    def close(self):
        if self.mydb:
            self.mydb.close()

    def insert_car_number(self, car_number):
        if not self.mydb:
            self.connect()
        try:
            mycursor = self.mydb.cursor()

            # Create the database if it doesn't exist
            mycursor.execute('CREATE DATABASE IF NOT EXISTS CAR_NUMBER_PLATE')

            # Use the database
            mycursor.execute('USE CAR_NUMBER_PLATE')

            # Create the table if it doesn't exist
            mycursor.execute('CREATE TABLE IF NOT EXISTS CAR_NUMBER (id INT AUTO_INCREMENT PRIMARY KEY, car_number VARCHAR(255))')

            # Insert the car number into the table
            sql = "INSERT INTO CAR_NUMBER (car_number) VALUES (%s)"
            val = (car_number,)
            mycursor.execute(sql, val)
            
            self.mydb.commit()  # Commit the changes
            print("Car number inserted successfully!")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if mycursor:
                mycursor.close()
            self.close()

    def select_car_numbers(self):
        if not self.mydb:
            self.connect()
        try:
            mycursor = self.mydb.cursor()

            # Select all car numbers from the table
            mycursor.execute("SELECT car_number FROM CAR_NUMBER")
            results = mycursor.fetchall()

            if results:
                print("Car numbers in the database:")
                for result in results:
                    print(result[0])
            else:
                print("No car numbers found in the database.")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if mycursor:
                mycursor.close()
            self.close()
