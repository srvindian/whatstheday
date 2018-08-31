# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 19:16:31 2018

@author: Sourav
"""
if __name__=="__main__":
    month=[0,3,3,6,1,4,6,2,5,0,3,5]
    day=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    year=[6,4,2,0];
    date=input('Enter your date \n(format: ddmmyyyy ex:04031994 i.e:4-march-1994)  \n:');
    day_val=(int(date[0:2])+int(date[len(date)-2:len(date)])+int(date[len(date)-2:len(date)])//4+\
        month[int(date[2:4])%12-1]+year[int(date[4:6])%4])%7;
    print('The day was/is/will be ',day[day_val]);
    