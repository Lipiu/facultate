SET SERVEROUTPUT ON;
-- create a procedure that modifies the salary of all employees 
--if their salary is larger than the average salary

CREATE OR REPLACE
PROCEDURE upd_avg(p_avg_salary IN OUT NUMBER)
IS
CURSOR c IS
SELECT employee_id, salary
FROM employees
WHERE salary > p_avg_salary;
BEGIN
FOR var IN c LOOP
update_sal(var.employee_id, 10);
END LOOP;
SELECT AVG(salary) INTO p_avg_salary
FROM employees;
END;
/

--The call:
DECLARE
v_avg_salary number;
BEGIN
SELECT AVG(salary) INTO v_avg_salary from employees;
dbms_output.put_line('The initial AVERAGE salary: '||round(v_avg_salary));
upd_avg(v_avg_salary);
dbms_output.put_line('The final AVERAGE salary: '||round(v_avg_salary,10));
END;
/
