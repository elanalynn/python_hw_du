import sqlite3

dogs = [
    {"dogId": 1, "dogName": "Fido", "dogAge": 1, "dogBreed": "Greyhound", "ownerId": 2},
    {"dogId": 2, "dogName": "Sparky", "dogAge": 4, "dogBreed": "Boxer", "ownerId": 3},
    {"dogId": 3, "dogName": "Bella", "dogAge": 6, "dogBreed": "Lab", "ownerId": 3},
    {"dogId": 4, "dogName": "Maggy", "dogAge": 7, "dogBreed": "Lab", "ownerId": 1},
    {"dogId": 5, "dogName": "Spot", "dogAge": 2, "dogBreed": "mutt", "ownerId": 2},
]
owners = [
    {"ownerId": 1, "ownerFName": "Harry", "ownerLName": "Potter"},
    {"ownerId": 2, "ownerFName": "Hermoine", "ownerLName": "Granger"},
    {"ownerId": 3, "ownerFName": "Ron", "ownerLName": "Weasley"},
]

conn = sqlite3.connect("dogs.db")
print("Created database successfully")

conn.execute(
    """CREATE TABLE dogs(
    dogId       INT         PRIMARY KEY     NOT NULL,
    dogName     TEXT                        NOT NULL,
    dogAge      INT                         NOT NULL,
    dogBreed    TEXT                        NOT NULL,
    ownerId     TEXT                        NOT NULL
);"""
)

conn.execute(
    """CREATE TABLE owners(
    ownerId     INT         PRIMARY KEY     NOT NULL,
    ownerFName  TEXT                        NOT NULL,
    ownerLName  TEXT                        NOT NULL
);"""
)

print("Tables created successfully")

for dog in dogs:
    print(dog)
    conn.execute(
        "INSERT INTO dogs (dogId, dogName, dogAge, dogBreed, ownerId) VALUES (?, ?, ?, ?, ?)",
        (dog["dogId"], dog["dogName"], dog["dogAge"], dog["dogBreed"], dog["ownerId"]),
    )

for owner in owners:
    conn.execute(
        "INSERT INTO owners (ownerId, ownerFName, ownerLName) VALUES (?, ?, ?)",
        (owner["ownerId"], owner["ownerFName"], owner["ownerLName"]),
    )

conn.commit()
print("Records created successfully")

conn.close()
