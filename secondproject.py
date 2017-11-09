'''
Pritam Basnet
secondproject.py
10/06/2017
This project plots the graph of the population adopotion by the influenital population and imitator population. It also plots the graph of rates of changes.
'''
import matplotlib.pyplot as pyplot
def productDiffusion2(inSize, imSize, rIn, sIn, rIm, sIm, weight, weeks, dt):
    '''
    This function simulates the product adoption over time in the Market with the inclusion of imitators and influential.
    Parameters:
        rIn, rIm: it is the chance of product adoption by the non-adopters in both cases of influenitals and imitators.
        sIn, sIm - it measures the interaction between adopters and non-adopters in both case of influentials and imitators.
        weeks: no of weeks
        dt: the small time difference.
        inSize: population of influentials
        imSize: population of imitators
        weight: measures the extent in which non-adopters impress adopters
    Return Values:
        timeList: The list of time for plotting X-Axis.
        aList: the list with the adoopters
        rList: the list with rate of changes
        totalList: the list of total
        Inlist1: the list of rate of changes of influentials
        ImList1: the list of rate of changes of imitators
    '''
    InList = []
    ImList = []
    totalList= []
    timeList = []
    
    influenced_adopters_Before= 0
    imitated_adopters_Before = 0
    total_adopters_Before = 0
    t = 0
    InList.append(influenced_adopters_Before)
    ImList.append(imitated_adopters_Before)
    totalList.append(total_adopters_Before)
    timeList.append(t)
    InList1 = [0]
    ImList1 = [0]
    totalList1 = [0]
    
    for i in range(0, int(weeks/dt)+1):
        newly_influenced = InList[-1]+ rIn*(1 - InList[-1])*dt + sIn * InList[-1] *(1 - InList[-1])*dt   #differential equations for newly influenced
        InList.append(newly_influenced)
        newly_imitated = ImList[-1] + rIm*(1 - ImList[-1])*dt + weight * sIm * InList[-1] * (1 - ImList[-1])*dt + (1 - weight) * sIm * ImList[-1] * (1 - ImList[-1])*dt
        ImList.append(newly_imitated)
        
        t = t+dt
        timeList.append(t)
        
        total_new_influenced = (newly_influenced - influenced_adopters_Before)/dt
        InList1.append(total_new_influenced)
        
        total_new_imitated = (newly_imitated - imitated_adopters_Before)/dt
        ImList1.append(total_new_imitated)
        
        total_new_adoptions = ((newly_influenced) + (newly_imitated))
        totalList.append(total_new_adoptions)
        total_adoptions = (total_new_adoptions - total_adopters_Before)/dt
        totalList1.append(total_adoptions)

        influenced_adopters_Before = newly_influenced
        imitated_adopters_Before = newly_imitated
        total_adopters_Before = total_new_adoptions
        
    for i in range(len(InList)):                                          # second loop to change fraction into percentage
        InList[i] = InList[i] * inSize
        InList1[i] = InList1[i] * inSize
        ImList[i] = ImList[i] * imSize
        ImList1[i] = ImList1[i] * imSize
        totalList1[i] = InList1[i] + ImList1[i]
        totalList[i] = InList[i] + ImList[i]
    return InList, ImList, InList1, ImList1,timeList, totalList, totalList1         #returns the lists
def main():
    inSize = 600
    imSize = 400
    rIn = 0.002
    sIn = 1.03
    rIm = 0
    sIm = 0.8
    weight = 0.6
    weeks = 15
    dt = 0.01
    InList, ImList, InList1, ImList1, timeList,totalList,totalList1= productDiffusion2(inSize, imSize, rIn, sIn, rIm, sIm, weight, weeks, dt)
    pyplot.figure(1)                                                                 #plots the figure 1
    pyplot.plot(timeList, InList, label = 'Influencers')
    pyplot.plot(timeList, ImList, label = 'Imitators')
    pyplot.plot(timeList, totalList, label = 'Total')
    pyplot.xlabel('Weeks')
    pyplot.ylabel('Market Adoption Numbers')
    pyplot.legend()
    
    pyplot.figure(2)                                                                   #plots the figure 2
    pyplot.plot(timeList, InList1, label = 'Influencers')
    pyplot.plot(timeList, ImList1, label = 'Imitators')
    pyplot.plot(timeList, totalList1, label = 'Total')
    pyplot.xlabel('Weeks')
    pyplot.ylabel('Marginal Market Adoption Numbers')
    pyplot.legend()
    pyplot.show()
    
main()
    
