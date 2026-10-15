CREATE DATABASE login_system_db;

-- Conéctate a la base de datos login_system_db en DBeaver antes de ejecutar la tabla
CREATE TABLE users (
    id_user SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    passw VARCHAR(50) NOT NULL,
    nombre VARCHAR(100) NOT NULL
);

INSERT INTO users (username, passw, nombre) 
VALUES ('admin', 'admin!123', 'Super admin');