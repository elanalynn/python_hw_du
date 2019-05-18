# Stock and Bond Portfolio with SQLite Database

Elana Kopelevich
May 15, 2019

## Instructions
Use the assignment created in the previous lesson. Use the data you read into your data structures from the text files and write it to the database. You can use either the dictionary data structure or the class data structure you set up in previous assignments. Use the header names for database attribute names as you are setting up the database. In addition to those fields, add a investor_id field to the investor table, stock_id and the related investor_id field to the stock table, and bond_id and related investor_id to the bond table.

Write code that will retrieve the data into your data structures, and print it out, in the same format as we used in the previous assignments

## Running the Appliction
`main.py` is the application entry point.

To run: `python3 main.py`

This reads the files and writes to a SQLite database. I left in the report functionality, but had the report get its data from the database.

## Report
A new report (`report.txt`) is generated every time the app is run. 
