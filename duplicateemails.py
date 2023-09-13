from Person
select Email
group by Email
having count(*) > 1
