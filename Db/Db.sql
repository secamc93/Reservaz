

-- Creación de la tabla Vehiculo
CREATE TABLE Vehiculo (
    ID              INT IDENTITY(1,1) PRIMARY KEY,
    Placa           VARCHAR(50),
    Modelo          VARCHAR(50),
    Marca           VARCHAR(50),
    Capacidad       INT,
    Pais            VARCHAR(100),
    UNIQUE(Placa, Pais)
);

-- Creación de la tabla Conductor
CREATE TABLE Conductor (
    ID              INT IDENTITY(1,1) PRIMARY KEY,
    DNI             INT UNIQUE,
    Nombre          VARCHAR(50),
    Apellidos       VARCHAR(50),
    Telefono        VARCHAR(15),
    Correo          VARCHAR(50),
    Pais            VARCHAR(50),
    UNIQUE(DNI, Pais)
);

-- Creación de la tabla Ruta
CREATE TABLE Ruta (
    ID              INT IDENTITY(1,1) PRIMARY KEY,
    Nombre          VARCHAR(100),
    Origen          VARCHAR(50),
    Destino         VARCHAR(50),
    Pais            VARCHAR(50)
    UNIQUE(Nombre, Origen, Destino, Pais)
);

--Creacion tabla grupo vehiculos conductores y ruta
CREATE TABLE Grupo (
    ID              INT IDENTITY(1,1) PRIMARY KEY,
    FK_Ruta         INT FOREIGN KEY REFERENCES Ruta(ID),
    FK_Vehiculo     INT FOREIGN KEY REFERENCES Vehiculo(ID),
    FK_Conductor    INT FOREIGN KEY REFERENCES Conductor(ID)
)

-- Creación de la tabla Viajes
CREATE TABLE Viaje (
    ID              INT IDENTITY(1,1) PRIMARY KEY,
    FK_Ruta         INT FOREIGN KEY REFERENCES Ruta(ID),
    FechaViaje      DATETIME,
    Pais            VARCHAR(50)
);

-- Creación de la tabla Pasajeros
CREATE TABLE Pasajero (
    ID              INT IDENTITY(1,1) PRIMARY KEY,
    DNI             INT,
    Nombre          VARCHAR(100),
    Correo          VARCHAR(50),
    Pais            VARCHAR(50),
    UNIQUE(DNI, Pais)
);

--Creacion tabla reservas 
CREATE TABLE Reserva (
    ID              INT IDENTITY(1,1) PRIMARY KEY,
    FK_Viaje        INT FOREIGN KEY REFERENCES Viaje(ID),
    FK_Pasajero     INT FOREIGN KEY REFERENCES Pasajero(ID),
    Fecha           DATETIME
);

-- Insertar registros en la tabla Vehiculo
INSERT INTO Vehiculo (Placa, Modelo, Marca, Capacidad, Pais)
VALUES
    ('ABC123', 'Sedan', 'Toyota', 5, 'USA'),
    ('DEF456', 'SUV', 'Ford', 7, 'USA'),
    ('GHI789', 'Hatchback', 'Honda', 4, 'USA'),
    ('JKL012', 'Sedan', 'Nissan', 5, 'USA'),
    ('MNO345', 'SUV', 'Chevrolet', 7, 'USA');

-- Insertar registros en la tabla Conductor
INSERT INTO Conductor (DNI, Nombre, Apellidos, Telefono, Correo, Pais)
VALUES
    (123456789, 'Juan', 'Perez', '123456789', 'juan.perez@example.com', 'USA'),
    (987654321, 'Maria', 'Lopez', '987654321', 'maria.lopez@example.com', 'USA');

-- Insertar registros en la tabla Ruta
INSERT INTO Ruta (Nombre, Origen, Destino, Pais)
VALUES
    ('Ruta 1', 'Ciudad A', 'Ciudad B', 'USA'),
    ('Ruta 2', 'Ciudad C', 'Ciudad D', 'USA');

-- Insertar registros en la tabla Grupo
INSERT INTO Grupo (FK_Ruta, FK_Vehiculo, FK_Conductor)
VALUES
    (1, 1, 1),
    (2, 2, 2);

-- Insertar registros en la tabla Viaje
INSERT INTO Viaje (FK_Ruta, FechaViaje, Pais)
VALUES
    (1, '2023-06-10 10:00:00', 'USA'),
    (2, '2023-06-11 15:30:00', 'USA');

-- Insertar registros en la tabla Pasajero
INSERT INTO Pasajero (DNI, Nombre, Correo, Pais)
VALUES
    (111111111, 'Pedro', 'pedro@example.com', 'USA'),
    (222222222, 'Ana', 'ana@example.com', 'USA');

-- Insertar registros en la tabla Reserva
INSERT INTO Reserva (FK_Viaje, FK_Pasajero, Fecha)
VALUES
    (1, 1, '2023-06-09 09:00:00'),
    (1, 2, '2023-06-09 09:30:00'),
    (2, 1, '2023-06-10 13:00:00'),
    (2, 2, '2023-06-10 14:00:00');
