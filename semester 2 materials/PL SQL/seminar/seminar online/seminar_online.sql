SET SERVEROUTPUT ON;

DECLARE
no_orders number := 0;

BEGIN
for i in 116..130 loop
select count(*) into no_orders
from orders
where customer_id = i;
exit when no_orders = 0;
dbms_output.put_line('The customer ' || i || ' has total of ' || no_orders || ' orders placed');
end loop;
END;
/

--testing
select customer_id, count(*) from orders where customer_id between 115 and 130 group by customer_id;
-------------------------------

-- using an index array, populate a ndarray(collection) with BULK COLLECT

DECLARE
TYPE dep_row IS RECORD (department_name varchar2(100), avg_sal number); 
--departments.department_name%type
TYPE ind_tab IS TABLE OF dep_row
INDEX BY PLS_INTEGER;
v_tab ind_tab;

BEGIN
SELECT department_name, round(avg(salary),2) avg_sal BULK COLLECT into v_tab 
FROM departments d  JOIN employees e ON d.department_id = e.department_id
GROUP BY department_name ORDER BY avg_sal desc;
DBMS_OUTPUT.PUT_LINE('No.of departments having payed employees ' || v_tab.count);
FOR i in v_tab.first..v_tab.last LOOP
DBMS_OUTPUT.PUT_LINE(v_tab(i).department_name || ' has the computed average salary: ' || v_tab(i).avg_sal);
END LOOP;
END;
/
-------------------------------
--FETCH FIRST/LAST rows CLAUSE -- starting with Oracle 12c
DECLARE
TYPE dep_row IS RECORD (department_name varchar2(100), avg_sal number); 
--departments.department_name%type
TYPE ind_tab IS TABLE OF dep_row
INDEX BY PLS_INTEGER;
v_tab ind_tab;

BEGIN
SELECT department_name, round(avg(salary),2) avg_sal BULK COLLECT into v_tab 
FROM departments d  JOIN employees e ON d.department_id = e.department_id
GROUP BY department_name ORDER BY avg_sal desc FETCH FIRST 5 ROWS ONLY;
DBMS_OUTPUT.PUT_LINE('No.of departments having payed employees ' || v_tab.count);
FOR i in v_tab.first..v_tab.last LOOP
DBMS_OUTPUT.PUT_LINE(v_tab(i).department_name || ' has the computed average salary: ' || v_tab(i).avg_sal);
END LOOP;
END;
/
-------------------------------

--CURSORS
DECLARE
no_rows number(2);

BEGIN
DELETE FROM product_information where product_id = 3114;
no_rows := SQL%ROWCOUNT;
DBMS_OUTPUT.PUT_LINE(no_rows || ' record deleted from the database!');
COMMIT;
END;
/
-------------------------------

select * from product_information where product_id = 3114;
select distinct category_id from product_information;
SELECT * FROM product_information p WHERE category_id = 24 
AND NOT EXISTS (SELECT 1 FROM ORDER_ITEMS oi WHERE p.product_id = oi.product_id);

begin
DELETE FROM product_information p WHERE category_id = 24 
AND NOT EXISTS (SELECT 1 FROM ORDER_ITEMS oi WHERE p.product_id = oi.product_id);
DBMS_OUTPUT.PUT_LINE(SQL%ROWCOUNT || ' deleted rows');
--ROLLBACK;
--DBMS_OUTPUT.PUT_LINE(SQL%ROWCOUNT || ' affected rows');
end;
/
