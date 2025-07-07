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

![entity-relationship-diagram](./exercise12-images/dbc-exe-12-ques-1-erd.svg)

## Question 2 

Transfer the entity-relationship schemata from Task 1 into the relational schema!

Relational Schema:

```
policy(<u>contract_no</u>, insurance_no, start_date, end_date)
assignee(status, bank_account, amount, payment_date, insurance_subject, due_date)
customer(<u>customer_no</u>, first_name, last_name, postal_code, city, email, phone)
person()
```

## Question 3 

Given the relation R(ABCDE) with the following functional dependencies: 

` A → B, AB → C, A → C, B → A, C → D, D → E `

Find systematically all keys and transform the relation step-wise into the BCNF.   
Is the schema in BCNF dependency preserving?    

Left:   
Middle: A, B, C, D  
Right: E  

Anything containing A and B will be a key.  
No combination of any other elements (without A and/or B) will be able to be a key.   

1<sup>st</sup> Normal Form:  
R(A,B,C,D,E)  

2<sup>nd</sup> Normal Form:     
R(A,B), R(A,C,D,E)

3<sup>rd</sup> Normal From:     
R(A,B), R(A,C), R(C,D), R(D,E)

BCNF Normal Form:   
R(A), R(B), R(A,C), R(C,D), R(D,E)

The schema in BCNF is not dependency preserving, as the functional dependency of `A -> B` and `B -> A` is lost.

## Question 4

Given the following example database:

Table Customer:

| Cid | Name       |
|-----|------------|
| 13  | M. Mueller |
| 17  | A. Meier   |
| 23  | I. Schulze |

Table Dealer:

| Did | Name       |
|-----|------------|
| 5   | G. Hals    |
| 7   | P. Schmidt |
| 11  | E. Meier   |
| 13  | E. Mueller |

Table Product:

| Pid | Label         |
|-----|---------------|
| 45  | Power Adapter |
| 57  | Cat5 Cable    |
| 67  | Mainboard     |

Offers table:

|Did|Pid|
|---|---|
|5  |45 |
|5  |57 |
|7  |67 |
|7  |45 |
|11 |57 |
|5  |67 |
|11 |67 |

Orders table:

|Oid|Did|Date       |Cid|
|---|---|-----------|---|
|3  |7  |0.1.12.2002|17 |
|5  |11 |27.04.2003 |23 |
|7  |5  |13.05.2003 |17 |
|10 |5  |01.09.2003 |13 |

Line_item table

|Oid|Pid|Amount|
|---|---|------|
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
with cust1 as ( 
    select name, pid from customer c 
    inner join orders o on o.cid = c.cid
    inner join line_item l on l.oid = o.oid 
) select distinct(a.name, b.name) from customer a 
inner join orders ord on ord.cid = a.cid 
inner join line_item l on l.oid = ord.oid
inner join cust1 b on b.pid = l.pid
where a.name != b.name;
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

## Question 5 
`⨝ , Π, σ, ⟕ , ∈, Ύ`

Formulate the following queries in relational algebra:  

(a) Output all orders from customer M.Mueller.

Π <sub>(oid,did,date,cid)</sub> σ<sub>(name='M.Mueller')</sub> (orders ⟕ <sub>(orders.cid=customer.cid)</sub> customer)

(b) Find all items ordered on days other than 13.05.2003.

Π <sub>(pid,label)</sub> (product ⨝ line_item ⨝ orders) - Π <sub>(pid,label)</sub> σ<sub>(orders.date='13.05.2003')</sub> (product ⨝ line_item ⨝ orders)

(c) Find all customers who have ordered more than one power supply.

Π <sub>(cid, name)</sub> σ <sub>(pid='45')</sub> Ύ <sub>(product,count(pid)>1)</sub> (product ⨝ line_item ⨝ orders)

(d) Find all dealers who offer a mainboard, but have not yet sold one.

Π <sub>(did, name)</sub> σ <sub>(pid='67')</sub> 

## Question 6

Formulate each of the following queries in tuple as well as domain calculus:

(a) The names of all customers.

{ x.name | x ∈ customer }

(b) Orders from customer Meier.

{ x | x ∈ orders ∧ u ∈ customer ∧ x.cid = u.cid ∧ u.name='A.Meier' }

(c) Which dealers offer Cat5 cables?

{ x | x ∈ dealer ∧ u ∈ offers ∧ x.did=u.did ∧ u.pid=57 }

(d) Which customers (name) have not placed orders?

{ x.name | x ∈ customer ∧ u ∈ orders ∧ x.cid=u.cid ∧ u.cid=NULL }
