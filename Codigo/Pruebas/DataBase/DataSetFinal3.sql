-- Tablas principales
CREATE TABLE alumnos (
    matricula1 INT PRIMARY KEY ,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL, 
	carrera VARCHAR(255) NOT NULL,
    hora_de_inicio TIME, 
    hora_de_FIN TIME
);

CREATE TABLE profesores (
	matricula2 INT PRIMARY KEY ,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    edad INT
    
);

-- Tablas relacionales
CREATE TABLE participacion (
    participacion_id INT PRIMARY KEY AUTO_INCREMENT,
    fecha DATE NOT NULL,
    comentario VARCHAR(500) NOT NULL,
    alumno_id INT,
    FOREIGN KEY (alumno_id) REFERENCES alumnos(matricula1)
);

CREATE TABLE asistencia (
    asistencia_id INT PRIMARY KEY AUTO_INCREMENT,
    fecha DATE NOT NULL,
    matricula INT NOT NULL,
    asistio BOOLEAN NOT NULL,
    tipo ENUM('alumno', 'profesor') NOT NULL,
    FOREIGN KEY (matricula) REFERENCES alumnos(matricula1) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (matricula) REFERENCES profesores(matricula2) ON DELETE CASCADE ON UPDATE CASCADE
);




