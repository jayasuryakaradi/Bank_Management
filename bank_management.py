import mysql.connector
import random
import pyttsx3

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="surya1998",
    database="banking"
)

def voice(string):
    pyobj = pyttsx3.init()
    pyobj.say(string)
    pyobj.runAndWait()



cursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE banking")
# cursor.execute("CREATE TABLE User_Details(SL INT AUTO_INCREMENT PRIMARY KEY,First_Name VARCHAR(255),Last_Name VARCHAR(255),Gender VARCHAR(1), Account_Number VARCHAR(10),Mobile VARCHAR(10),Address VARCHAR(255),Balance VARCHAR(255),ATM_PIN VARCHAR(4))")

while True:
    print("--------------------------------------")
    print("WELCOME TO STATE BANK OF INDIA")

    print("--------------------------------------")
    print("""
1. OPEN NEW ACCOUNT    2. VIEW ACCOUNT DETAILS
3. WITHDRAW AMOUNT     4. DEPOSIT AMOUNT
5. CHANGE ATM PIN      6.EXIT
""")
    print("--------------------------------------")
    main_voice_count=0
    if main_voice_count==0:
        voice("WELCOME TO STATE BANK OF INDIA, Please choose the option")
        main_voice_count=1

    main_menu_option_selection=int(input("PLEASE CHOOSE: "))
    print("--------------------------------------")


    # 1.OPENING ACCOUNT
    if main_menu_option_selection==1:
        print("OPENING ACCOUNT: ")
        print("--------------------------------------")
        first_name=input("FIRST NAME: ").upper()
        last_name=input("LAST NAME: ").upper()
        print("--------------------------------------")
        print("GENDER: 1.MALE    2.FEMALE    3.UNISEX")
        while True:
            g=int(input("SELECT: "))
            gender=""
            if g==1:
                gender="M"
                break
            elif g==2:
                gender="F"
                break
            elif g==3:
                gender="U"
                break
            else:
                print("Error")
        print("--------------------------------------")
        account_number = random.randint(1000000000, 9999999999)
        mobile_number=""
        print("MOBILE NUMBER: ", end=" ")
        while True:
            mobile_number=input()
            if len(mobile_number)==10:
                break
            else:
                print("INVALID!!, PLEASE ENTER CORRECT MOBILE NUMBER")
        address = input("ADDRESS: ").upper()
        opening_balance=int(input("DEPOSIT AMOUNT: "))
        atm_pin=random.randint(1111, 9999)
        sql = "INSERT INTO User_Details (First_Name,Last_Name,Gender,Account_Number,Mobile,Address,Balance,ATM_PIN) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(first_name, last_name, gender, account_number, mobile_number, address, opening_balance, atm_pin)
        cursor.execute(sql, val)
        mydb.commit()
        print("--------------------------------------")
        print("ACCOUNT CREATED SUCESSFULLY")
        voice("ACCOUNT CREATED SUCESSFULLY")
        print("--------------------------------------")
        print("FULL NAME        :        ", first_name, " ", last_name)
        print("ADDRESS          :        ", address)
        print("ACCOUNT NUMBER   :        ", account_number)
        print("MOBILE           :        ", mobile_number)
        print("BALANCE          :        ", opening_balance)
        print("ATM_PIN          :        ", atm_pin)
        print("--------------------------------------")


    # 2.VIEW DETAILS
    elif main_menu_option_selection==2:
        print("""SEARCH DETAILS BY:
        1. ACCOUNT NUMBER  2. MOBILE NUMBER  3. MAIN MENU""")
        while True:
            view_details_menu=int(input("PLEASE CHOOSE: "))
            print("--------------------------------------")

            if view_details_menu==1:
                while True:
                    account_number=input("ENTER ACC NUMBER: ")
                    atm_pin=input("ENTER ATM PIN: ")
                    sql_acc_num = "SELECT * FROM user_details WHERE Account_Number = %s"
                    sql_atm_pin = "SELECT * FROM user_details WHERE ATM_PIN = %s"
                    val_acc_num=(account_number,)
                    val_atm_pin=(atm_pin,)
                    cursor.execute(sql_acc_num, val_acc_num)
                    myresult = cursor.fetchall()
                    print("--------------------------------------")
                    if account_number==myresult[0][4] and atm_pin==myresult[0][8]:
                        print("NAME          :     ", myresult[0][1], " ", myresult[0][2])
                        print("ACC NUMBER    :     ", myresult[0][4])
                        print("MOBILE NUMBER :     ", myresult[0][5])
                        print("ADDRESS       :     ", myresult[0][6])
                        print("BALANCE       :     ", myresult[0][7])
                        print("--------------------------------------")
                        break
                    else:
                        print("INVALID DETAILS!!, ENTER CORRECT DETAILS")
                        print("--------------------------------------")
                break

            elif view_details_menu==2:
                while True:
                    mobile_number = input("ENTER MOBILE NUMBER: ")
                    atm_pin = input("ENTER ATM PIN: ")
                    sql_mob_num = "SELECT * FROM user_details WHERE Mobile = %s"
                    sql_atm_pin = "SELECT * FROM user_details WHERE ATM_PIN = %s"
                    val_mob_num = (mobile_number,)
                    val_atm_pin = (atm_pin,)
                    cursor.execute(sql_mob_num, val_mob_num)
                    myresult = cursor.fetchall()
                    print("--------------------------------------")
                    if mobile_number == myresult[0][5] and atm_pin == myresult[0][8]:
                        print("NAME          :     ", myresult[0][1], " ", myresult[0][2])
                        print("ACC NUMBER    :     ", myresult[0][4])
                        print("MOBILE NUMBER :     ", myresult[0][5])
                        print("ADDRESS       :     ", myresult[0][6])
                        print("BALANCE       :     ", myresult[0][7])
                        print("--------------------------------------")

                        break
                    else:
                        print("INVALID DETAILS!!, ENTER CORRECT DETAILS")
                        voice("INVALID DETAILS!!, ENTER CORRECT DETAILS")
                        print("--------------------------------------")
                    break
                break

            elif view_details_menu==3:
                break
            else:
                print("INVALID!!, PLEASE CHOOSE CORRECT OPTION")
                voice("INVALID!!, PLEASE CHOOSE CORRECT OPTION")
                print("--------------------------------------")


    # 3 WITHDRAW AMOUNT
    elif main_menu_option_selection==3:
        print("WITHDRAW AMOUNT")
        print("--------------------------------------")
        while True:
            account_number = input("ENTER ACC NUMBER: ")
            atm_pin = input("ENTER ATM PIN: ")
            sql_acc_num = "SELECT * FROM user_details WHERE Account_Number = %s"
            sql_atm_pin = "SELECT * FROM user_details WHERE ATM_PIN = %s"
            val_acc_num = (account_number,)
            val_atm_pin = (atm_pin,)
            cursor.execute(sql_acc_num, val_acc_num)
            myresult = cursor.fetchall()
            print("--------------------------------------")
            if account_number == myresult[0][4] and atm_pin == myresult[0][8]:
                print("NAME: ", myresult[0][1], " ", myresult[0][2])
                print("ACC NUMBER: ", myresult[0][4])
                print("MOBILE NUMBER: ", myresult[0][5])
                print("BALANCE: ", myresult[0][7])
                print("--------------------------------------")

                while True:
                    wd_amount=int(input("WITHDRAW AMOUNT: "))
                    main_balance_con_int=int(myresult[0][7])
                    id_key=myresult[0][0]
                    main_bal_after_trans=0
                    if wd_amount % 100==0:
                        if wd_amount<=main_balance_con_int:
                            main_bal_after_trans=main_balance_con_int-wd_amount
                            print("TRANSACTION DONE SUCESSFULLY")
                            voice("TRANSACTION DONE SUCESSFULLY")
                            print("--------------------------------------")
                            sql_tran_update= "UPDATE user_details SET Balance = %s WHERE SL = %s"
                            val = (main_bal_after_trans, id_key)
                            cursor.execute(sql_tran_update, val)
                            mydb.commit()
                            print("1.MAIN MENU     2.EXIT")
                            while True:
                                wd_menu = int(input("PLEASE CHOOSE: "))
                                if wd_menu==1:
                                    print("--------------------------------------")
                                    break
                                elif wd_menu==2:
                                    print("--------------------------------------")
                                    exit(1)
                                else:
                                    print("--------------------------------------")
                                    print("INVALID!!, PLEASE CHOOSE CORRENT OPTION")
                                    voice("INVALID!!, PLEASE CHOOSE CORRENT OPTION")
                                    print("--------------------------------------")
                        else:
                            print("--------------------------------------")
                            print("INSUFFICENT BALANCE")
                            voice("INSUFFICENT BALANCE")
                            print("CURRENT BALANCE: ", myresult[0][7])
                            print("--------------------------------------")
                    else:
                        print("INVALID!!, PLEASE ENTER VALID AMOUNT")
                        print("Only 100, 200, 500, 2000")
                        voice("INVALID!!, PLEASE ENTER VALID AMOUNT, Only 100,200,500,2000")
                        print("--------------------------------------")
                    break

            else:
                print("INVALID DETAILS!!, PLEASE ENTER CORRECT DETAILS")
                voice("INVALID DETAILS!!, PLEASE ENTER CORRECT DETAILS")
                print("--------------------------------------")
            break

    # 4.DEPOSIT AMOUNT
    elif main_menu_option_selection==4:
        print("DEPOSIT AMOUNT")
        print("--------------------------------------")
        while True:
            account_number = input("ENTER ACC NUMBER: ")
            atm_pin = input("ENTER ATM PIN: ")
            sql_acc_num = "SELECT * FROM user_details WHERE Account_Number = %s"
            sql_atm_pin = "SELECT * FROM user_details WHERE ATM_PIN = %s"
            val_acc_num = (account_number,)
            val_atm_pin = (atm_pin,)
            cursor.execute(sql_acc_num, val_acc_num)
            myresult = cursor.fetchall()
            print("--------------------------------------")
            if account_number == myresult[0][4] and atm_pin == myresult[0][8]:
                print("NAME: ", myresult[0][1], " ", myresult[0][2])
                print("ACC NUMBER: ", myresult[0][4])
                print("MOBILE NUMBER: ", myresult[0][5])
                print("BALANCE: ", myresult[0][7])
                print("--------------------------------------")

                while True:
                    deposit_amount=int(input("DEPOSIT AMOUNT: "))
                    main_balance_con_int=int(myresult[0][7])
                    id_key=myresult[0][0]

                    main_bal_after_trans=main_balance_con_int+deposit_amount
                    print("TRANSACTION DONE SUCESSFULLY")
                    voice("TRANSACTION DONE SUCESSFULLY")
                    print("--------------------------------------")
                    sql_tran_update= "UPDATE user_details SET Balance = %s WHERE SL = %s"
                    val = (main_bal_after_trans, id_key)
                    cursor.execute(sql_tran_update, val)
                    mydb.commit()
                    print("1.MAIN MENU     2.EXIT")

                    while True:
                        deposit_menu = int(input("PLEASE CHOOSE: "))
                        if deposit_menu==1:
                            break
                        elif deposit_menu==2:
                            exit(1)
                        else:
                            print("--------------------------------------")
                            print("INVALID!!, PLEASE CHOOSE CORRECT OPTION")
                            voice("INVALID!!, PLEASE CHOOSE CORRECT OPTION")

                            print("--------------------------------------")
                    break
            else:
                print("INVALID DETAILS!!, PLEASE ENTER CORRECT DETAILS")
                voice("INVALID DETAILS!!, PLEASE ENTER CORRECT DETAILS")
                print("--------------------------------------")
            break

    # 5.CHANGE ATM PIN
    elif main_menu_option_selection==5:
        print("CHANGE ATM PIN")
        while True:
            account_number = input("ENTER ACC NUMBER: ")
            atm_pin = input("ENTER ATM PIN: ")
            sql_acc_num = "SELECT * FROM user_details WHERE Account_Number = %s"
            sql_atm_pin = "SELECT * FROM user_details WHERE ATM_PIN = %s"
            val_acc_num = (account_number,)
            val_atm_pin = (atm_pin,)
            cursor.execute(sql_acc_num, val_acc_num)
            myresult = cursor.fetchall()
            print("--------------------------------------")
            if account_number == myresult[0][4] and atm_pin == myresult[0][8]:
                print("NAME: ", myresult[0][1], " ", myresult[0][2])
                print("ACC NUMBER: ", myresult[0][4])
                print("MOBILE NUMBER: ", myresult[0][5])
                print("BALANCE: ", myresult[0][7])
                print("--------------------------------------")


                while True:
                    atm_pin=int(input("CURRENT ATM PIN: "))
                    atm_pin_con_int=int(myresult[0][8])
                    id_key=myresult[0][0]
                    if atm_pin==atm_pin_con_int:
                        temp_atm_pin1=int(input("ENTER NEW PIN: "))
                        temp_atm_pin2=int(input("ENTER THE NEW PIN ONCE AGAIN: "))
                        if temp_atm_pin1==temp_atm_pin2:
                            print("--------------------------------------")
                            print("ATM PIN CHANGED SUCESSFULLY")
                            voice("ATM PIN CHANGED SUCESSFULLY")
                            print("--------------------------------------")
                            sql_pin_update= "UPDATE user_details SET ATM_PIN = %s WHERE SL = %s"
                            val = (temp_atm_pin1, id_key)
                            cursor.execute(sql_pin_update, val)
                            mydb.commit()
                            print("1.MAIN MENU     2.EXIT")
                            while True:
                                wd_menu=int(input("PLEASE CHOOSE: "))
                                if wd_menu==1:
                                    break
                                elif wd_menu==2:
                                    exit(1)
                                else:
                                    print("--------------------------------------")
                                    print("INVALID!!, PLEASE CHOOSE CORRECT OPTION")
                                    voice("INVALID!!, PLEASE CHOOSE CORRECT OPTION")
                                    print("--------------------------------------")
                            break
                        else:
                            print("--------------------------------------")
                            print("NEW PIN NOT MATCHING!!")
                            voice("NEW PIN NOT MATCHING!!")
                            print("--------------------------------------")
                    else:
                        print("--------------------------------------")
                        print("INVALID CURRENT PIN!!, ENTER CORRECT")
                        voice("INVALID CURRENT PIN!!, ENTER CORRECT")
                        print("--------------------------------------")
                break
                break
            else:
                print("INVALID PIN!!, PLEASE ENTER VALID PIN")
                voice("INVALID PIN!!, PLEASE ENTER VALID PIN")
                print("--------------------------------------")

    # 6.Exit
    elif main_menu_option_selection==6:
        exit(1)
    #
    else:
        print("INVALID!!, PLEASE CHOOSE THE CORRECT OPTION")
        voice("INVALID!!, PLEASE CHOOSE THE CORRECT OPTION")
        print("--------------------------------------")
