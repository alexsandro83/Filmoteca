CREATE TABLE generos (
    id_genero INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL UNIQUE,
    descricao TEXT
);
CREATE TABLE filmes (
    id_filme INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(100) NOT NULL,
    diretor VARCHAR(100) NOT NULL,
    ano_lancamento INT NOT NULL,
    duracao INT NOT NULL,
    quantidade_estoque INT DEFAULT 1,
    quantidade_total INT DEFAULT 1,
    genero_id INT NOT NULL,
    FOREIGN KEY (genero_id) REFERENCES generos(id_genero)
);
CREATE TABLE filme_ator (
    id_filme_ator INT PRIMARY KEY AUTO_INCREMENT,
    filme_id INT NOT NULL,
    ator_id INT NOT NULL,
    personagem VARCHAR(100),
    FOREIGN KEY (filme_id) REFERENCES filmes(id_filme),
    FOREIGN KEY (ator_id) REFERENCES atores(id_ator),
    UNIQUE KEY unique_filme_ator (filme_id, ator_id)
);