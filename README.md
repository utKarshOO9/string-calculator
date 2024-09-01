# string-calculator

A simple String calculator with a method signature:

```
int Add(string numbers)
```

The method can take string of numbers as input by delimited by characters will return their sum. 

for example “” or “1” or “1,2” as inputs.
(for an empty string it will return 0) 


Features

- [x] Do sum of number which are delimited by `,` integers
- [x] Do sum of number which are delimited by `,` integers, with n integers
- [x] Allow the Add method to handle new lines between numbers (instead of commas) delimiter `\n` `,`
- [x] Different delimiters identified as `//{delimiter}\n` ex: `//;\n` should do additions
- [x] Addition of negative numbers should throw errors with `negatives not allowed`
- [x] Numbers bigger than 1000 should be ignored, so adding `2 + 1001 = 2`
- [x] Delimiters can be of any length with the following format: `//[delimiter]\n` ex: `//[&&&]\n` `//[|||]\n` `//[PPP]\n` 
- [x] Allow multiple delimiters like this `//[delim1][delim2]\n` ex: `//[;][**]\n`
- [x] Allow multiple delimiters with length longer than one char
- [x] CLI Application to run calculator for getting output
- [x] Enable Api Interface for calculator
    
    Scope
    
    - Create Api over calculator
    - Able to take numbers as string as payload
    - Return Json Response 
        ```json
            {
                "input": "1,2",
                "output": 3,
                "errors": []
            }
        ```

        ```json
            {
                "input": "1,-2",
                "output": None
                "errors": [
                    "negatives not allowed: numbers(-2)"
                ]
            }
        ```




