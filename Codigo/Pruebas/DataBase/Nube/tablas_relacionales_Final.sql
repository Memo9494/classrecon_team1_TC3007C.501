-- Tabla general para matrículas
CREATE TABLE personas (
    matricula VARCHAR(9) PRIMARY KEY,
    tipo ENUM('alumno', 'profesor') NOT NULL
);

-- Tablas principales
CREATE TABLE alumnos (
    matricula1 VARCHAR(9) PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL, 
	carrera VARCHAR(255) NOT NULL,
    hora_de_inicio TIME, 
    hora_de_FIN TIME,
    FOREIGN KEY (matricula1) REFERENCES personas(matricula) ON DELETE CASCADE
);

CREATE TABLE profesores (
	matricula2 VARCHAR(9) PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    edad INT,
    FOREIGN KEY (matricula2) REFERENCES personas(matricula) ON DELETE CASCADE
);

-- Tablas relacionales
CREATE TABLE participacion (
    participacion_id INT PRIMARY KEY AUTO_INCREMENT,
    fecha DATE NOT NULL,
    comentario VARCHAR(500) NOT NULL,
    alumno_id VARCHAR(9),
    FOREIGN KEY (alumno_id) REFERENCES alumnos(matricula1) ON DELETE CASCADE
);

CREATE TABLE asistencia (
    asistencia_id INT PRIMARY KEY AUTO_INCREMENT,
    fecha DATE NOT NULL,
    matricula VARCHAR(9) NOT NULL,
    asistio BOOLEAN NOT NULL,
    tipo ENUM('alumno', 'profesor') NOT NULL,
    FOREIGN KEY (matricula) REFERENCES personas(matricula) ON DELETE CASCADE
);
