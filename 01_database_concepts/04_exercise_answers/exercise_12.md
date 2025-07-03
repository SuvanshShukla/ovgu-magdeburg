# Database Concepts Exercise 12

Written By: Suvansh Shukla (matriculation number: 256245)

## Question 1

Prepare an entity-relationship schema to store information about insurance contracts:
A customer concludes policies with an insurance company. In the database,
all information about policies should be stored. Every policy has an identifying contract number,
an insurance number, a start and an end date. In addition,
every policy has at least one assignee (beneficiary). Every assignee insured with
a defined portion of the amount. Moreover, the payment date should be stored
if the insurance case occurs. Every assignee is a person. Additionally, the bank
account of the assignee must be stored. Moreover, the insurance subject, the
due date for dues and a status must be stored. A customer is a person that
has an address (first and last name, postal code, city) and contact information
(phone and email). In addition to the personal information, every customer
has a customer number. Some customers do not have a policy yet, but every
policy belongs to exactly one customer.

## Question 4

Given the following example database:

Table Customer:

| Cid | Name       |
| --- | ---------- |
| 13  | M. Mueller |
| 17  | A. Meier   |
| 23  | I. Schulze |

Table Dealer:

| Did | Name       |
| --  | --         |
| 5   | G. Hals    |
| 7   | P. Schmidt |
| 11  | E. Meier   |
| 13  | E. Mueller |

Table Product:

| Pid | Label         |
| --  | --            |
| 45  | Power Adapter |
| 57  | Cat5 Cable    |
| 67  | Mainboard     |

Offers table:

|Did|Pid|
|-- |-- |
|5  |45 |
|5  |57 |
|7  |67 |
|7  |45 |
|11 |57 |
|5  |67 |
|11 |67 |

Orders table:

|Oid|Did|Date       |Cid|
|-- |-- |--         |-- |
|3  |7  |0.1.12.2002|17 |
|5  |11 |27.04.2003 |23 |
|7  |5  |13.05.2003 |17 |
|10 |5  |01.09.2003 |13 |

Line_item table

|Oid|Pid|Amount|
|-- |-- |--    |
|3  |45 |1     |
|3  |67 |5     |
|5  |67 |5     |
|7  |57 |3     |
|7  |67 |2     |
|10 |45 |2     |
|10 |57 |5     |
|10 |67 |3     |

Formulate the following SQL queries:

(a) Create the orders table.

```SQL
create table orders (
    int oid primary key,
    date date,
    int did,
    int cid,
    foreign key(cid) references customer(cid),
    foreign key(did) references dealer(did)
);
```

(b) Find for each customer all products, that he has never ordered.

```SQL
select c.name, p.label
from customer c, orders o, linte_item l, products p;
minus 
select c.name, p.label 
from customer c inner join orders o on o.cid = c.cid 
inner join Line_item l on l.oid = o.oid 
inner join products p on p.pid = l.Pid
```

(c) Output pairs of customers that have bought at least one common Product.

```SQL

```

(d) Output dealer-IDs of those dealers that could have served/delivered all orders.

```SQL
select d.did from dealer d
inner join offers o on o.did = d.did
group by d.did 
having count(pid) = (select count(pid) from product);
```

(e) Find all dealer-IDs of those dealers, who could have served the orders of customer I.Schulze.

```SQL
select d.did from dealer d 
inner join offers o on o.did = d.did 
where pid = (
    select pid from Line_item l
    inner join orders ord on ord.oid = l.oid 
    inner join customer c on c.cid = ord.cid 
    where c.name = 'I. Schulze'
);
```

(f) Add an order from A.Meier containing all available articles once, from a dealer able to fulfill this order.

```SQL

```

