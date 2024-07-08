-- Crear la tabla Usuarios si no existe (solo como referencia, si no está creada aún)
CREATE TABLE IF NOT EXISTS Usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL
);

-- Insertar algunos datos de ejemplo
INSERT INTO Usuarios (nombre) VALUES ('Usuario1'), ('Usuario2'), ('Usuario3');

-- Seleccionar todos los registros de la tabla Usuarios
SELECT * FROM Usuarios;
