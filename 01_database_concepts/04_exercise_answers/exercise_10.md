# Database Concepts Exercise 10

## Tables

Customer Table:

|Cid|Name|
|--|--|
|13|M.Mueller|
|17|A.Meier|
|23|I.Schulze|

Dealer table:

|Did|Name|
|---|---|
|5|G.Hals|
|7|P.Schmidt|
|11|E.Meier|
|13|E.Mueller|

Product table;

|Pid|Label|
|--|--|
|45|Power adapter|
|57|Cat5 cable|
|67|Mainboard|

Offers table:

|Did|Pid|
|--|--|
|5|45|
|5|57|
|7|67|
|7|45|
|11|57|
|5|67|
|11|67|

Orders table:

|Oid|Did|Date|Cid|
|--|--|--|--|
|3|7|0.1.12.2002|17|
|5|11|27.04.2003|23|
|7|5|13.05.2003|17|
|10|5|01.09.2003|13|

Line_item table

|Oid|Pid|Amount|
|--|--|--|
|3|45|1|
|3|67|5|
|5|67|5|
|7|57|3|
|7|67|2|
|10|45|2|
|10|57|5|
|10|67|3|

## Question 1. Express following queries in SQL!

a. Get the names of all customers.

```SQL
select name from customer;
```

b. Get all orders of customer Meier.

```SQL
select * from customer join orders on oid = cid 
where name like '%Meier';
```

c. List all products that have not been sold on 13.05.2003.

```SQL
select p.* from product p join line_item l on p.pid = l.pid 
join orders o on o.oid = l.oid 
where o.date != '13.05.2003';
```

d. List all products that dealer Meier sold to customer Schulze.

```SQL
select p.* from product p join line_item l on p.pid = l.pid 
join orders o on o.oid = l.oid 
join customer c on c.cid = o.oid 
join dealer d on d.did = o.did 
where d.name like '%Meier' and c.name like '%Schulze';
```

e. Get all products that dealer Meier sold and customer Schulze bought.

```SQL
select p.* from product p join line_item l on p.pid = l.pid 
join orders o on o.oid = l.oid 
join customer c on c.cid = o.oid 
join dealer d on d.did = o.did 
where d.name like '%Meier' or c.name like '%Schulze';
```

## Question 2. Describe the following queries in SQL!

(a) Get the label of all products that are ordered more than twice.

```SQL
select p.label from product p join line_item l on l.pid = p.pid 
group by l.pid, p.label;
```

(b) Which customers (name) haven't ordered anything?

```SQL
select c.name from orders o left outer join customer c on c.cid = o.oid;
```

(c) For all dealers (name), list the products (label) that they do not offer.
(d) Output the products (label) sorted by total SalesPerProduct.
(e) Output the name of all dealers and their respective orders (if no order exists, fill these entries with NULL)!

