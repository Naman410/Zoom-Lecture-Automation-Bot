import numpy as np
import os              
import pandas as pd    
import pyautogui
import time
from datetime import datetime


def signing_in(meeting_id) : 
    """, passkey):"""
    
    """
    The code when given the meeting id
    and password starts the zoom application
    waits for it to start writes the id and password
    and logins in and starts the meeting for you
    and maybe starts recording it too
    
    """

    os.startfile("C:\\Users\\NAMAN\\AppData\\Roaming\\Zoom\\bin\\zoom.exe")
    for i in range(0,30):
        start1 = pyautogui.locateCenterOnScreen('Join.png')
        start2 = pyautogui.locateCenterOnScreen('If not signed in.png')
        # startover = pyautogui.locateCenterOnScreen('signed out.png')
        if start1 != None :             #start1
            pyautogui.click(start1)
            print('START - 1')
            break

        elif start2 != None:            #start2
            pyautogui.click(start2)
            print('START - 2')
            for i in range (0,15) :
                signin_with_google = pyautogui.locateCenterOnScreen('click on sign with google.png')
                if signin_with_google != None:
                    print('singing in with google')
                    pyautogui.click(signin_with_google)
                    for i in range (0,15) :
                        my_account_name1 = pyautogui.locateCenterOnScreen('Click on naman.png')
                        my_account_name2 = pyautogui.locateCenterOnScreen('Clicking on my account.png')
                        direct_lucky_join = pyautogui.locateCenterOnScreen('Join.png')
                        if my_account_name1 != None:
                            print('account name 1')
                            pyautogui.click(my_account_name1)
                            time.sleep(2)
                            for i in range(0,5) :
                                my_account_name1 = pyautogui.locateCenterOnScreen('Click on naman.png')
                                my_account_name2 = pyautogui.locateCenterOnScreen('Clicking on my account.png')
                                if my_account_name1 != None:
                                    print('account name 1 second try')
                                    pyautogui.click(my_account_name1)
                                    break
                                elif my_account_name2 != None:
                                    print('account name 2 second try')
                                    pyautogui.click(my_account_name2)
                                    break
                                time.sleep(2)

                            for i in range(0,15) :

                                start1 = pyautogui.locateCenterOnScreen('Join.png')
                                if start1 != None :
                                    print('Clicking on JOIN Now!')
                                    pyautogui.click(start1)        
                                    x=10
                                    break
                                time.sleep(2)
                            break
                        
                        elif my_account_name2 != None:
                            print('account name 2')
                            pyautogui.click(my_account_name2)
                            time.sleep(2)
                            for i in range(0,5) :
                                my_account_name1 = pyautogui.locateCenterOnScreen('Click on naman.png')
                                my_account_name2 = pyautogui.locateCenterOnScreen('Clicking on my account.png')
                                if my_account_name1 != None:
                                    print('account name 1 second try')
                                    pyautogui.click(my_account_name1)
                                    break
                                elif my_account_name2 != None:
                                    print('account name 2 second try')
                                    pyautogui.click(my_account_name2)
                                    break
                                time.sleep(2)

                            for i in range(0,15) :
                                print('Clicking on JOIN Now!')
                                start1 = pyautogui.locateCenterOnScreen('Join.png')
                                if start1 != None :
                                    pyautogui.click(start1)        
                                    x=10
                                    break
                                time.sleep(2)
                            break
                        elif direct_lucky_join != None :
                            print('Clicking on JOIN Now!')
                            time.sleep(2)
                            pyautogui.click(start1)        
                            x=10
                            break
                        time.sleep(2)
                    break
                time.sleep(2)
            if x == 10 :
                break
        # elif startover != 0:
        #     print('Start Over')
        #     for j in range (0,4):
        #         signing_in(meeting_id)
        #         if j == 3:
        #             break
        elif i == 29 :
            signing_in(meeting_id)#,passkey)
            print("Trying to sign in again")        
        
        time.sleep(2)

    for i in range(0,15):
        time.sleep(2)
        id = pyautogui.locateCenterOnScreen('meeting ID.png')
        print('entering the meeting ID and moving ahead')
        if id != None :
            print('typing now')
            pyautogui.click(id)
            pyautogui.write(meeting_id)
            pyautogui.press("enter")
            break
    """
    # *******************************************
    # If password section is added any other time
    # *******************************************

    for i in range(0,15):
        time.sleep(5)
        passwords = pyautogui.locateCenterOnScreen('Passcode.png')
        print('entering the password and moving ahead')
        if passwords != None :
            print('typing now')
            pyautogui.click(passwords)
            pyautogui.write(passkey)
            pyautogui.press("enter")
            break
    
    """
    return
