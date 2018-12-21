## Mega-Parser
Parse Tree for TINY Language.

## How to run:
clone the repo
pip3 install -r requirements.txt
python3 main.py

## Input:
Place your Tiny syntax in sample_input.txt file

## Output:
output.png

## Examples:

```
X:=2;
y:=3;
z:=5;
a:=x+y+z;
```
![alt parse tree](https://i.ibb.co/WpG4K37/Screenshot-from-2018-12-21-21-04-26.png)
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
