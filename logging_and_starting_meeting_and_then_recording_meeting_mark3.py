import numpy as np
import os              
import pandas as pd    
import pyautogui
import time
from datetime import datetime


"""

***********************************************************************************************
THIS RECORDING CODE IS BIT GLITCHY AND YOU MIGHT HAVE TO TWEAK IT A BIT BASED ON YOUR SYSTEM
BUT IF YOU JUST WANT THE CODE TO SWITCH ON THE LECTURES AND NOT RECORD THEM THEN YOU CAN USE
THE OTHER FILE WHICH IS MADE JUST FOR THAT.

***********************************************************************************************

"""


def signing_in(meeting_id):
    #, passkey):
    """
    The code when given the meeting id
    and password starts the zoom application
    waits for it to start writes the id and password
    and logins in and starts the meeting for you
    and maybe starts recording it too
    """

    os.startfile("C:\\Users\\NAMAN\\AppData\\Roaming\\Zoom\\bin\\zoom.exe")
    print("Hello!")
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
            signing_in(meeting_id) #,passkey)

            print("Trying to sign in again")        
        
        time.sleep(2)
    a = 0
    for i in range(0,15):
        time.sleep(2)
        id = pyautogui.locateCenterOnScreen('meeting ID.png')
        print('entering the meeting ID and moving ahead')
        if id != None :
            print('typing now')
            pyautogui.click(id)
            pyautogui.write(meeting_id)
            pyautogui.press("enter")
            a = 1
            break
    
    if a != 1:
        signing_in(meeting_id)#,passkey)
    """
    #For Password protected meetings

    for i in range(0,15):
        time.sleep(5)
        passwords = pyautogui.locateCenterOnScreen('Passcode.png')
        print('entering the password and moving ahead')
        if passwords != None :
            print('typing now')
            pyautogui.click(passwords)
            pyautogui.write(passkey)
            pyautogui.press("enter")
            a = a + 1
            break
    
    if a != 2:
        signing_in(meeting_id)#, passkey)
    """

    for  i in range (0,20):
        time.sleep(15)
        connecting = pyautogui.locateCenterOnScreen('loading.png')
        time.sleep(2)
        host_is_late = pyautogui.locateCenterOnScreen('The host will start the meeting.png')
        if host_is_late == None and connecting == None:            
            for i in range(0,20):
                time.sleep(15)
                waiting_room = pyautogui.locateCenterOnScreen('Waiting line.png')
                connecting = pyautogui.locateCenterOnScreen('loading.png')
                if waiting_room == None and connecting == None and host_is_late == None:    #just to be double sure
                    # return_to_meeting = pyautogui.locateCenterOnScreen('return_to_the_meeting.png')
                    # pyautogui.click(return_to_meeting)
                    print('the meeting has stared...')
                    time.sleep(2)
                    pyautogui.doubleClick()
                    time.sleep(2)
                    pyautogui.hotkey('alt','tab')
                    time.sleep(2)

                    pyautogui.hotkey('win','up')
                    # pyautogui.screenshot(r"C:\Users\NAMAN\Downloads\screenshot1.png")
                    time.sleep(2)
                    return_to_meeting = pyautogui.locateCenterOnScreen('return_to_the_meeting.png')
                    # print(return_to_meeting)
                    time.sleep(2)
                    if return_to_meeting != None:
                        pyautogui.hotkey('alt','tab')
                        time.sleep(2)
                        pyautogui.hotkey('win','up')
                    pyautogui.hotkey('win','alt','r')
                    print('the recording has started...')
                    # return 1
                    break
            break
    
    # for i in range():
    #     time.sleep(5)
    #     just_start_recording_again = pyautogui.locateCenterOnScreen('if recording stops in between.png')
    #     if just_start_recording_again != None :
    #         pyautogui.hotkey('win','alt','r')
    #     if 
    return