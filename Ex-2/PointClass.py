# -*- coding: utf-8 -*-
'''
This module provides a class 'Point' which helps to find the Euclidean distance between two points, which are created
as objects of the class. This exercise comes under the course UIT2201 (Programming and Data Structures).

This is a source code purely based on my logic. It may have some bugs as well. 

Kindly feel free to comment down your suggestions and/or opinions.

Created on: 12th April 2023

Revised on: 13th April 2023

Original Author: Nithish Kumar S 
'''

class Point:
    '''
    The class Point is used to find the Euclidean distance between two points and returns it.
    This class contains these functions:
        (i) __init__ - assigns the parameters passed (a,b) to the x-coordinate
                        and the y-coordinate.
        (ii) distance() - returns the distance between two points passed as arguments.
    '''    
    
    x=0
    y=0

    def __init__ (self,a=0,b=0):
        '''
        Parameters: 
            self - refers to the object instance created under the Point class.
            a,b - local variables referring to x and y.
        ----------
        
        This function is a constructor that gets invoked automatically, when an object is created under the 'Point'
        class. It assigns the a,b to x,y coordinates of the object 'self'.

        Returns: x value assigned using the local variable a, y value assigned using the local variable b.
        '''
        
        self.x = a
        self.y = b


    def distance (self,other):
        '''
        Parameters: 
            self - refers to the object1,
            other - refers to the object2.
        ----------
        
        This function finds the Euclidean distance between two points, passed as objects of the class.

        Returns: distance - Euclidean distance between point1 and point2.
        '''
        
        xdiff = (other.x - self.x)**2
        ydiff = (other.y - self.y)**2
        distance = (xdiff + ydiff)**0.5
        return distance


#usage of __name__ so that the test cases are not imported.
if __name__ == '__main__':
    
    import random

    number = int(input("Enter the number of points:"))

    #lists to store the point numbers and their coordinates(points)
    points = []
    coordinates = []


    for i in range(1,number+1):            #creating random coordinates
        x = random.randint(0,10)
        y = random.randint(0,10)
        point_no = 'point' + str(i)
        point_coordinates = (x,y)
        points.append(point_no)
        coordinates.append(point_coordinates)

    print("The coordinates of the points created are: \n",coordinates)


    '''
    #used to find the distance between two successive coordinates in the list of coordinates.
    
    for i in range(number-1):
    p1 = Point(coordinates[i][0],coordinates[i][1])
    p2 = Point(coordinates[i+1][0],coordinates[i+1][1])

    print("distance between the points",coordinates[i],"and",coordinates[i+1])
    print(p2.distance(p1))
    '''


    distances = []             #distance storing list
    points_taken = []          #to store the data about points taken

    x = int(input("\n Enter the x coordinate of pknew point:"))
    y = int(input("Enter the y coordinate of pknew point:"))

    pknew = (x,y)              #defining the pknew point


    for i in range(number):    #creating the list of distances and points taken
        p1 = Point(pknew[0],pknew[1])
        p2 = Point(coordinates[i][0],coordinates[i][1])

        distance = p2.distance(p1)
        distances.append(round(distance,2))
        statement = str(pknew) + ' and ' + str(coordinates[i])
        points_taken.append(statement)


    inc_distances = distances[:]                    #list copied to sort the original list, while 
                                                    #restoring the unsorted list as 'distances'.


    for i in range(len(inc_distances)):             #sorting the list of distances in increasing order as a new list
        for j in range(len(inc_distances)-0-1):
            if inc_distances[j]>inc_distances[j+1]:
                inc_distances[j],inc_distances[j+1] = inc_distances[j+1],inc_distances[j]
            


    k = int(input("\n  Enter the number of nearest neighbours you wish to print:"))    #to print k nearest neighbours


    nearest_neighbours = []          #a list which would store the nearest neighbours of pknew point.


    for i in range(k):               #creating a list with nearest neighbours
        inc_distances = inc_distances[0:k]
        for i in inc_distances:
            ind = distances.index(i)
            statement = points_taken[ind]
            if statement not in nearest_neighbours:
                nearest_neighbours.append(statement)
    
    print("\n The nearest neighbours of pknew point ",pknew," are:")
    
    for statement in nearest_neighbours:     #printing nearest neighbours
        print(statement)

