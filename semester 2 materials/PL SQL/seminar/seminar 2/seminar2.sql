--solve this by taking value from keyboard
SET SERVEROUTPUT ON
DECLARE
    a NUMBER := 17;
    b NUMBER := 3;
    sum1 NUMBER;
    
BEGIN
    sum1 := a + b;
    dbms_output.put_line(sum1);
END;
/


declare
m decimal; -- echivalent m NUMBER(38,0)
n float; -- echivalent n NUMBER
begin
m:=100.20;
dbms_output.put_line('m='||m);
n:=100.20;
dbms_output.put_line('n='||n);
End;
/ 


declare
z signtype;
begin
z:=0;
dbms_output.put_line('z='||z);
End;
/


DECLARE
v_last_name VARCHAR2(50);
BEGIN
    SELECT last_name INTO v_last_name FROM employees WHERE employee_id = 100;
    dbms_output.put_line('The employee with id 100 is Mr. ' || v_last_name);
END;
/


DECLARE
    v_last_name customers.CUST_last_name%TYPE;
    v_first_name customers.CUST_first_name%TYPE;
BEGIN
    SELECT cust_first_name, cust_last_name into v_first_name, v_last_name from customers where customer_id = 222;
    dbms_output.put_line('The customer with id 222 is: ' || v_first_name || ' ' || v_last_name);
END;
/

VARIABLE n number
BEGIN
select count(*) into :n
from orders
where order_mode = 'online';
END;
/
PRINT n
 -- Question: What’s the result?
begin
:n:=:n+5;
dbms_output.put_line('n='||:n);
 -- N=?
 :n:=:n+3;
dbms_output.put_line('n='||:n);
 -- N=?
end;
/ 
PRINT n


SET SERVEROUTPUT ON
VARIABLE g_price number
BEGIN
select round(avg(unit_price),2) into :g_price
from order_items
where product_id = 3133;
END;
/
select * from order_items where unit_price <= :g_price;



