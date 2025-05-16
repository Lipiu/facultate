SET SERVEROUTPUT ON

DECLARE
v_list_price product_information.list_price%type;

BEGIN
SELECT list_price INTO v_list_price FROM product_information WHERE product_id = &p;
DBMS_OUTPUT.PUT_LINE('Initial price was: ' || v_list_price);
IF v_list_price < 350 THEN
    v_list_price := 1.1 * v_list_price;
ELSIF v_list_price BETWEEN 350 and 900 THEN
    v_list_price := 1.2 * v_list_price;
ELSE
    v_list_price := 1.5 * v_list_price;
END IF;
dbms_output.put_line('Final price is: ' || v_list_price);
END;
/

DECLARE
grade number;
Begin
IF grade<5 THEN
dbms_output.put_line('Sorry');
ELSE
dbms_output.put_line('Congrats');
END IF;
END;
/ 

-- solved using CASE
DECLARE
v_list_price product_information.list_price%type;

BEGIN
SELECT list_price INTO v_list_price FROM product_information WHERE product_id = &p;
DBMS_OUTPUT.PUT_LINE('Initial price was: ' || v_list_price);
v_list_price := CASE 
WHEN v_list_price < 350 THEN 1.1 * v_list_price
WHEN v_list_price BETWEEN 350 AND 900 THEN 1.2 * v_list_price
ELSE 1.5 * v_list_price
END;
dbms_output.put_line('Final price is: ' || v_list_price);
END;
/

-- LOOPS
DECLARE
v_nr NUMBER(2) := 10;
i NUMBER(2) := 1;

BEGIN
LOOP
v_nr := v_nr - i;
i := i + 1;
EXIT WHEN v_nr < 0;
dbms_output.put_line(v_nr);
END LOOP;
END;
/

--Display in ascending order the employees with the id between 100-110 if their salary is lower
--than the average
DECLARE
v_salary_employees employees.salary%type;
v_avg_salary v_salary_employees%type;
i number(4) := 100;

BEGIN
SELECT AVG(salary) into v_avg_salary from employees;
dbms_output.put_line('The average salary is: ' || v_avg_salary);
LOOP
SELECT salary INTO v_salary_employees FROM employees WHERE employee_id = i;
IF v_salary_employees <= v_avg_salary THEN
dbms_output.put_line('The employee with the id ' || i || ' has the salary ' || v_salary_employees);
END IF;
i := i + 1;
EXIT WHEN i > 110;
END LOOP;
END;
/

--WHILE
DECLARE
v_salary_employees employees.salary%type;
v_avg_salary v_salary_employees%type;
i number(4) := 100;

BEGIN
SELECT AVG(salary) into v_avg_salary from employees;
dbms_output.put_line('The average salary is: ' || v_avg_salary);
WHILE i <= 110 LOOP
SELECT salary INTO v_salary_employees FROM employees WHERE employee_id = i;
IF v_salary_employees <= v_avg_salary THEN
dbms_output.put_line('The employee with the id ' || i || ' has the salary ' || v_salary_employees);
END IF;
i := i + 1;
END LOOP;
END;
/

--FOR LOOP
DECLARE
v_salary_employees employees.salary%type;
v_avg_salary v_salary_employees%type;

BEGIN
SELECT AVG(salary) into v_avg_salary from employees;
dbms_output.put_line('The average salary is: ' || v_avg_salary);
for i in 100..110 LOOP
SELECT salary INTO v_salary_employees FROM employees WHERE employee_id = i;
IF v_salary_employees <= v_avg_salary THEN
dbms_output.put_line('The employee with the id ' || i || ' has the salary ' || v_salary_employees);
END IF;
END LOOP;
END;
/

--Load in the MESSAGES table numbers from 1…50 excpetiong the numbers 16 şi 7.
CREATE TABLE MESSAGES(REZ VARCHAR2(10))
BEGIN
for i in 1..50 loop
if i = 16 or i = 7 then
null;
else
insert into MESSAGES(REZ) values(i);
end if;
commit;
end loop;
END;
/
