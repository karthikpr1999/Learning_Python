import numpy as np
import matplotlib.pyplot as plt 

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()

'''
import matplotlib.pyplot as plt 
a = [1, 2, 3, 4, 5] 
b = [0, 0.6, 0.2, 15, 10, 8, 16, 21] 
c = [4, 2, 6, 8, 3, 20, 13, 15] 

# use fig whenever u want the 
# output in a new window also 
# specify the window size you 
# want ans to be displayed 
fig = plt.figure(figsize =(10, 10)) 

# creating multiple plots in a 
# single plot 
sub1 = plt.subplot(2, 2, 1) 
sub2 = plt.subplot(2, 2, 2) 
sub3 = plt.subplot(2, 2, 3) 
sub4 = plt.subplot(2, 2, 4) 

sub1.plot(a, 'sb') 

# sets how the display subplot 
# x axis values advances by 1 
# within the specified range 
sub1.set_xticks(list(range(0, 10, 1))) 
sub1.set_title('1st Rep') 

sub2.plot(b, 'or') 

# sets how the display subplot x axis 
# values advances by 2 within the 
# specified range 
sub2.set_xticks(list(range(0, 10, 2))) 
sub2.set_title('2nd Rep') 

# can directly pass a list in the plot 
# function instead adding the reference 
sub3.plot(list(range(0, 22, 3)), 'vg') 
sub3.set_xticks(list(range(0, 10, 1))) 
sub3.set_title('3rd Rep') 

sub4.plot(c, 'Dm') 

# similarly we can set the ticks for 
# the y-axis range(start(inclusive), 
# end(exclusive), step) 
sub4.set_yticks(list(range(0, 24, 2))) 
sub4.set_title('4th Rep') 

# without writing plt.show() no plot 
# will be visible 
plt.show() 


import matplotlib.pyplot as plt 

a = [1, 2, 3, 4, 5] 
b = [0, 0.6, 0.2, 15, 10, 8, 16, 21] 
plt.plot(a) 

# o is for circles and r is 
# for red 
plt.plot(b, "or") 

plt.plot(list(range(0, 22, 3))) 

# naming the x-axis 
plt.xlabel('Day ->') 

# naming the y-axis 
plt.ylabel('Temp ->') 

c = [4, 2, 6, 8, 3, 20, 13, 15] 
plt.plot(c, label = '4th Rep') 

# get current axes command 
ax = plt.gca() 

# get command over the individual 
# boundary line of the graph body 
ax.spines['right'].set_visible(False) 
ax.spines['top'].set_visible(False) 

# set the range or the bounds of 
# the left boundary line to fixed range 
ax.spines['left'].set_bounds(-3, 40) 

# set the interval by which 
# the x-axis set the marks 
plt.xticks(list(range(-3, 10))) 

# set the intervals by which y-axis 
# set the marks 
plt.yticks(list(range(-3, 20, 3))) 

# legend denotes that what color 
# signifies what 
ax.legend(['1st Rep', '2nd Rep', '3rd Rep', '4th Rep']) 

# annotate command helps to write 
# ON THE GRAPH any text xy denotes 
# the position on the graph 
plt.annotate('Temperature V / s Days', xy = (1.01, -2.15)) 

# gives a title to the Graph 
plt.title('All Features Discussed') 

plt.show() 

import matplotlib.pyplot as plt
x = [1,2,3]  
# corresponding y axis values  
y = [2,4,1]  
    
# plotting the points   
plt.plot(x, y)  
    
# naming the x axis  
plt.xlabel('x - axis')  
# naming the y axis  
plt.ylabel('y - axis')  
    
# giving a title to my graph  
plt.title('My first graph!')  
    
# function to show the plot  
plt.show()  


# initializing the data
x = [10, 20, 30, 40]
y = [20, 30, 40, 50]

# plotting the data
plt.plot(x, y)

# Adding the title
plt.title("Simple Plot")

# Adding the labels
plt.ylabel("y-axis")
plt.xlabel("x-axis")
plt.show()
'''
