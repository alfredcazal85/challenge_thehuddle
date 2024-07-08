-- Crear la tabla Usuarios si no existe (solo como referencia, si no está creada aún)
CREATE TABLE IF NOT EXISTS Usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL
);

-- Insertar algunos datos de ejemplo
INSERT INTO Usuarios (nombre) VALUES ('Usuario1'), ('Usuario2'), ('Usuario3');

-- Actualizar el nombre del usuario con id = 1 a 'NuevoNombre'
UPDATE Usuarios
SET nombre = 'NuevoNombre'
WHERE id = 1;

-- Verificar que se ha actualizado correctamente
SELECT * FROM Usuarios;
