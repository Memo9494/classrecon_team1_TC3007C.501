-- Tabla de Alumnos con restricción CHECK
CREATE TABLE IF NOT EXISTS alumnos (
    matricula VARCHAR(9) PRIMARY KEY CHECK (matricula LIKE 'A%'),
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    edad INT,
    carrera VARCHAR(255),
    num_participaciones INT DEFAULT 0,
    hr_inicio TIME,
    hr_fin TIME
);

-- Tabla de Profesores con restricción CHECK
CREATE TABLE IF NOT EXISTS profesores (
    matricula VARCHAR(9) PRIMARY KEY CHECK (matricula LIKE 'L%'),
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    edad INT
);

-- Tabla de Asistencia sin restricción de clave foránea
CREATE TABLE IF NOT EXISTS asistencia (
    asistencia_id INT PRIMARY KEY AUTO_INCREMENT,
    matricula VARCHAR(9) NOT NULL,
    tipo ENUM('Alumno', 'Profesor') NOT NULL,
    asistio BOOLEAN NOT NULL
);

-- Tabla de Participación (Solo para alumnos)
CREATE TABLE IF NOT EXISTS participacion (
    participacion_id INT PRIMARY KEY AUTO_INCREMENT,
    matricula VARCHAR(9) NOT NULL,
    fecha DATE,
    detalle TEXT,
    FOREIGN KEY (matricula) REFERENCES alumnos(matricula) ON DELETE CASCADE
);


