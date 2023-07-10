1. What function would you use to get the type of an object?

Write the name of the function in the file, without ().

2. How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without ().

3. In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = 100

4. In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = 89

5. In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = a

6. In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = a + 1

7. What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)

8. What do these 3 lines print?

>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)

9. What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)What do these 3 lines print?

10. What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)

11. What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)

12. What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)

13. What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)

14. What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)

15. What does this script print?

l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)

16. What does this script print?

l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)

17. What does this script print?

def increment(n):
    n += 1

a = 1
increment(a)
print(a)

18. What does this script print?

def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)

19. What does this script print?

def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)

20. Write a function def copy_list(l): that returns a copy of a list.

The input list can contain any type of objects
Your file should be maximum 3-line long (no documentation needed)
You are not allowed to import any module

21. a = ()
Is a a tuple? Answer with Yes or No

22. a = (1, 2)
Is a a tuple? Answer with Yes or No.

23. a = (1)
Is a a tuple? Answer with Yes or No.

24. a = (1, )
Is a a tuple? Answer with Yes or No.

25. What does this script print?

a = (1)
b = (1)
a is b

26. What does this script print?

a = (1, 2)
b = (1, 2)
a is b

27. What does this script print?

a = ()
b = ()
a is b

28. >>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
Will the last line of this script print 139926795932424? Answer with Yes or No.

29. >>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
Will the last line of this script print 139926795932424? Answer with Yes or No.