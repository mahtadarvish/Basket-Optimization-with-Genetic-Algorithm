# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 22:12:41 2023

@author: dellhp
"""

import numpy as np
import statistics

class Knapsack01Problem:
    """This class encapsulates the Knapsack 0-1 Problem from RosettaCode.org
    """

    def __init__(self):

        # initialize instance variables:
        self.items = []
        self.maxCapacity = 0

        # initialize the data:
        self.__initData()

    def __len__(self):
        """
        :return: the total number of items defined in the problem
        """
        return len(self.items)

    def __initData(self):
        """initializes the RosettaCode.org knapsack 0-1 problem data
        """
        self.items = [
            ("map", 9, 150),
            ("compass", 13, 35),
            ("water", 153, 200),
            ("sandwich", 50, 160),
            ("glucose", 15, 60),
            ("tin", 68, 45),
            ("banana", 27, 60),
            ("apple", 39, 40),
            ("cheese", 23, 30),
            ("beer", 52, 10),
            ("suntan cream", 11, 70),
            ("camera", 32, 30),
            ("t-shirt", 24, 15),
            ("trousers", 48, 10),
            ("umbrella", 73, 40),
            ("waterproof trousers", 42, 70),
            ("waterproof overclothes", 43, 75),
            ("note-case", 22, 80),
            ("sunglasses", 7, 20),
            ("towel", 18, 12),
            ("socks", 4, 50),
            ("book", 30, 10)
        ]

        self.maxCapacity = 400

    
        """
        Prints the selected items in the list, while ignoring items that will cause the accumulating weight to exceed the maximum weight
        :param zeroOneList: a list of 0/1 values corresponding to the list of the problem's items. '1' means that item was selected.
        """
        #totalWeight = totalValue = 0

        
        
    def getValue(self, attr_fltList):
        """
        Calculates the value of the selected items in the list, while ignoring items that will cause the accumulating weight to exceed the maximum weight
        :param zeroOneList: a list of 0/1 values corresponding to the list of the problem's items. '1' means that item was selected.
        :return: the calculated value
        zeroOneList[i]
        """

        totalWeight = totalValue = 0

        for i in range(len(attr_fltList)):
            violation=0
            item, weight, value = self.items[i]
            if totalWeight + weight <= self.maxCapacity:
                totalWeight +=   attr_fltList[i] * weight
                totalValue +=   attr_fltList[i] * value
            #if totalWeight >= self.maxCapacity:
               # violation=violation+1
        return totalValue,violation
     
    def evaluate(self,attr_fltList):
        
        
        violation=0
        totalWeight = totalValue = 0
        if  statistics.stdev(attr_fltList)<=20:
                #violation=violation+10000
        
        
        

          for i in range(len(attr_fltList)):
            violation=0
            item, weight, value = self.items[i]
            if totalWeight +attr_fltList[i]*weight <= self.maxCapacity:
                totalWeight +=   attr_fltList[i] * weight
                totalValue +=   attr_fltList[i] * value
            else:
                totalValue=0
            
        #if totalWeight >= self.maxCapacity:
               # violation=violation+1   
        else:
            totalValue=0
    
        return totalValue     
             
         #return (1+(0.5*totalValue)-(1+(0.5*violation)))
         
         
         
     
     
    '''def GetWeightViolation(self,attr_fltList):
          
          violation=0
          
          for i in range(len(attr_fltList)):
          
              #if attr_fltList[i] > self.maxCapasityOfeachItem[i]:
              
                 violation=violation+(self.maxCapasityOfeachItem[i]-attr_fltList[i])
                 
              return violation'''
          
             
    '''def Violation1(self,attr_fltList,items):
          
          violation=0
          
          for i in range(len(attr_fltList)):
          
              if sum(attr_fltList[i]*items[i][2])>= 4000:
              
                 violation=violation+1
                 
          return violation 
      
         
     def Violation2(self,attr_fltList):
         violation=0
        # for i in range (len(attr_fltList)):
         if  statistics.stdev(attr_fltList)>=500:
                 violation=violation+1'''
                 
          
          
          
          
             
              
    def getCost(self, attr_fltList):
        """
        Calculates the total cost of the various violations in the given schedule
        ...
        :param schedule: a list of binary values describing the given schedule
        :return: the calculated cost
        """

        #if len(schedule) != self.__len__():
            #raise ValueError("size of schedule list should be equal to ", self.__len__())

        # convert entire schedule into a dictionary with a separate schedule for each nurse:
       # nurseShiftsDict = self.getNurseShifts(schedule)

        # count the various violations:
        #consecutiveShiftViolations = self.countConsecutiveShiftViolations(nurseShiftsDict)
        #shiftsPerWeekViolations = self.countShiftsPerWeekViolations(nurseShiftsDict)[1]
        #nursesPerShiftViolations = self.countNursesPerShiftViolations(nurseShiftsDict)[1]
        #shiftPreferenceViolations = self.countShiftPreferenceViolations(nurseShiftsDict)
        #TimePrefrenceViolations=self.countTimePrefrenceViolations()

        # calculate the cost of the violations:
       # hardContstraintViolations =  self.GetWeightViolation(attr_fltList)+self.Violation1(attr_fltList)+self.getValue(attr_fltList)[1]
        hardContstraintViolations =  self.Violation2(attr_fltList)
    
        #softContstraintViolations = shiftPreferenceViolations

        #return self.hardConstraintPenalty * hardContstraintViolations + softContstraintViolations
        #return self.hardConstraintPenalty * hardContstraintViolations
        return  hardContstraintViolations
         
         
            
        
        
        
        
        
        
    def printItems(self, attr_fltList):
        """
        Prints the selected items in the list, while ignoring items that will cause the accumulating weight to exceed the maximum weight
        :param zeroOneList: a list of 0/1 values corresponding to the list of the problem's items. '1' means that item was selected.
        """
        totalWeight = totalValue = 0
        j=[]

        for i in range(len(attr_fltList)):
            item, weight, value = self.items[i]
           # if attr_fltList <= self.maxCapacity:
           # if attr_fltList[i]<= self.maxCapasityOfeachItem[i] :   
            if totalWeight + attr_fltList[i] *weight <= self.maxCapacity:
                
                if attr_fltList[i] > 0:
                    totalWeight += attr_fltList[i] *weight
                    totalValue += attr_fltList[i] *value
                    c="- Adding {}: weight = {}, value = {}, accumulated weight = {}, accumulated value = {}".format(item, weight, value, totalWeight, totalValue)
                    j.append(c)
        d="- Total weight = {}, Total value = {}".format(totalWeight, totalValue)
        #j=[] 
        #j.append(c) 
        j.append(d)
        return(j)     
        
        
        
        
        
        


# testing the class:
def main():
    # create a problem instance:
    knapsack = Knapsack01Problem()

    # creaete a random solution and evaluate it:
    randomSolution = np.random.randint(2, size=len(knapsack))
    print("Random Solution = ")
    print(randomSolution)
    knapsack.printItems(randomSolution)


if __name__ == "__main__":
    main()