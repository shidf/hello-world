# -*- coding: utf-8 -*- 
import string
import types
from Bill_calculate import *

def run(self):
    
    test_scenario_1 = [[0,0,0,0],[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,1,0],[1,0,0,1],[0,1,0,1],[1,1,1,0],[1,0,1,1],[0,1,1,1],[1,1,0,1],[1,1,1,1]]

    test_scenario_2 = [[0,0,0,0],[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,1,0],[1,0,0,1],[0,1,0,1],[1,1,1,0],[1,0,1,1],[0,1,1,1],[1,1,0,1],[1,1,1,1]]

    test_scenario_3 = [[0,0,0,0],[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,1,0],[1,0,0,1],[0,1,0,1],[1,1,1,0],[1,0,1,1],[0,1,1,1],[1,1,0,1],[1,1,1,1]]

    #change test_scenario_2, multiply with 2
    for i in range(len(test_scenario_2)):
        a = test_scenario_2[i]
        for j in range(len(a)):
            a[j] = a[j]*2

    #change test_scenario_3, multiply with 3
    for i in range(len(test_scenario_3)):
        a = test_scenario_3[i]
        for j in range(len(a)):
            a[j] = a[j]*3
    
    Cal_bill = Bill_cal()
    
    ###1) Permanent
    Custom_type = 'Permanent'

    #1.1)DVD_number < DVD_days
    Free_transaction_left = ''

    for i in range(len(test_scenario_1)):
        DVD_number_list = test_scenario_1[i]
        DVD_days_list = test_scenario_3[i]
        Bill_one_time,Free_transaction_left = Cal_bill.Custom_bill_cal(DVD_number_list,DVD_days_list,Custom_type,Free_transaction_left)


    #1.2)DVD_number = DVD_days
    Free_transaction_left = ''

    for i in range(len(test_scenario_2)):
        DVD_number_list = test_scenario_2[i]
        DVD_days_list = test_scenario_2[i]
        Bill_one_time,Free_transaction_left = Cal_bill.Custom_bill_cal(DVD_number_list,DVD_days_list,Custom_type,Free_transaction_left)

    #1.3)DVD_number > DVD_days
    Free_transaction_left = ''

    for i in range(len(test_scenario_3)):
        DVD_number_list = test_scenario_3[i]
        DVD_days_list = test_scenario_1[i]
        Bill_one_time,Free_transaction_left = Cal_bill.Custom_bill_cal(DVD_number_list,DVD_days_list,Custom_type,Free_transaction_left)


    #2) Temporary
    Custom_type = 'Temporary'
    #2.1)DVD_number < DVD_days
    Free_transaction_left = ''

    for i in range(len(test_scenario_1)):
        DVD_number_list = test_scenario_1[i]
        DVD_days_list = test_scenario_3[i]
        Bill_one_time,Free_transaction_left = Cal_bill.Custom_bill_cal(DVD_number_list,DVD_days_list,Custom_type,Free_transaction_left)


    #2.2)DVD_number = DVD_days
    Free_transaction_left = ''

    for i in range(len(test_scenario_2)):
        DVD_number_list = test_scenario_2[i]
        DVD_days_list = test_scenario_2[i]
        Bill_one_time,Free_transaction_left = Cal_bill.Custom_bill_cal(DVD_number_list,DVD_days_list,Custom_type,Free_transaction_left)

    #2.3)DVD_number > DVD_days
    Free_transaction_left = ''

    for i in range(len(test_scenario_3)):
        DVD_number_list = test_scenario_3[i]
        DVD_days_list = test_scenario_1[i]
        Bill_one_time,Free_transaction_left = Cal_bill.Custom_bill_cal(DVD_number_list,DVD_days_list,Custom_type,Free_transaction_left)

    #3) all customer types
    Customer_type_list = Free_transaction_times_every_membership.keys()
    for j in range(len(Customer_type_list)):
        Custom_type = Customer_type_list[j]
        Free_transaction_left = ''
        for i in range(len(test_scenario_1)):
            DVD_number_list = test_scenario_1[i]
            DVD_days_list = test_scenario_3[i]
            Bill_one_time,Free_transaction_left = Cal_bill.Custom_bill_cal(DVD_number_list,DVD_days_list,Custom_type,Free_transaction_left)

        Free_transaction_left = ''
        for i in range(len(test_scenario_2)):
            DVD_number_list = test_scenario_2[i]
            DVD_days_list = test_scenario_2[i]
            Bill_one_time,Free_transaction_left = Cal_bill.Custom_bill_cal(DVD_number_list,DVD_days_list,Custom_type,Free_transaction_left)

        Free_transaction_left = ''
        for i in range(len(test_scenario_3)):
            DVD_number_list = test_scenario_3[i]
            DVD_days_list = test_scenario_1[i]
            Bill_one_time,Free_transaction_left = Cal_bill.Custom_bill_cal(DVD_number_list,DVD_days_list,Custom_type,Free_transaction_left)

    #4) test_scenario reverse
    test_scenario_1.reverse()
    test_scenario_2.reverse()
    test_scenario_3.reverse()

    for j in range(len(Customer_type_list)):
        Custom_type = Customer_type_list[j]
        Free_transaction_left = ''
        for i in range(len(test_scenario_1)):
            DVD_number_list = test_scenario_1[i]
            DVD_days_list = test_scenario_3[i]
            Bill_one_time,Free_transaction_left = Cal_bill.Custom_bill_cal(DVD_number_list,DVD_days_list,Custom_type,Free_transaction_left)

        Free_transaction_left = ''
        for i in range(len(test_scenario_2)):
            DVD_number_list = test_scenario_2[i]
            DVD_days_list = test_scenario_2[i]
            Bill_one_time,Free_transaction_left = Cal_bill.Custom_bill_cal(DVD_number_list,DVD_days_list,Custom_type,Free_transaction_left)

        Free_transaction_left = ''
        for i in range(len(test_scenario_3)):
            DVD_number_list = test_scenario_3[i]
            DVD_days_list = test_scenario_1[i]
            Bill_one_time,Free_transaction_left = Cal_bill.Custom_bill_cal(DVD_number_list,DVD_days_list,Custom_type,Free_transaction_left)


