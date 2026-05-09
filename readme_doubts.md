


1. If I have a table (Eg: department) already have some data inside it 
it has a duplicate values in department_name now if we alter it to accept only 
unique values then what happens to old records and will it execute ? 

ANSWEER:
    If you try to add a UNIQUE constraint to a column that already contains duplicates, the operation will fail, and no changes will be made to your table structure.


