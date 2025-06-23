# POSTGRESQL Notes

## When we can effectively use alias for a column in PostgreSQL

| Use Case                  | PostgreSQL Support                |
| ------------------------- | --------------------------------- |
| `ORDER BY alias_name`     | ✅ Yes                            |
| `WHERE alias_name = ...`  | ❌ No                             |
| `GROUP BY alias_name`     | ✅ Yes (PostgreSQL supports this) |
| `HAVING alias_name > ...` | ❌ No (use expression again)      |

### Why this works

In PostgreSQL, you can reference a column alias in the ORDER BY clause — the query planner recognizes it after the SELECT list is processed.

So:
- operating_hours is defined in the SELECT clause.
- PostgreSQL remembers this alias.
- ORDER BY operating_hours is valid and will sort by the computed value of that expression.

## Seeing what tables there are in your DB using SQL queries

Just use the below query:

```sql 
SELECT
    table_schema || '.' || table_name
FROM
    information_schema.tables
WHERE
    table_type = 'BASE TABLE'
AND
    table_schema NOT IN ('pg_catalog', 'information_schema');
```

