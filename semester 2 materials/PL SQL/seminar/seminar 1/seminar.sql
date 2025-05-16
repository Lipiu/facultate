SET SERVEROUTPUT ON

DECLARE
v_message VARCHAR2(100);
BEGIN
v_message := 'Hello from the PL/SQL universe';

--if DBMS_OUTPUT.PUT_LINE IS greyed out it means it works properly.
DBMS_OUTPUT.PUT_LINE(v_message);
END;
/