# -*- coding: utf-8 -*- 
import string
import types

#assumption: all the transaction happened in the valid date within membership time

Free_transaction_times_every_membership  = {
            'Permanent':30,
            'S1':12,
            'S2':7,
            'S3':7,
            'S4':7,
            'Temporary':1
            }

Additional_transation_cost_every_membershi = {'Permanent':50,
            'S1':12,
            'S2':15,
            'S3':15,
            'S4':15,
            'Temporary':0
            } 

DVD_types_money_dic = {'Movies':20,
            'Documentaries':20,
            'Games':50,
            'Sports':30
            } 

class Bill_cal:

    def __init__(self):
            pass

    def Custom_bill_cal(self,DVD_number_list,DVD_days_list,Custom_type,Free_transaction_left):
        
        Free_transaction_times_initial = Free_transaction_times_every_membership[Custom_type]
        if Free_transaction_left == '':
            Free_transaction_left = Free_transaction_times_initial

        print 'Free_transaction_left==',Free_transaction_left 

        if Free_transaction_left > Free_transaction_times_initial:
            print 'The initial Free transaction times is error!'
            return

        DVD_types_money_list = [DVD_types_money_dic['Movies'],DVD_types_money_dic['Documentaries'],DVD_types_money_dic['Games'],DVD_types_money_dic['Sports']]

        if Free_transaction_left == 0:
            Bill_one_time = 0
            for i in range(len(DVD_number_list)):
                every_type_bill = DVD_types_money_list[i]*DVD_number_list[i]*DVD_days_list[i]
                Bill_one_time+=every_type_bill

            Free_transaction_left = 0

        else:  
            Bill_one_time = 0
            DVD_numbers_total = 0
            for i in range(len(DVD_number_list)):
                DVD_numbers_every_type = DVD_number_list[i]
                DVD_numbers_total += DVD_numbers_every_type
            
            Free_transaction_left_1 = Free_transaction_left

            if DVD_numbers_total <= Free_transaction_left:
                Free_transaction_left = Free_transaction_left - DVD_numbers_total
            else:
                Free_transaction_left = 0

            for i in range(len(DVD_number_list)):
                if Free_transaction_left_1 == 0:
                    Bill_one_time += DVD_number_list[i]*DVD_days_list[i]*DVD_types_money_list[i]

                if DVD_number_list[i] <= Free_transaction_left_1:
                    Free_transaction_left_1 = Free_transaction_left_1 - DVD_number_list[i]
                    Free_transaction_used = DVD_number_list[i]

                    Bill_one_time += ((DVD_number_list[i] - Free_transaction_used)*DVD_days_list[i] + Free_transaction_used*(DVD_days_list[i] - 1))*DVD_types_money_list[i]
                else:
                    Free_transaction_used = Free_transaction_left_1
                    Free_transaction_left_1 = 0

                    Bill_one_time += ((DVD_number_list[i] - Free_transaction_used)*DVD_days_list[i] + Free_transaction_used*(DVD_days_list[i] - 1))*DVD_types_money_list[i]


        print "This rental transaction bill is %d, there are %d times free transaction left!" %(Bill_one_time,Free_transaction_left)

        return Bill_one_time,Free_transaction_left



