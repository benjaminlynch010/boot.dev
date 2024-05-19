* in python a variable can be set to an empty string (NoneType) `empty_string = None`
* python is dynamically typed - a var can store any type and that type can change
* statically typed - var types cannot be reassigned
* multi-variable declaration - variables can be assigned on a single line e.g. `sword_name, sword_damage, sword_length = "Excalibur", 10, 200`

## chapter 3 - functions
* a function will return `None` if no return is specified
* print - shows value in console
* return - makes value available to the caller of the function
* function can return mulitple values by separating them with a comma e.g.
* parameters are the names used for inputs when defining a function 
* arguments are the values of the inputs supplied when a function is called
* an argument can be assigned a default value using the `=` operator e.g.
    ```
    def function(arg1, arg2=0)
    ```
#### binary numbers
* each `1` in a binary number represents an ever-greater multiple of 2
```
`0001` = 1
`0010` = 2
`0011` = 3
`0100` = 4
`0101` = 5
`0110` = 6
`0111` = 7
`1000` = 8
`1001` = 9
`1010` = 10
`1011` = 11
`1100` = 12
`1101` = 13
`1110` = 14
`1111` = 15

10011011
128(1) + 64(0) + 32(0)+ 16(1) + 8(1) + 4(0) + 2(1) + 1(1) = 155
```

* a `1` in binary is the same as `True` while `0` is the same as `False`
* bitwise '&' and '|' operator are similar to `and` and `or` logical operators, they perform simiilar logic on all the bits in a value
```python
0101 = 5
&
0111 = 7
=
0101 = 5
```
```python
0101 = 5
&
0010 = 2
=
0000 = 0
```
* when writing a number in binary, the prefix `0b` is used to indicate what follows is a binary number e.g.
```python
0b0101 & 0b0111
# returns 5
```
* `not` operator reverses the result
```python
print(not True)
# prints False

print(not False)
# prints True


    


