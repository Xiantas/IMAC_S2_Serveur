CREATE TABLE IF NOT EXISTS stocks (
    id_ingredient INTEGER PRIMARY KEY AUTOINCREMENT,
    nom_ingredient TEXT,
    quantite INTEGER NOT NULL,
    prix FLOAT NOT NULL 
);

CREATE TABLE IF NOT EXISTS orders (
    id_order INTEGER PRIMARY KEY AUTOINCREMENT,
    id_client INTEGER NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(id_client) REFERENCES clients (id_client)
);

CREATE TABLE IF NOT EXISTS clients (
    id_client INTEGER PRIMARY KEY AUTOINCREMENT,
    nom_client TEXT,
    adresse_mail TEXT,
    mdp TEXT,
    adresse TEXT
);

CREATE TABLE IF NOT EXISTS orderparts (
    id_order INTEGER NOT NULL ,
    id_ingredient INTEGER NOT NULL ,
    PRIMARY KEY(id_order , id_ingredient),
    FOREIGN KEY(id_order) REFERENCES orders (id_order),
    FOREIGN KEY(id_ingredient) REFERENCES stocks (id_ingredient)

);

INSERT INTO stocks 
VALUES 
(1,"viande", 10, 12.89),
(2,"pain", 10, 12.89),
(3,"salade", 10, 12.89),
(4,"tomate", 10 ,13.5),
(5,"tamère" , 1 , 0.5);

INSERT INTO clients(NULL)
INSERT INTO orders (0,0)

