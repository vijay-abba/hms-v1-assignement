


1. If I have a table (Eg: department) already have some data inside it 
it has a duplicate values in department_name now if we alter it to accept only 
unique values then what happens to old records and will it execute ? 

ANSWEER:
    If you try to add a UNIQUE constraint to a column that already contains duplicates, the operation will fail, and no changes will be made to your table structure.


2. I am using rich package for color printing 
   instead of using ColPt("message", style="red")
   i ahve used a class called ColPrint: inside added methods red and green 
   and import and using simply ColPrint.red("message"), 
   So does this effect python performance ? 

Answer:
    The short answer is no, it will not affect your performance in any noticeable way. In fact, what you have done is actually a highly praised software engineering practice! You have created what is called a Wrapper or Helper Class, and it shows your evaluators that you understand the DRY Principle (Don't Repeat Yourself).