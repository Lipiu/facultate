set serveroutput on;

DECLARE
type p_type is record (v_code product_information.product_id%type not null:=2500, 
                       v_name product_information.product_name%type, 
                       v_min_price product_information.min_price%type);
vrec_prod p_type;

BEGIN
select product_id, product_name, min_price 
into vrec_prod 
from product_information 
where product_id = 2761;
dbms_output.put_line('Product: ' || vrec_prod.v_name || ' has the minimum price of: ' || vrec_prod.v_min_price);
END;
/
---------------------------

DECLARE
vrec_prod product_information%rowtype;

BEGIN
select product_name, min_price -- or select *
into vrec_prod.product_name, vrec_prod.min_price -- if use * here is only vrec_prod
from product_information 
where product_id = 2761;
dbms_output.put_line('Product: ' || vrec_prod.product_name || ' has the minimum price of: ' || vrec_prod.min_price);
END;
/
---------------------------

DECLARE
vrec_dpt departments%rowtype;
i number(2) := 10;

BEGIN
LOOP
select * 
into vrec_dpt 
from departments
where department_id = i;
dbms_output.put_line('Deparment: ' || vrec_dpt.department_id || ' ---> ' || vrec_dpt.department_name);
EXIT WHEN i >= 50;
i := i + 10; -- i :=+ 10
END LOOP;
END;
/
---------------------------

DECLARE
type emp_table is table of employees%rowtype index by pls_integer;
v_tab emp_table;

BEGIN
--loading the data in the array
for i in 100..120 loop
select * into v_tab(i)
from employees
where employee_id = i;
end loop;

--extracting the data from the array
for i in v_tab.first..v_tab.last loop
dbms_output.put_line('Employee: ' || v_tab(i).first_name || ' ' || v_tab(i).last_name || ' works in the department' || v_tab(i).department_id);
end loop;
dbms_output.put_line('Total employees in the indexed array: ' || v_tab.count);
END;
/