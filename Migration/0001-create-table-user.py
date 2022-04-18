from yoyo import step
step(
    "CREATE TABLE `usuarios` (\
        `user_id` int(11) NOT NULL AUTO_INCREMENT, \
        `dt_nascimento` datetime NOT NULL, \
        `nome` varchar(30) NOT NULL, \
        `user_cpf` varchar(11) NOT NULL, \
        `user_pass` varchar(255) NOT NULL, \
        PRIMARY KEY (`user_id`) \
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8",
    "DROP TABLE `usuarios`",
)
