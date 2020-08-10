# Session4

## Numeric Types II


This assignment targets on writing a Qualean class which is inspired by Boolean+Quantum concepts.

We can assign it only 3 possible real states. True, False, and maybe (1, 0, -1) but it internally picks an imaginary state. 

As soon as you assign a real number it takes a imaginary number which is randomly generated from code random.uniform(-1,1) i.e. a number randomly generated between -1 and 1 is multiplied by the real number passed by the user.

Then it is rounded off to the 10th decimal place using Banker's rounding and then finally we store this particular number . Banker's rounding is implemented in python so don't require to write any new round function.

Following are the functions which are defined inside the Qualean class.



### Functions used in Qualean class

Following are the functions which are defined inside the Qualean class.

- ```__str__``` : This method returns the str object of value of the Qualean object mentioned.
- ```__repr__``` :This method returns the representation of the Qualean object and the value it contains in a nicely formatted string.
- ```__and__```:  This magic method implements the logical AND Operation for the user defined Qualean objects.
- ```__eq__``` : Equality is implemented for objects of Qualean type and Boolean type. Comparison with any other type of object raises a ```TypeError```
- ```__add__``` : Method overrides the basic implementation of addition + operator for the Qualean class..
- ```__or__``` : Logical OR operator, we perform logical OR on the imaginary values of the two objects else it returns ```False```.


- ```__float__``` : This method allows the user to convert the imaginary value to ```float```. Imaginary value is stored as a decimal with precision = 10 by default. 
- ```__ge__``` : 
  This method compares two Qualean objects to check if one object is greater than or equal to the other. If the objects being compared are not of Qualean type, ```TypeError``` is raised. 
- ```__gt__``` : Method overrides the greater than checking > for the user defined Qualean objects.
- ```__invertsign__``` : Method inverts the sign of the imaginary value. This is implemented using the ```copy_negate()``` method. 
- ```__le__``` : This method compares two Qualean objects to check if one object is lesser than or equal to the other. If the objects being compared are not of Qualean type, ```TypeError``` is raised.
- ```__lt__``` : Method overrides lesser than checking < for the user defined Qualean objects.
- ```__mul__``` : Multiplication between Qualean objects is implemented. 
- ```__sqrt__``` : Method implements the mathematical Square root operation on the Qualean object. For negative numbers, it returns complex numbers
- ```__bool__``` : This returns ```False``` for Qualean(0) and ```True``` for any other value(ie, Qualean(1) or Qualean(-1)). 
- ```__init__``` : This function initialises the Qualean object. 



## Test Cases

- test_readme_exists: Checks if the read.md file exists. 
- test_readme_contents: Checks if sufficient number of words have been used to describe the functions and methods.

- test_indentations: Checks if the indentations are up to the mark. Checks with respect to PEP8 format 

- test_function_name_had_cap_letter: Checks if there is any capital letter used in the name of the function that is not a standard.
- test_input_values: Checks whether the input number is any of 1, 0 or -1. If not it raises value error

- test_sum_multi_equal: It does summation of 100 qs and compares that result with the output of multiplication of q and 100. The result should match otherwise the test fails.

- test_square_root: Checks whether the square root of q does match with decimal square root of q

- test_false_case: Checks the validation for: q1 and q2 returns False when q2 is not defined as well and q1 is False.
- test_str_case: Checks if str returns a value that is of type str.
- test_repr_case: Returns the stored value in string type for representation purpose.
- test_equal_case: Compares two class instances to see if they match. The method equal gets called for the comparison.
- test_readme_proper_description: Checks if readme file contains explanation for all the functions and methods 
- test_readme_file_for_formatting: Checks if minimum words used to describe the fuctions, methods and test cases.
- test_true_case: Validates for: q1 or q2 returns True when q2 is not defined as well and q1 is not false

- test_add_method: adds a string to the class instance q. The operation should result in a value error else the test fails.

- test_and_case: Checks and operator works successfully between two instance of Quelean class.

- test_or_case: Checks or operator works successfully between two instance of Quelean class.

- test_float_case: Converts the result of a class instance into float and check if that happens successfully

- test_ge_case: Checks if a class instance q1 is greater than or equal to another class instance q2

- test_gt_case: Checks if a class instance q1 is greater than q2

- test_le_case: Checks if a class instance q1 is lesser than or equal to another class instance q2

- test_lt_case: Checks if a class instance q1 is lesser than another class instance q2

- test_invertsign_case: This test tries to invert the sign of the value from class instance q and validates if that is successful.

- test_multiplication_case: Tries to multipy q1 with q2 and vice versa and checks if their results match with each other where q1 and q2 are two instances of class Quelean

- test_bool_case: Does boolean comparison of multiple instances of class Quelean. Since random number is generated for every instance the result of the camparison should be False.

- test_isclose_case: Creates million different class objects and adds them up to check if the result is close to 0. 



##Results

![Image](https://github.com/The-School-of-AI/session4-kart19-out/results.png)




