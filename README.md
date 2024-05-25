this is my first project about use API for get more information about diferent species of animals.
json and sqlite files are done by concrete example of animal and API.py file is adjustable for any type of animal (animals whose information is avaliable in this web api)

now i want to talk about how to use my project. There are some new nuances. this code need some aspects to work correctly:
1. when u create new table in database this code(code which is used to create table) must be commented after using it one because table name is uniq and if we run table creating code again it raise error.
2. in this code are two user input valiables, when u select animal name in the first variable, then u must select the one species of first selected animal.
   for example:  if u select 'LION' in first user-input, then u must select lion's species in second user-input (for exaple: mountain lion or cave lion)
