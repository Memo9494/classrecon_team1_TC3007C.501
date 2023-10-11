-- Tablas principales
CREATE TABLE alumnos (
    alumno_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL
);

CREATE TABLE profesores (
    profesor_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL
);

-- Tablas relacionales
CREATE TABLE participacion (
    participacion_id INT PRIMARY KEY AUTO_INCREMENT,
    fecha DATE NOT NULL,
    comentario VARCHAR(500) NOT NULL,
    alumno_id INT,
    FOREIGN KEY (alumno_id) REFERENCES alumnos(alumno_id)
);

CREATE TABLE asistencia (
    asistencia_id INT PRIMARY KEY AUTO_INCREMENT,
    fecha DATE NOT NULL,
    asistio BOOLEAN NOT NULL,
    alumno_id INT,
    profesor_id INT,
    FOREIGN KEY (alumno_id) REFERENCES alumnos(alumno_id),
    FOREIGN KEY (profesor_id) REFERENCES profesores(profesor_id)
);

