from yoyo import read_migrations, get_backend

backend = get_backend('postgres://postgres:erl@localhost/testdb')
migrations = read_migrations('./migration')
backend.apply_migrations(backend.to_apply(migrations))
