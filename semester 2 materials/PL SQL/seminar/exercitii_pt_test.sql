SET SERVEROUTPUT ON;


--Exercise 1: Credit Risk Category
--Write a PL/SQL block that takes a customer ID and classifies the customer's credit limit:
--If CREDIT_LIMIT ≥ 10,000 → print "HIGH"
--If between 5,000 and 9,999 → "MEDIUM"
--Otherwise → "LOW"
DECLARE
v_customer_id CUSTOMERS.customer_id%type;
v_customer_credit_limit CUSTOMERS.credit_limit%type;
BEGIN
SELECT credit_limit INTO v_customer_credit_limit FROM CUSTOMERS WHERE customer_id = v_customer_id;
IF v_customer_credit_limit >= 10000 THEN
dbms_output.put_line('HIGH');
ELSIF v_customer_credit_limit between 5000 and 9999 THEN
dbms_output.put_line('MEDIUM');
ELSE dbms_output.put_line('LOW');
END IF;
EXCEPTION
WHEN NO_DATA_FOUND THEN
dbms_output.put_line('Customer not found.');
END;
/


--Exercise 2: Recent Orders Printer
--Task:
--Write a PL/SQL block that:
--Selects the 5 most recent orders (ORDER_ID) from the ORDERS table.
--Uses a loop to print each ORDER_ID.
BEGIN
FOR rec IN (
SELECT ORDER_ID FROM ORDERS 
ORDER BY ORDER_DATE DESC 
FETCH FIRST 5 ROWS ONLY
) 
LOOP
dbms_output.put_line('Order ID: ' || rec.order_id);
END LOOP;
END;
/


--Write a PL/SQL block that:
--Declares a cursor to select EMPLOYEE_ID, LAST_NAME, and DEPARTMENT_ID from the EMPLOYEES table.
--Filters only employees where DEPARTMENT_ID = 60.
--Loops through the cursor and prints each employee's info.
DECLARE
cursor myCursor is SELECT employee_id, first_name, last_name, department_id from EMPLOYEES
WHERE department_id = 60;
v_employee_id EMPLOYEES.employee_id%type;
v_employee_first_name EMPLOYEES.first_name%type;
v_employee_last_name EMPLOYEES.last_name%type;
v_department_id EMPLOYEES.department_id%type;
BEGIN
dbms_output.put_line('Info about employees in department 60: ');
open myCursor;
LOOP
fetch myCursor into v_employee_id, v_employee_first_name, v_employee_last_name, v_department_id;
EXIT WHEN myCursor%NOTFOUND;
dbms_output.put_line('Name: ' || v_employee_first_name || ' ' || v_employee_last_name);
dbms_output.put_line('ID: ' || v_employee_id);
dbms_output.put_line('Department ID: ' || v_department_id);
END LOOP;
END;
/


--Exercise 4: Handle Missing Customer
--Task:
--Write a PL/SQL block that:
--Accepts a CUSTOMER_ID (you can hardcode or prompt).
--Attempts to retrieve the customer’s CUST_FIRST_NAME from the CUSTOMERS table.
--If found, prints the name.
--If the customer does not exist, catch the exception and print "Customer not found."
DECLARE
v_customer_id CUSTOMERS.customer_id%type := &p;
v_cust_first_name CUSTOMERS.cust_first_name%type;
BEGIN
SELECT cust_first_name INTO v_cust_first_name 
FROM CUSTOMERS WHERE customer_id = v_customer_id;
dbms_output.put_line('Customer first name: ' || v_cust_first_name);
EXCEPTION
WHEN NO_DATA_FOUND THEN
dbms_output.put_line('No customer found.');
END;
/


--Exercise 5: Procedure to Print Customer Email
--Write a procedure named PRINT_CUST_EMAIL that:
--Takes a CUSTOMER_ID as a parameter.
--Prints the customer's email (CUST_EMAIL).
--If no such customer, prints "No such customer".
CREATE OR REPLACE PROCEDURE 
print_customer_email(
p_customer_id IN CUSTOMERS.customer_id%type, 
p_customer_email OUT CUSTOMERS.cust_email%type
)
IS
BEGIN
SELECT cust_email into p_customer_email
FROM CUSTOMERS 
WHERE customer_id = p_customer_id;
EXCEPTION
WHEN NO_DATA_FOUND THEN
dbms_output.put_line('No such customer');
END;












