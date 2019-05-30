# Stock and Bond Portfolio with SQLite Database

Elana Kopelevich
May 15, 2019

## Instructions
Import the values from the JSON file (AllStocks.json) for the stocks in the portfolio. The stock quotes included in the JSON file start with the purchase dates of the stock, so not all start dates are the same, so you will need to create different date lists to associate with the stock prices.

Graph (with a simple line graph) the stock prices. Show the dates on the x-axis of the graph. For this graph use the closing price. Given that the value of Google is so high the other lines of the graph may appear fairly flat and low.


## Dependencies
- pygal (`pip3 install pygal`)

## Running the Appliction
`main.py` is the application entry point.

To run: `python3 main.py`

This reads the files and writes to a SQLite database. I left in the report functionality, but had the report get its data from the database.

## Report
A new SVG (`AllStock.svg`) is generated every time the app is run. 
