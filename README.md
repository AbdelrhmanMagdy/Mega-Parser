## Mega-Parser
Parse Tree for TINY Language.

## How to run:
###environment: Linux
### Executable
- Clone the repo
- Go to dist folder
- Place your Tiny syntax in sample_input.txt filr
- Double click on main file
- Find and click output.png

### Source code
- clone the repo
- pip3 install -r requirements.txt
- python3 main.py

## Input:
- Place your Tiny syntax in sample_input.txt file

## Output:
- output.png

## Examples:

```
X:=2;
y:=3;
z:=5;
a:=x+y+z;
if z<8 then
    repeat
    a:=a*2;
    z:=z-1
    until z=0;
    write a
else
    read b;
    if b = 1 then
        write b*(x+y)
    else
        write a
    end
end;
write z
```
![alt parse tree](https://i.ibb.co/cNwjm0B/output.png)
```
read x; {input an integer }
if 0 < x then { don’t compute if x <= 0 }
fact := 1;
repeat
fact := fact * x;
x := x - 1
until x = 0;
write fact { output factorial of x }
end
```
![alt parse tree](https://i.ibb.co/rx9wFNL/Screenshot-from-2018-12-21-21-02-17.png)
