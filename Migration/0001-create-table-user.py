from yoyo import step

step(
    "CREATE TABLE usuarios ( \
        user_id Serial, \
        dt_nascimento varchar(20) NOT NULL, \
        nome varchar(30) NOT NULL, \
        user_cpf varchar(11) NOT NULL, \
        user_pass varchar(255) NOT NULL, \
        PRIMARY KEY (user_id)\
    )",
    "DROP TABLE `usuarios`",
)
