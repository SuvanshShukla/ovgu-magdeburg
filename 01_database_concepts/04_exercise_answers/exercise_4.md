# Exercise 4

## 1. Create the tables for the relations RECOMMENDS and MADE FROM. Assume that the relation GRAPE, DISH, and CRITIC already exist. Guarantee referential integrity through value propagation due to UPDATE operations. For more information about the relationships of relations, see the example database in the appendix.

```sql
create table recommends (
    String dish_name,
    String critic_name,
    String wine_name,
    primary key(dish_name, critic_name, wine_name),
    foreign key(dish_name) references dish(name),
    foreign key(cirtic_name) references cirtic(name),
    foreign key(wine_name) references wine(name)
);

create table made_from (
    float proportion,
    String grape_name,
    String wine_name,
    primary key(grape_name, wine_name),
    foreign key(grape_name) references grape(name),
    foreign key(wine_name) references wine(name)
);
```
