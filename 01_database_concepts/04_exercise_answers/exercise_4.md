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

## 2. Which possibilities does the DDL provide to guarantee referential integrity in case of deletes or updates?

## 3. Given the following relational schema of the database found in the appendix:
## Customer (Cid, Name) offers (Did -> Dealer, Pid -> Product) 
## Dealer (Did, Name) Orders (Oid, Did -> Dealer, Date, Cid -> Customer) 
## Product (Pid, Label) line item (Oid -> Orders, Pid -> Product, Amount) 
## For each query on the given database instance: 
## (i) show the result and (ii) trans- late it into a query that non-databasers would give and understand. Example: SELECT Address FROM Inhabitant ->  Get the addresses of all inhabitants.

### (a) π OID (Line item)

`select oid from line_item;` -> Get all order IDs from line item table.

### (b) π Name (Dealer ⨝ Orders)

`select name from dealer join orders;` -> Get all names from the result when we fetch all rows from the dealer table that has the same `Did` as the rows in the orders table.

### (c) π Did (Dealer) - π Did (offers)

```sql
select did from dealer
where did not in (
    select did from offers
);
```

This means to get all the Did values from the dealer table that are not present in the offers table.

### (d) π Date ((σ Date<01.03.2003 (Orders) ∪ (σ Date>01.05.2003 (Orders))))

```sql
select date from orders
where date < to_date(01.03.2003)
union
select date from orders
where date > to_date(01.05.2003);
```

This means to fetch all the dates from the orders table where orders are before 01.03.2003 and after 01.05.2003.

### (e) Customer ⨝ Orders ⨝ line_item ⨝ Product

```sql
select * from customer
join orders join line_item
join product;
```

This means to fetch all rows and columns from tables, customer and orders by matching `Cid` then join orders and line items by matching `Oid` then join line item and product by matching `Pid`.

## 4. Given the relational schema in task 3. Express the following queries using relational algebra!

### (a) Get the names of all customers.

π name (customer)

### (b) Get all orders of customer Meier.

orders ⨝ (σ name=Meier (customer)) 

### (c) List all products that have not been sold on 13.05.2003.

σ(product) - σ date=13.05.2003 (product)

### (d) List all products that dealer Meier sold to customer Schulze.

products ⨝ line_item ⨝ ((σ name=Meier (dealer)) ⨝ orders ⨝ (σ name=Schulze (customer)))

products ⨝ line_item ⨝ (σ did=(π did (σ name=Meier (dealer)))(orders) ∪ σ cid=(π cid (σ name=Schulze (customer)))(orders))

```sql
select * from products 
join line_item 
join orders
where orders.did in (select did from dealer where name = 'Meier')
and orders.cid in (select cid from customer where name = 'Schulze');
```
