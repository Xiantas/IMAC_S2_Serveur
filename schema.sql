CREATE TABLE IF NOT EXISTS stocks (
    id_produit INTEGER PRIMARY KEY AUTOINCREMENT,
    nom_produit TEXT,
    quantite INTEGER NOT NULL,
    prix FLOAT NOT NULL 
);

CREATE TABLE IF NOT EXISTS orders (
    id_order INTEGER PRIMARY KEY AUTOINCREMENT,
    id_client INTEGER NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    prix_total FLOAT,
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
    id_order INTEGER NOT NULL,
    id_produit INTEGER NOT NULL ,
    PRIMARY KEY(id_order , id_produit),
    FOREIGN KEY(id_order) REFERENCES orders (id_order),
    FOREIGN KEY(id_produit) REFERENCES stocks (id_produit)

);

INSERT INTO stocks 
VALUES 
(NULL,"Cheesebuger", 10, 6.50),
(NULL,"Burger Classique", 10, 6.00),
(NULL,"Bacon Burger", 10, 7.00),
(NULL,"BiggiMac", 10 ,6.00),
(NULL,"Burger Végé" , 10 , 6.00),
(NULL,"Sandwich Jambon-Emmental", 10, 5.00),
(NULL,"Sandwich Crudités", 10, 5.00),
(NULL,"Sandwich Rosette Beurre", 10, 5.00),
(NULL,"Frites", 10 ,3.50),
(NULL,"Potatoes" , 10 , 3.50),
(NULL,"Salade", 10, 4.00),
(NULL,"Chips", 10, 2.00),
(NULL,"Tiramisu", 10 ,3.00),
(NULL,"Glace chocolat" , 10 , 2.00),
(NULL,"Glace vanille", 10, 2.00),
(NULL,"Glace fraise", 10, 2.00),
(NULL,"Brownie", 10, 2.00),
(NULL,"Cookie", 10, 2.00),
(NULL,"Eau" , 10 , 1.00),
(NULL,"Thé", 10, 1.00),
(NULL,"Coca-Cola", 10 ,1.50),
(NULL,"7up", 10, 1.50),
(NULL,"Jus d'orange", 10 ,1.50),
(NULL,"Jus multifruits", 10 ,1.50);

INSERT INTO clients VALUES (NULL, "Joe", "joedalton@shrug.com", "Dalton", "prison")
/*
INSERT INTO orders (0,0)
*/
