-- Crear la tabla Usuarios si no existe
CREATE TABLE IF NOT EXISTS Usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL
);

-- Insertar un registro en la tabla Usuarios
INSERT INTO Usuarios (nombre) VALUES ('Juan Pérez');
