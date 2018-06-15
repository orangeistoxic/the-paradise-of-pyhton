輸入和輸出
1.輸出
範例程式(圓面積)

```
#!/usr/bin/env python
#coding=utf-8

# radius = 25 
# Input:Prompt the user to enter a radius
radius = eval(input ("Enter a number for radius: "))

# Processin:Compute area
area = radius * radius * 3.1415962

# Output:Display results
print("The area for the circle of radius", radius, "is", area)
```
![](pic/frt-1.PNG)



發現無法輸出 改使用python3
![](pic/frt-2.PNG)


2.同時指定(Simultaneous Assignment )


範例程式(三數平均)



```
#!/usr/bin/env python
#coding=utf-8

# Prompt the user to enter three numbers
number1, number2, number3 = eval(input("Enter three numbers separated by commas: "))

# Compute average
average = (number1 + number2 + number3) / 3

# Display result
print("The average of", number1, number2, number3, "is", average)
```


一樣使用python3才能執行
![](pic/danie-1.PNG)



