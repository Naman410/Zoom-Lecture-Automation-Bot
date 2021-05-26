import numpy as np
import os              
import pyautogui
import time
from datetime import datetime
# import logging_and_starting_meeting_mark1 as logging
import logging_and_starting_meeting_mark2 as logging
# import logging_and_starting_meeting_and_then_recording_meeting_mark1 as logging
# import logging_and_starting_meeting_and_then_recording_meeting_mark2 as logging
# import logging_and_starting_meeting_and_then_recording_meeting_mark3 as logging

# day = datetime.now().strftime("%H:%M")
# print_with_time(day)
# i=0
# j = 0
pyautogui.PAUSE = 2

"""

*******************************************************************************************************
THIS CODE IS WRITTEN FOR A PARTICULAR TIME TABLE AND PARTICULARLLY TOTAL 5 SUBJECTS IN THE PORTION
YOU CAN EDIT THE CODE BASED ON YOUR NEEDS

*******************************************************************************************************

"""
def print_with_time(data, data1 = None, data2 = None):
    present_time = float(datetime.now().strftime("%H.%M"))
    if data1 == None :
        print (data,"     //", present_time)
    elif data2 == None:
        print (data, data1, "     //", present_time)
    else:
        print (data, data1, data2, "     //", present_time)
# print_with_time("Naman is awesome")


def computer_on():
    """
    clicks enter and enters the computer password to unlock the pc
    """
    pyautogui.press('enter')
    pyautogui.write('4615')


def network_connection_check():
    """network_connection_check()
    
    To check if the computer is 
    connected to a network or not"""


def close():
    """
    leave the meeting and completely
    close the zoom application
    """
    wait = pyautogui.locateCenterOnScreen('please wait for host.jpg')
    if wait != None :
        pyautogui.hotkey('alt','f4')
    else :
        pyautogui.hotkey('alt','q')
    # leave_button = pyautogui.locateCenterOnScreen('leave meeting.png')
    # pyautogui.click(leave_button)
    # closing_zoom_app = pyautogui.locateCenterOnScreen('closes zoom app first.png')
    # pyautogui.click(closing_zoom_app)
    time.sleep(3)
    pyautogui.hotkey('alt','f4')
    time.sleep(2)
    up_arrow = pyautogui.locateCenterOnScreen('up_arrow_key.png')
    pyautogui.click(up_arrow)
    zoom_sign = pyautogui.locateCenterOnScreen('right click zoom.png')
    pyautogui.click(zoom_sign, button='right')
    exit_zoom = pyautogui.locateCenterOnScreen('exit.png')
    pyautogui.click(exit_zoom)
    return



def manual_time_table():
    """
    temporarily fixed timetable schedule
    """
    chemistry = "3546515974"                            #"Meeting ID of Subject 1 in my case computer"
    electrical_engineering_lab = "5027946685"           #"Meeting ID of Subject 2 in my case english"
    workshop = "95099235753"                               #"Meeting ID of subject 3 in my case engineerig graphics"
    sociology = "9187053280"                           #"Meeting ID of subject 4 in my case physics"
    maths =     "3464612000"                            #"meeting ID of subject 5 in my case maths"

    day = datetime.now().strftime("%a")
    
    if day.lower() == 'mon':
        print_with_time("Today is monday")
        n = 0
        while True:
            present_time = float(datetime.now().strftime("%H.%M"))
            present_time_in_minutes = int((present_time - int(present_time))*100)
            if present_time >= 08.30 and present_time < 09.32 and n!= 1 :
                print_with_time('First lecture started')

                logging.signing_in(chemistry)
                
                print_with_time('We are in the first lecture')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 32 :
                    present_left_time = 9.32 - present_present_time
                elif present_present_time_in_minutes > 32 :
                    present_left_time = 9.32 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                # print_with_time('sleeping...')
                # time.sleep(present_left_time_in_seconds)
                # print_with_time("Checking...")
                # for_for_loop = (present_left_time_in_seconds/3)+1
                # for_for_loop = int(for_for_loop)
                # print_with_time("In loop for this many times:",for_for_loop)
                # for i in range(0, for_for_loop):
                #     time.sleep(3)
                #     just_start_recording_again = pyautogui.locateCenterOnScreen('if recording stops in between.png')
                #     recording_sign = pyautogui.locateCenterOnScreen('recording_sign.png')
                #     meeting_ended_1 = pyautogui.locateCenterOnScreen('meeting has been ended by the host.png')
                #     meeting_ended_2 = pyautogui.locateCenterOnScreen('meeting has been ended by the host2.png')
                #     meeting_ended_3 = pyautogui.locateCenterOnScreen('meeting has been ended by the host3.png')
                #     meeting_ended_4 = pyautogui.locateCenterOnScreen('meeting has been ended by the host4.png')
                #     join_button = pyautogui.locateCenterOnScreen('Join.png')
                #     if meeting_ended_1 != None or meeting_ended_2 != None or meeting_ended_3 != None or meeting_ended_4 != None or join_button != None :
                #         break
                #     if just_start_recording_again != None  or recording_sign == None:
                #         pyautogui.screenshot(r"C:\\Users\\NAMAN\\Videos\\Captures\\For Development Purposes\\screenshot1.png")
                        # pyautogui.hotkey('win','alt','r')
                # present_present_time = float(datetime.now().strftime("%H.%M"))
                # present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                # if present_present_time_in_minutes <= 32 :
                #     present_left_time = 9.32 - present_present_time
                # elif present_present_time_in_minutes > 32 :
                #     present_left_time = 9.32 - present_present_time - 0.4
                # present_left_time_in_hours = int(present_left_time)
                # present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                # present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                if present_left_time_in_seconds >= 0 :
                    print_with_time('sleeping...')
                    time.sleep(present_left_time_in_seconds)
                else :
                    print_with_time('Time up, no time for sleep, none of the lectures ended early')
                n = 1
            elif present_time >= 09.32 and present_time < 09.45 and n!= 2:    #just to be on the safe side 2mins extra
                if n != 0:
                    close()
                print_with_time('First lecture ended')                                
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 45 :
                    present_left_time = 9.45 - present_present_time
                elif present_present_time_in_minutes > 45 :
                    present_left_time = 9.45 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                print_with_time('Next lecture starts in...',present_left_time)
                print_with_time('sleeping...')
                time.sleep(present_left_time_in_seconds)
                n = 2

            elif present_time >= 09.45 and present_time < 10.47 and  n!= 3:
                print_with_time('Second lecture started')

                logging.signing_in(electrical_engineering_lab)
                
                print_with_time('We are in the second lecture')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 47 :
                    present_left_time = 10.47 - present_present_time
                elif present_present_time_in_minutes > 47 :
                    present_left_time = 10.47 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                # print_with_time('sleeping...')
                # time.sleep(present_left_time_in_seconds)
                # print_with_time("Checking...")
                # for_for_loop = (present_left_time_in_seconds/3)+1
                # for_for_loop = int(for_for_loop)
                # print_with_time("In loop for this many times:",for_for_loop)
                # for i in range(0, for_for_loop):
                #     time.sleep(3)
                #     just_start_recording_again = pyautogui.locateCenterOnScreen('if recording stops in between.png')
                #     recording_sign = pyautogui.locateCenterOnScreen('recording_sign.png')
                #     meeting_ended_1 = pyautogui.locateCenterOnScreen('meeting has been ended by the host.png')
                #     meeting_ended_2 = pyautogui.locateCenterOnScreen('meeting has been ended by the host2.png')
                #     meeting_ended_3 = pyautogui.locateCenterOnScreen('meeting has been ended by the host3.png')
                #     meeting_ended_4 = pyautogui.locateCenterOnScreen('meeting has been ended by the host4.png')
                #     join_button = pyautogui.locateCenterOnScreen('Join.png')
                #     if meeting_ended_1 != None or meeting_ended_2 != None or meeting_ended_3 != None or meeting_ended_4 != None or join_button != None :
                #         break
                #     if just_start_recording_again != None  or recording_sign == None:
                #         pyautogui.screenshot(r"C:\\Users\\NAMAN\\Videos\\Captures\\For Development Purposes\\screenshot2.png")
                        # pyautogui.hotkey('win','alt','r')
                # present_present_time = float(datetime.now().strftime("%H.%M"))
                # present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                # if present_present_time_in_minutes <= 47 :
                #     present_left_time = 10.47 - present_present_time
                # elif present_present_time_in_minutes > 47 :
                #     present_left_time = 10.47 - present_present_time - 0.4
                # present_left_time_in_hours = int(present_left_time)
                # present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                # present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                if present_left_time_in_seconds >= 0 :
                    print_with_time('sleeping...')
                    time.sleep(present_left_time_in_seconds)
                else :
                    print_with_time('Time up, no time for sleep, none of the lectures ended early')
                n = 3
            elif present_time >= 10.47 and present_time < 11.30  and n!= 4:
                if n != 0:
                    close()
                print_with_time('Second ecture Ended')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 30 :
                    present_left_time = 11.30 - present_present_time
                elif present_present_time_in_minutes > 30 :
                    present_left_time = 11.30 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                print_with_time('Next lecture starts in...',present_left_time)
                print_with_time('sleeping...')
                time.sleep(present_left_time_in_seconds)
                n = 4

            elif present_time >= 11.30 and present_time < 12.32 and n!= 5:
                print_with_time('Third lecture started')

                logging.signing_in(maths)
                
                print_with_time('We are in the third lecture')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 32 :
                    present_left_time = 12.32 - present_present_time
                elif present_present_time_in_minutes > 32 :
                    present_left_time = 12.32 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                # print_with_time('sleeping...')
                # time.sleep(present_left_time_in_seconds)
                # print_with_time("Checking...")
                # for_for_loop = (present_left_time_in_seconds/3)+1
                # for_for_loop = int(for_for_loop)
                # print_with_time("In loop for this many times:",for_for_loop)
                # for i in range(0, for_for_loop):
                #     time.sleep(3)
                #     just_start_recording_again = pyautogui.locateCenterOnScreen('if recording stops in between.png')
                #     recording_sign = pyautogui.locateCenterOnScreen('recording_sign.png')
                #     meeting_ended_1 = pyautogui.locateCenterOnScreen('meeting has been ended by the host.png')
                #     meeting_ended_2 = pyautogui.locateCenterOnScreen('meeting has been ended by the host2.png')
                #     meeting_ended_3 = pyautogui.locateCenterOnScreen('meeting has been ended by the host3.png')
                #     meeting_ended_4 = pyautogui.locateCenterOnScreen('meeting has been ended by the host4.png')
                #     join_button = pyautogui.locateCenterOnScreen('Join.png')
                #     if meeting_ended_1 != None or meeting_ended_2 != None or meeting_ended_3 != None or meeting_ended_4 != None or join_button != None :
                #         break
                #     if just_start_recording_again != None  or recording_sign == None:
                #         pyautogui.screenshot(r"C:\\Users\\NAMAN\\Videos\\Captures\\For Development Purposes\\screenshot3.png")
                        # pyautogui.hotkey('win','alt','r')
                # present_present_time = float(datetime.now().strftime("%H.%M"))
                # present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                # if present_present_time_in_minutes <= 32 :
                #     present_left_time = 12.32 - present_present_time
                # elif present_present_time_in_minutes > 32 :
                #     present_left_time = 12.32 - present_present_time - 0.4
                # present_left_time_in_hours = int(present_left_time)
                # present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                # present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                if present_left_time_in_seconds >= 0 :
                    print_with_time('sleeping...')
                    time.sleep(present_left_time_in_seconds)
                else :
                    print_with_time('Time up, no time for sleep, none of the lectures ended early')
                n = 5
            elif present_time >= 12.32 and present_time < 14.00 and n!= 6:
                if n != 0:
                    close()
                print_with_time('Third lecture ended')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 0 :
                    present_left_time = 14.00 - present_present_time
                elif present_present_time_in_minutes > 0 :
                    present_left_time = 14.00 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                print_with_time('Next lecture starts in...',present_left_time)
                print_with_time('sleeping...')
                time.sleep(present_left_time_in_seconds)
                n = 6

            elif present_time >= 14.00 and present_time < 15.02 and n!= 7:
                print_with_time('Fourth lecture started')

                logging.signing_in(electrical_engineering_lab)
                
                print_with_time('We are in the fourth lecture')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 0 :
                    present_left_time = 15.02 - present_present_time
                elif present_present_time_in_minutes > 0 :
                    present_left_time = 15.02 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                # print_with_time('sleeping...')
                # time.sleep(present_left_time_in_seconds)
                # print_with_time("Checking...")
                # for_for_loop = (present_left_time_in_seconds/3)+1
                # for_for_loop = int(for_for_loop)
                # print_with_time("In loop for this many times:",for_for_loop)
                # for i in range(0, for_for_loop):
                #     time.sleep(3)
                #     just_start_recording_again = pyautogui.locateCenterOnScreen('if recording stops in between.png')
                #     recording_sign = pyautogui.locateCenterOnScreen('recording_sign.png')
                #     meeting_ended_1 = pyautogui.locateCenterOnScreen('meeting has been ended by the host.png')
                #     meeting_ended_2 = pyautogui.locateCenterOnScreen('meeting has been ended by the host2.png')
                #     meeting_ended_3 = pyautogui.locateCenterOnScreen('meeting has been ended by the host3.png')
                #     meeting_ended_4 = pyautogui.locateCenterOnScreen('meeting has been ended by the host4.png')
                #     join_button = pyautogui.locateCenterOnScreen('Join.png')
                #     if meeting_ended_1 != None or meeting_ended_2 != None or meeting_ended_3 != None or meeting_ended_4 != None or join_button != None :
                #         break
                #     if just_start_recording_again != None  or recording_sign == None:
                #         pyautogui.screenshot(r"C:\\Users\\NAMAN\\Videos\\Captures\\For Development Purposes\\screenshot4.png")
                        # pyautogui.hotkey('win','alt','r')
                # present_present_time = float(datetime.now().strftime("%H.%M"))
                # present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                # if present_present_time_in_minutes <= 0 :
                #     present_left_time = 15.02 - present_present_time
                # elif present_present_time_in_minutes > 0 :
                #     present_left_time = 15.02 - present_present_time - 0.4
                # present_left_time_in_hours = int(present_left_time)
                # present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                # present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                if present_left_time_in_seconds >= 0 :
                    print_with_time('sleeping...')
                    time.sleep(present_left_time_in_seconds)
                else :
                    print_with_time('Time up, no time for sleep, none of the lectures ended early')
                n = 7
            elif present_time >= 15.02 and n != 0 and n!= 8:
                if n != 0:
                    close()
                print_with_time('Fourth lecture ended')
                print_with_time('All dlasses done for the day buddy!')
                n = 8
            
            elif present_time < 8.30:
                if present_time_in_minutes > 30:
                    time_left = 8.30 - present_time - 0.40
                else:
                    time_left = 8.30 - present_time
                time_left = round(time_left,2)
                time_left_in_hours = int(time_left)
                # print_with_time('Next lecture starts in...',present_left_time)
                time_left_in_minutes = int((time_left - int(time_left))*100)
                time_left_in_seconds =( (time_left_in_minutes * 60 + time_left_in_hours * 3600) + 60)
                print_with_time('The next class is in :',time_left)
                print_with_time('sleeping...')
                time.sleep(time_left_in_seconds)
            elif present_time > 15.02:
                if present_time_in_minutes != 0:
                    time_left = (24.00 - present_time - 0.40) 
                else:
                    time_left = (24.00 - present_time)   
                time_left = round(time_left,2)
                time_left_in_hours = int(time_left)
                time_left_in_minutes = int((time_left - int(time_left))*100)
                time_left_in_seconds =( (time_left_in_minutes * 60 + time_left_in_hours * 3600) + 60)
                print_with_time('The next day starts in :',time_left,'hrs')
                print_with_time(time_left_in_seconds)
                print_with_time('sleeping...')
                time.sleep(time_left_in_seconds)
                manual_time_table()
            
    elif day.lower() == 'tue':
        print_with_time("Today is tuesday")
        n = 0
        while True:
            present_time = float(datetime.now().strftime("%H.%M"))
            present_time_in_minutes = int((present_time - int(present_time))*100)
            if present_time >= 08.30 and present_time < 09.32 and n!= 1 :
                print_with_time('First lecture started')

                logging.signing_in(chemistry)
                
                print_with_time('We are in the first lecture')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 32 :
                    present_left_time = 9.32 - present_present_time
                elif present_present_time_in_minutes > 32 :
                    present_left_time = 9.32 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                # print_with_time('sleeping...')
                # time.sleep(present_left_time_in_seconds)
                # print_with_time("Checking...")
                # for_for_loop = (present_left_time_in_seconds/3)+1
                # for_for_loop = int(for_for_loop)
                # print_with_time("In loop for this many times:",for_for_loop)
                # for i in range(0, for_for_loop):
                #     time.sleep(3)
                #     just_start_recording_again = pyautogui.locateCenterOnScreen('if recording stops in between.png')
                #     recording_sign = pyautogui.locateCenterOnScreen('recording_sign.png')
                #     meeting_ended_1 = pyautogui.locateCenterOnScreen('meeting has been ended by the host.png')
                #     meeting_ended_2 = pyautogui.locateCenterOnScreen('meeting has been ended by the host2.png')
                #     meeting_ended_3 = pyautogui.locateCenterOnScreen('meeting has been ended by the host3.png')
                #     meeting_ended_4 = pyautogui.locateCenterOnScreen('meeting has been ended by the host4.png')
                #     join_button = pyautogui.locateCenterOnScreen('Join.png')
                #     if meeting_ended_1 != None or meeting_ended_2 != None or meeting_ended_3 != None or meeting_ended_4 != None or join_button != None :
                #         break
                #     if just_start_recording_again != None  or recording_sign == None:
                #         pyautogui.screenshot(r"C:\\Users\\NAMAN\\Videos\\Captures\\For Development Purposes\\screenshot1.png")
                        # pyautogui.hotkey('win','alt','r')
                # present_present_time = float(datetime.now().strftime("%H.%M"))
                # present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                # if present_present_time_in_minutes <= 32 :
                #     present_left_time = 9.32 - present_present_time
                # elif present_present_time_in_minutes > 32 :
                #     present_left_time = 9.32 - present_present_time - 0.4
                # present_left_time_in_hours = int(present_left_time)
                # present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                # present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                if present_left_time_in_seconds >= 0 :
                    print_with_time('sleeping...')
                    time.sleep(present_left_time_in_seconds)
                else :
                    print_with_time('Time up, no time for sleep, none of the lectures ended early')
                n = 1
            elif present_time >= 09.32 and present_time < 09.45 and n!= 2:    #just to be on the safe side 2mins extra
                if n != 0:
                    close()
                print_with_time('First lecture ended')                                
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 45 :
                    present_left_time = 9.45 - present_present_time
                elif present_present_time_in_minutes > 45 :
                    present_left_time = 9.45 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                print_with_time('Next lecture starts in...',present_left_time)
                print_with_time('sleeping...')
                time.sleep(present_left_time_in_seconds)
                n = 2

            elif present_time >= 09.45 and present_time < 10.47 and  n!= 3:
                print_with_time('Second lecture started')

                logging.signing_in(maths)
                
                print_with_time('We are in the second lecture')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 47 :
                    present_left_time = 10.47 - present_present_time
                elif present_present_time_in_minutes > 47 :
                    present_left_time = 10.47 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                # print_with_time('sleeping...')
                # time.sleep(present_left_time_in_seconds)
                # print_with_time("Checking...")
                # for_for_loop = (present_left_time_in_seconds/3)+1
                # for_for_loop = int(for_for_loop)
                # print_with_time("In loop for this many times:",for_for_loop)
                # for i in range(0, for_for_loop):
                #     time.sleep(3)
                #     just_start_recording_again = pyautogui.locateCenterOnScreen('if recording stops in between.png')
                #     recording_sign = pyautogui.locateCenterOnScreen('recording_sign.png')
                #     meeting_ended_1 = pyautogui.locateCenterOnScreen('meeting has been ended by the host.png')
                #     meeting_ended_2 = pyautogui.locateCenterOnScreen('meeting has been ended by the host2.png')
                #     meeting_ended_3 = pyautogui.locateCenterOnScreen('meeting has been ended by the host3.png')
                #     meeting_ended_4 = pyautogui.locateCenterOnScreen('meeting has been ended by the host4.png')
                #     join_button = pyautogui.locateCenterOnScreen('Join.png')
                #     if meeting_ended_1 != None or meeting_ended_2 != None or meeting_ended_3 != None or meeting_ended_4 != None or join_button != None :
                #         break
                #     if just_start_recording_again != None  or recording_sign == None:
                #         pyautogui.screenshot(r"C:\\Users\\NAMAN\\Videos\\Captures\\For Development Purposes\\screenshot2.png")
                        # pyautogui.hotkey('win','alt','r')
                # present_present_time = float(datetime.now().strftime("%H.%M"))
                # present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                # if present_present_time_in_minutes <= 47 :
                #     present_left_time = 10.47 - present_present_time
                # elif present_present_time_in_minutes > 47 :
                #     present_left_time = 10.47 - present_present_time - 0.4
                # present_left_time_in_hours = int(present_left_time)
                # present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                # present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                if present_left_time_in_seconds >= 0 :
                    print_with_time('sleeping...')
                    time.sleep(present_left_time_in_seconds)
                else :
                    print_with_time('Time up, no time for sleep, none of the lectures ended early')
                n = 3
            elif present_time >= 10.47 and present_time < 11.30  and n!= 4:
                if n != 0:
                    close()
                print_with_time('Second ecture Ended')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 30 :
                    present_left_time = 11.30 - present_present_time
                elif present_present_time_in_minutes > 30 :
                    present_left_time = 11.30 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                print_with_time('Next lecture starts in...',present_left_time)
                print_with_time('sleeping...')
                time.sleep(present_left_time_in_seconds)
                n = 4

            elif present_time >= 11.30 and present_time < 12.32 and n!= 5:
                print_with_time('Third lecture started')

                logging.signing_in(chemistry)
                
                print_with_time('We are in the third lecture')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 32 :
                    present_left_time = 12.32 - present_present_time
                elif present_present_time_in_minutes > 32 :
                    present_left_time = 12.32 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                # print_with_time('sleeping...')
                # time.sleep(present_left_time_in_seconds)
                # print_with_time("Checking...")
                # for_for_loop = (present_left_time_in_seconds/3)+1
                # for_for_loop = int(for_for_loop)
                # print_with_time("In loop for this many times:",for_for_loop)
                # for i in range(0, for_for_loop):
                #     time.sleep(3)
                #     just_start_recording_again = pyautogui.locateCenterOnScreen('if recording stops in between.png')
                #     recording_sign = pyautogui.locateCenterOnScreen('recording_sign.png')
                #     meeting_ended_1 = pyautogui.locateCenterOnScreen('meeting has been ended by the host.png')
                #     meeting_ended_2 = pyautogui.locateCenterOnScreen('meeting has been ended by the host2.png')
                #     meeting_ended_3 = pyautogui.locateCenterOnScreen('meeting has been ended by the host3.png')
                #     meeting_ended_4 = pyautogui.locateCenterOnScreen('meeting has been ended by the host4.png')
                #     join_button = pyautogui.locateCenterOnScreen('Join.png')
                #     if meeting_ended_1 != None or meeting_ended_2 != None or meeting_ended_3 != None or meeting_ended_4 != None or join_button != None :
                #         break
                #     if just_start_recording_again != None  or recording_sign == None:
                #         pyautogui.screenshot(r"C:\\Users\\NAMAN\\Videos\\Captures\\For Development Purposes\\screenshot3.png")
                        # pyautogui.hotkey('win','alt','r')
                # present_present_time = float(datetime.now().strftime("%H.%M"))
                # present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                # if present_present_time_in_minutes <= 32 :
                #     present_left_time = 12.32 - present_present_time
                # elif present_present_time_in_minutes > 32 :
                #     present_left_time = 12.32 - present_present_time - 0.4
                # present_left_time_in_hours = int(present_left_time)
                # present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                # present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                if present_left_time_in_seconds >= 0 :
                    print_with_time('sleeping...')
                    time.sleep(present_left_time_in_seconds)
                else :
                    print_with_time('Time up, no time for sleep, none of the lectures ended early')
                n = 5
            elif present_time >= 12.32 and present_time < 14.00 and n!= 6:
                if n != 0:
                    close()
                print_with_time('Third lecture ended')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 0 :
                    present_left_time = 14.00 - present_present_time
                elif present_present_time_in_minutes > 0 :
                    present_left_time = 14.00 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                print_with_time('Next lecture starts in...',present_left_time)
                print_with_time('sleeping...')
                time.sleep(present_left_time_in_seconds)
                n = 6

            elif present_time >= 14.00 and present_time < 15.02 and n!= 7:
                print_with_time('Fourth lecture started')

                logging.signing_in(sociology)
                
                print_with_time('We are in the fourth lecture')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 0 :
                    present_left_time = 15.02 - present_present_time
                elif present_present_time_in_minutes > 0 :
                    present_left_time = 15.02 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                # print_with_time('sleeping...')
                # time.sleep(present_left_time_in_seconds)
                # print_with_time("Checking...")
                # for_for_loop = (present_left_time_in_seconds/3)+1
                # for_for_loop = int(for_for_loop)
                # print_with_time("In loop for this many times:",for_for_loop)
                # for i in range(0, for_for_loop):
                #     time.sleep(3)
                #     just_start_recording_again = pyautogui.locateCenterOnScreen('if recording stops in between.png')
                #     recording_sign = pyautogui.locateCenterOnScreen('recording_sign.png')
                #     meeting_ended_1 = pyautogui.locateCenterOnScreen('meeting has been ended by the host.png')
                #     meeting_ended_2 = pyautogui.locateCenterOnScreen('meeting has been ended by the host2.png')
                #     meeting_ended_3 = pyautogui.locateCenterOnScreen('meeting has been ended by the host3.png')
                #     meeting_ended_4 = pyautogui.locateCenterOnScreen('meeting has been ended by the host4.png')
                #     join_button = pyautogui.locateCenterOnScreen('Join.png')
                #     if meeting_ended_1 != None or meeting_ended_2 != None or meeting_ended_3 != None or meeting_ended_4 != None or join_button != None :
                #         break
                #     if just_start_recording_again != None  or recording_sign == None:
                #         pyautogui.screenshot(r"C:\\Users\\NAMAN\\Videos\\Captures\\For Development Purposes\\screenshot4.png")
                        # pyautogui.hotkey('win','alt','r')
                # present_present_time = float(datetime.now().strftime("%H.%M"))
                # present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                # if present_present_time_in_minutes <= 0 :
                #     present_left_time = 15.02 - present_present_time
                # elif present_present_time_in_minutes > 0 :
                #     present_left_time = 15.02 - present_present_time - 0.4
                # present_left_time_in_hours = int(present_left_time)
                # present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                # present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                if present_left_time_in_seconds >= 0 :
                    print_with_time('sleeping...')
                    time.sleep(present_left_time_in_seconds)
                else :
                    print_with_time('Time up, no time for sleep, none of the lectures ended early')
                n = 7
            elif present_time >= 15.02 and n != 0 and n!= 8:
                if n != 0:
                    close()
                print_with_time('Fourth lecture ended')
                print_with_time('All dlasses done for the day buddy!')
                n = 8
            
            elif present_time < 8.30:
                if present_time_in_minutes > 30:
                    time_left = 8.30 - present_time - 0.40
                else:
                    time_left = 8.30 - present_time
                time_left = round(time_left,2)
                time_left_in_hours = int(time_left)
                # print_with_time('Next lecture starts in...',present_left_time)
                time_left_in_minutes = int((time_left - int(time_left))*100)
                time_left_in_seconds =( (time_left_in_minutes * 60 + time_left_in_hours * 3600) + 60)
                print_with_time('The next class is in :',time_left)
                # print_with_time(time_left_in_seconds)
                print_with_time('sleeping...')
                time.sleep(time_left_in_seconds)
            elif present_time > 15.02:
                if present_time_in_minutes != 0:
                    time_left = (24.00 - present_time - 0.40) 
                else:
                    time_left = (24.00 - present_time)   
                time_left = round(time_left,2)
                time_left_in_hours = int(time_left)
                time_left_in_minutes = int((time_left - int(time_left))*100)
                time_left_in_seconds =( (time_left_in_minutes * 60 + time_left_in_hours * 3600) + 60)
                print_with_time('The next day starts in :',time_left,'hrs')
                print_with_time(time_left_in_seconds)
                print_with_time('sleeping...')
                time.sleep(time_left_in_seconds)
                manual_time_table()
            
    elif day.lower() == 'wed':
        print_with_time("Today is wednesday")
        n = 0
        while True:
            present_time = float(datetime.now().strftime("%H.%M"))
            present_time_in_minutes = int((present_time - int(present_time))*100)
            if present_time >= 08.30 and present_time < 09.32 and n!= 1 :
                print_with_time('First lecture started')

                logging.signing_in(electrical_engineering_lab)
                
                print_with_time('We are in the first lecture')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 32 :
                    present_left_time = 9.32 - present_present_time
                elif present_present_time_in_minutes > 32 :
                    present_left_time = 9.32 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                # print_with_time('sleeping...')
                # time.sleep(present_left_time_in_seconds)
                # print_with_time("Checking...")
                # for_for_loop = (present_left_time_in_seconds/3)+1
                # for_for_loop = int(for_for_loop)
                # print_with_time("In loop for this many times:",for_for_loop)
                # for i in range(0, for_for_loop):
                #     time.sleep(3)
                #     just_start_recording_again = pyautogui.locateCenterOnScreen('if recording stops in between.png')
                #     recording_sign = pyautogui.locateCenterOnScreen('recording_sign.png')
                #     meeting_ended_1 = pyautogui.locateCenterOnScreen('meeting has been ended by the host.png')
                #     meeting_ended_2 = pyautogui.locateCenterOnScreen('meeting has been ended by the host2.png')
                #     meeting_ended_3 = pyautogui.locateCenterOnScreen('meeting has been ended by the host3.png')
                #     meeting_ended_4 = pyautogui.locateCenterOnScreen('meeting has been ended by the host4.png')
                #     join_button = pyautogui.locateCenterOnScreen('Join.png')
                #     if meeting_ended_1 != None or meeting_ended_2 != None or meeting_ended_3 != None or meeting_ended_4 != None or join_button != None :
                #         break
                #     if just_start_recording_again != None  or recording_sign == None:
                #         pyautogui.screenshot(r"C:\\Users\\NAMAN\\Videos\\Captures\\For Development Purposes\\screenshot1.png")
                        # pyautogui.hotkey('win','alt','r')
                # present_present_time = float(datetime.now().strftime("%H.%M"))
                # present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                # if present_present_time_in_minutes <= 32 :
                #     present_left_time = 9.32 - present_present_time
                # elif present_present_time_in_minutes > 32 :
                #     present_left_time = 9.32 - present_present_time - 0.4
                # present_left_time_in_hours = int(present_left_time)
                # present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                # present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                if present_left_time_in_seconds >= 0 :
                    print_with_time('sleeping...')
                    time.sleep(present_left_time_in_seconds)
                else :
                    print_with_time('Time up, no time for sleep, none of the lectures ended early')
                n = 1
            elif present_time >= 09.32 and present_time < 09.45 and n!= 2:    #just to be on the safe side 2mins extra
                if n != 0:
                    close()
                print_with_time('First lecture ended')                                
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 45 :
                    present_left_time = 9.45 - present_present_time
                elif present_present_time_in_minutes > 45 :
                    present_left_time = 9.45 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                print_with_time('Next lecture starts in...',present_left_time)
                print_with_time('sleeping...')
                time.sleep(present_left_time_in_seconds)
                n = 2

            elif present_time >= 09.45 and present_time < 10.47 and  n!= 3:
                print_with_time('Second lecture started')

                logging.signing_in(chemistry)
                
                print_with_time('We are in the second lecture')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 47 :
                    present_left_time = 10.47 - present_present_time
                elif present_present_time_in_minutes > 47 :
                    present_left_time = 10.47 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                # print_with_time('sleeping...')
                # time.sleep(present_left_time_in_seconds)
                # print_with_time("Checking...")
                # for_for_loop = (present_left_time_in_seconds/3)+1
                # for_for_loop = int(for_for_loop)
                # print_with_time("In loop for this many times:",for_for_loop)
                # for i in range(0, for_for_loop):
                #     time.sleep(3)
                #     just_start_recording_again = pyautogui.locateCenterOnScreen('if recording stops in between.png')
                #     recording_sign = pyautogui.locateCenterOnScreen('recording_sign.png')
                #     meeting_ended_1 = pyautogui.locateCenterOnScreen('meeting has been ended by the host.png')
                #     meeting_ended_2 = pyautogui.locateCenterOnScreen('meeting has been ended by the host2.png')
                #     meeting_ended_3 = pyautogui.locateCenterOnScreen('meeting has been ended by the host3.png')
                #     meeting_ended_4 = pyautogui.locateCenterOnScreen('meeting has been ended by the host4.png')
                #     join_button = pyautogui.locateCenterOnScreen('Join.png')
                #     if meeting_ended_1 != None or meeting_ended_2 != None or meeting_ended_3 != None or meeting_ended_4 != None or join_button != None :
                #         break
                #     if just_start_recording_again != None  or recording_sign == None:
                #         pyautogui.screenshot(r"C:\\Users\\NAMAN\\Videos\\Captures\\For Development Purposes\\screenshot2.png")
                        # pyautogui.hotkey('win','alt','r')
                # present_present_time = float(datetime.now().strftime("%H.%M"))
                # present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                # if present_present_time_in_minutes <= 47 :
                #     present_left_time = 10.47 - present_present_time
                # elif present_present_time_in_minutes > 47 :
                #     present_left_time = 10.47 - present_present_time - 0.4
                # present_left_time_in_hours = int(present_left_time)
                # present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                # present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                if present_left_time_in_seconds >= 0 :
                    print_with_time('sleeping...')
                    time.sleep(present_left_time_in_seconds)
                else :
                    print_with_time('Time up, no time for sleep, none of the lectures ended early')
                n = 3
            elif present_time >= 10.47 and present_time < 11.30  and n!= 4:
                if n != 0:
                    close()
                print_with_time('Second ecture Ended')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 30 :
                    present_left_time = 11.30 - present_present_time
                elif present_present_time_in_minutes > 30 :
                    present_left_time = 11.30 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                print_with_time('Next lecture starts in...',present_left_time)
                print_with_time('sleeping...')
                time.sleep(present_left_time_in_seconds)
                n = 4

            elif present_time >= 11.30 and present_time < 12.32 and n!= 5:
                print_with_time('Third lecture started')

                logging.signing_in(maths)
                
                print_with_time('We are in the third lecture')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 32 :
                    present_left_time = 12.32 - present_present_time
                elif present_present_time_in_minutes > 32 :
                    present_left_time = 12.32 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                # print_with_time('sleeping...')
                # time.sleep(present_left_time_in_seconds)
                # print_with_time("Checking...")
                # for_for_loop = (present_left_time_in_seconds/3)+1
                # for_for_loop = int(for_for_loop)
                # print_with_time("In loop for this many times:",for_for_loop)
                # for i in range(0, for_for_loop):
                #     time.sleep(3)
                #     just_start_recording_again = pyautogui.locateCenterOnScreen('if recording stops in between.png')
                #     recording_sign = pyautogui.locateCenterOnScreen('recording_sign.png')
                #     meeting_ended_1 = pyautogui.locateCenterOnScreen('meeting has been ended by the host.png')
                #     meeting_ended_2 = pyautogui.locateCenterOnScreen('meeting has been ended by the host2.png')
                #     meeting_ended_3 = pyautogui.locateCenterOnScreen('meeting has been ended by the host3.png')
                #     meeting_ended_4 = pyautogui.locateCenterOnScreen('meeting has been ended by the host4.png')
                #     join_button = pyautogui.locateCenterOnScreen('Join.png')
                #     if meeting_ended_1 != None or meeting_ended_2 != None or meeting_ended_3 != None or meeting_ended_4 != None or join_button != None :
                #         break
                #     if just_start_recording_again != None  or recording_sign == None:
                #         pyautogui.screenshot(r"C:\\Users\\NAMAN\\Videos\\Captures\\For Development Purposes\\screenshot3.png")
                        # pyautogui.hotkey('win','alt','r')
                # present_present_time = float(datetime.now().strftime("%H.%M"))
                # present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                # if present_present_time_in_minutes <= 32 :
                #     present_left_time = 12.32 - present_present_time
                # elif present_present_time_in_minutes > 32 :
                #     present_left_time = 12.32 - present_present_time - 0.4
                # present_left_time_in_hours = int(present_left_time)
                # present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                # present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                if present_left_time_in_seconds >= 0 :
                    print_with_time('sleeping...')
                    time.sleep(present_left_time_in_seconds)
                else :
                    print_with_time('Time up, no time for sleep, none of the lectures ended early')
                n = 5
            elif present_time >= 12.32 and present_time < 14.00 and n!= 6:
                if n != 0:
                    close()
                print_with_time('Third lecture ended')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 0 :
                    present_left_time = 14.00 - present_present_time
                elif present_present_time_in_minutes > 0 :
                    present_left_time = 14.00 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                print_with_time('Next lecture starts in...',present_left_time)
                print_with_time('sleeping...')
                time.sleep(present_left_time_in_seconds)
                n = 6

            elif present_time >= 14.00 and present_time < 15.02 and n!= 7:
                print_with_time('Fourth lecture started')

                logging.signing_in(workshop)
                
                print_with_time('We are in the fourth lecture')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 0 :
                    present_left_time = 15.02 - present_present_time
                elif present_present_time_in_minutes > 0 :
                    present_left_time = 15.02 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                # print_with_time('sleeping...')
                # time.sleep(present_left_time_in_seconds)
                # print_with_time("Checking...")
                # for_for_loop = (present_left_time_in_seconds/3)+1
                # for_for_loop = int(for_for_loop)
                # print_with_time("In loop for this many times:",for_for_loop)
                # for i in range(0, for_for_loop):
                #     time.sleep(3)
                #     just_start_recording_again = pyautogui.locateCenterOnScreen('if recording stops in between.png')
                #     recording_sign = pyautogui.locateCenterOnScreen('recording_sign.png')
                #     meeting_ended_1 = pyautogui.locateCenterOnScreen('meeting has been ended by the host.png')
                #     meeting_ended_2 = pyautogui.locateCenterOnScreen('meeting has been ended by the host2.png')
                #     meeting_ended_3 = pyautogui.locateCenterOnScreen('meeting has been ended by the host3.png')
                #     meeting_ended_4 = pyautogui.locateCenterOnScreen('meeting has been ended by the host4.png')
                #     join_button = pyautogui.locateCenterOnScreen('Join.png')
                #     if meeting_ended_1 != None or meeting_ended_2 != None or meeting_ended_3 != None or meeting_ended_4 != None or join_button != None :
                #         break
                #     if just_start_recording_again != None  or recording_sign == None:
                #         pyautogui.screenshot(r"C:\\Users\\NAMAN\\Videos\\Captures\\For Development Purposes\\screenshot4.png")
                        # pyautogui.hotkey('win','alt','r')
                # present_present_time = float(datetime.now().strftime("%H.%M"))
                # present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                # if present_present_time_in_minutes <= 0 :
                #     present_left_time = 15.02 - present_present_time
                # elif present_present_time_in_minutes > 0 :
                #     present_left_time = 15.02 - present_present_time - 0.4
                # present_left_time_in_hours = int(present_left_time)
                # present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                # present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                if present_left_time_in_seconds >= 0 :
                    print_with_time('sleeping...')
                    time.sleep(present_left_time_in_seconds)
                else :
                    print_with_time('Time up, no time for sleep, none of the lectures ended early')
                n = 7
            elif present_time >= 15.02 and n != 0 and n!= 8:
                if n != 0:
                    close()
                print_with_time('Fourth lecture ended')
                print_with_time('All dlasses done for the day buddy!')
                n = 8
            
            elif present_time < 8.30:
                if present_time_in_minutes > 30:
                    time_left = 8.30 - present_time - 0.40
                else:
                    time_left = 8.30 - present_time
                time_left = round(time_left,2)
                time_left_in_hours = int(time_left)
                # print_with_time('Next lecture starts in...',present_left_time)
                time_left_in_minutes = int((time_left - int(time_left))*100)
                time_left_in_seconds =( (time_left_in_minutes * 60 + time_left_in_hours * 3600) + 60)
                print_with_time('The next class is in :',time_left)
                print_with_time('sleeping...')
                time.sleep(time_left_in_seconds)
            elif present_time > 15.02:
                if present_time_in_minutes != 0:
                    time_left = (24.00 - present_time - 0.40) 
                else:
                    time_left = (24.00 - present_time)   
                time_left = round(time_left,2)
                time_left_in_hours = int(time_left)
                time_left_in_minutes = int((time_left - int(time_left))*100)
                time_left_in_seconds =( (time_left_in_minutes * 60 + time_left_in_hours * 3600) + 60)
                print_with_time('The next day starts in :',time_left,'hrs')
                print_with_time(time_left_in_seconds)
                print_with_time('sleeping...')
                time.sleep(time_left_in_seconds)
                manual_time_table()
    
    elif day.lower() == 'thu':
        print_with_time("Today is thursday")
        n = 0
        while True:
            present_time = float(datetime.now().strftime("%H.%M"))
            present_time_in_minutes = int((present_time - int(present_time))*100)
            if present_time >= 08.30 and present_time < 09.32 and n!= 1 :
                print_with_time('First lecture started')

                logging.signing_in(maths)
                
                print_with_time('We are in the first lecture')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 32 :
                    present_left_time = 9.32 - present_present_time
                elif present_present_time_in_minutes > 32 :
                    present_left_time = 9.32 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                # print_with_time('sleeping...')
                # time.sleep(present_left_time_in_seconds)
                # print_with_time("Checking...")
                # for_for_loop = (present_left_time_in_seconds/3)+1
                # for_for_loop = int(for_for_loop)
                # print_with_time("In loop for this many times:",for_for_loop)
                # for i in range(0, for_for_loop):
                #     time.sleep(3)
                #     just_start_recording_again = pyautogui.locateCenterOnScreen('if recording stops in between.png')
                #     recording_sign = pyautogui.locateCenterOnScreen('recording_sign.png')
                #     meeting_ended_1 = pyautogui.locateCenterOnScreen('meeting has been ended by the host.png')
                #     meeting_ended_2 = pyautogui.locateCenterOnScreen('meeting has been ended by the host2.png')
                #     meeting_ended_3 = pyautogui.locateCenterOnScreen('meeting has been ended by the host3.png')
                #     meeting_ended_4 = pyautogui.locateCenterOnScreen('meeting has been ended by the host4.png')
                #     join_button = pyautogui.locateCenterOnScreen('Join.png')
                #     if meeting_ended_1 != None or meeting_ended_2 != None or meeting_ended_3 != None or meeting_ended_4 != None or join_button != None :
                #         break
                #     if just_start_recording_again != None  or recording_sign == None:
                #         pyautogui.screenshot(r"C:\\Users\\NAMAN\\Videos\\Captures\\For Development Purposes\\screenshot1.png")
                        # pyautogui.hotkey('win','alt','r')
                # present_present_time = float(datetime.now().strftime("%H.%M"))
                # present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                # if present_present_time_in_minutes <= 32 :
                #     present_left_time = 9.32 - present_present_time
                # elif present_present_time_in_minutes > 32 :
                #     present_left_time = 9.32 - present_present_time - 0.4
                # present_left_time_in_hours = int(present_left_time)
                # present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                # present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                if present_left_time_in_seconds >= 0 :
                    print_with_time('sleeping...')
                    time.sleep(present_left_time_in_seconds)
                else :
                    print_with_time('Time up, no time for sleep, none of the lectures ended early')
                n = 1
            elif present_time >= 09.32 and present_time < 09.45 and n!= 2:    #just to be on the safe side 2mins extra
                if n != 0:
                    close()
                print_with_time('First lecture ended')                                
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 45 :
                    present_left_time = 9.45 - present_present_time
                elif present_present_time_in_minutes > 45 :
                    present_left_time = 9.45 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                print_with_time('Next lecture starts in...',present_left_time)
                print_with_time('sleeping...')
                time.sleep(present_left_time_in_seconds)
                n = 2

            elif present_time >= 09.45 and present_time < 10.47 and  n!= 3:
                print_with_time('Second lecture started')

                logging.signing_in(chemistry)
                
                print_with_time('We are in the second lecture')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 47 :
                    present_left_time = 10.47 - present_present_time
                elif present_present_time_in_minutes > 47 :
                    present_left_time = 10.47 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                # print_with_time('sleeping...')
                # time.sleep(present_left_time_in_seconds)
                # print_with_time("Checking...")
                # for_for_loop = (present_left_time_in_seconds/3)+1
                # for_for_loop = int(for_for_loop)
                # print_with_time("In loop for this many times:",for_for_loop)
                # for i in range(0, for_for_loop):
                #     time.sleep(3)
                #     just_start_recording_again = pyautogui.locateCenterOnScreen('if recording stops in between.png')
                #     recording_sign = pyautogui.locateCenterOnScreen('recording_sign.png')
                #     meeting_ended_1 = pyautogui.locateCenterOnScreen('meeting has been ended by the host.png')
                #     meeting_ended_2 = pyautogui.locateCenterOnScreen('meeting has been ended by the host2.png')
                #     meeting_ended_3 = pyautogui.locateCenterOnScreen('meeting has been ended by the host3.png')
                #     meeting_ended_4 = pyautogui.locateCenterOnScreen('meeting has been ended by the host4.png')
                #     join_button = pyautogui.locateCenterOnScreen('Join.png')
                #     if meeting_ended_1 != None or meeting_ended_2 != None or meeting_ended_3 != None or meeting_ended_4 != None or join_button != None :
                #         break
                #     if just_start_recording_again != None  or recording_sign == None:
                #         pyautogui.screenshot(r"C:\\Users\\NAMAN\\Videos\\Captures\\For Development Purposes\\screenshot2.png")
                        # pyautogui.hotkey('win','alt','r')
                # present_present_time = float(datetime.now().strftime("%H.%M"))
                # present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                # if present_present_time_in_minutes <= 47 :
                #     present_left_time = 10.47 - present_present_time
                # elif present_present_time_in_minutes > 47 :
                #     present_left_time = 10.47 - present_present_time - 0.4
                # present_left_time_in_hours = int(present_left_time)
                # present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                # present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                if present_left_time_in_seconds >= 0 :
                    print_with_time('sleeping...')
                    time.sleep(present_left_time_in_seconds)
                else :
                    print_with_time('Time up, no time for sleep, none of the lectures ended early')
                n = 3
            elif present_time >= 10.47 and present_time < 11.30  and n!= 4:
                if n != 0:
                    close()
                print_with_time('Second ecture Ended')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 30 :
                    present_left_time = 11.30 - present_present_time
                elif present_present_time_in_minutes > 30 :
                    present_left_time = 11.30 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                print_with_time('Next lecture starts in...',present_left_time)
                print_with_time('sleeping...')
                time.sleep(present_left_time_in_seconds)
                n = 4

            elif present_time >= 11.30 and present_time < 12.32 and n!= 5:
                print_with_time('Third lecture started')

                logging.signing_in(sociology)
                
                print_with_time('We are in the third lecture')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 32 :
                    present_left_time = 12.32 - present_present_time
                elif present_present_time_in_minutes > 32 :
                    present_left_time = 12.32 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                # print_with_time('sleeping...')
                # time.sleep(present_left_time_in_seconds)
                # print_with_time("Checking...")
                # for_for_loop = (present_left_time_in_seconds/3)+1
                # for_for_loop = int(for_for_loop)
                # print_with_time("In loop for this many times:",for_for_loop)
                # for i in range(0, for_for_loop):
                #     time.sleep(3)
                #     just_start_recording_again = pyautogui.locateCenterOnScreen('if recording stops in between.png')
                #     recording_sign = pyautogui.locateCenterOnScreen('recording_sign.png')
                #     meeting_ended_1 = pyautogui.locateCenterOnScreen('meeting has been ended by the host.png')
                #     meeting_ended_2 = pyautogui.locateCenterOnScreen('meeting has been ended by the host2.png')
                #     meeting_ended_3 = pyautogui.locateCenterOnScreen('meeting has been ended by the host3.png')
                #     meeting_ended_4 = pyautogui.locateCenterOnScreen('meeting has been ended by the host4.png')
                #     join_button = pyautogui.locateCenterOnScreen('Join.png')
                #     if meeting_ended_1 != None or meeting_ended_2 != None or meeting_ended_3 != None or meeting_ended_4 != None or join_button != None :
                #         break
                #     if just_start_recording_again != None  or recording_sign == None:
                #         pyautogui.screenshot(r"C:\\Users\\NAMAN\\Videos\\Captures\\For Development Purposes\\screenshot3.png")
                        # pyautogui.hotkey('win','alt','r')
                # present_present_time = float(datetime.now().strftime("%H.%M"))
                # present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                # if present_present_time_in_minutes <= 32 :
                #     present_left_time = 12.32 - present_present_time
                # elif present_present_time_in_minutes > 32 :
                #     present_left_time = 12.32 - present_present_time - 0.4
                # present_left_time_in_hours = int(present_left_time)
                # present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                # present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                if present_left_time_in_seconds >= 0 :
                    print_with_time('sleeping...')
                    time.sleep(present_left_time_in_seconds)
                else :
                    print_with_time('Time up, no time for sleep, none of the lectures ended early')
                n = 5
            elif present_time >= 12.32 and present_time < 14.00 and n!= 6:
                if n != 0:
                    close()
                print_with_time('Third lecture ended')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 0 :
                    present_left_time = 14.00 - present_present_time
                elif present_present_time_in_minutes > 0 :
                    present_left_time = 14.00 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                print_with_time('Next lecture starts in...',present_left_time)
                print_with_time('sleeping...')
                time.sleep(present_left_time_in_seconds)
                n = 6

            elif present_time >= 14.00 and present_time < 15.02 and n!= 7:
                print_with_time('Fourth lecture started')

                logging.signing_in(electrical_engineering_lab)
                
                print_with_time('We are in the fourth lecture')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 0 :
                    present_left_time = 15.02 - present_present_time
                elif present_present_time_in_minutes > 0 :
                    present_left_time = 15.02 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                # print_with_time('sleeping...')
                # time.sleep(present_left_time_in_seconds)
                # print_with_time("Checking...")
                # for_for_loop = (present_left_time_in_seconds/3)+1
                # for_for_loop = int(for_for_loop)
                # print_with_time("In loop for this many times:",for_for_loop)
                # for i in range(0, for_for_loop):
                #     time.sleep(3)
                #     just_start_recording_again = pyautogui.locateCenterOnScreen('if recording stops in between.png')
                #     recording_sign = pyautogui.locateCenterOnScreen('recording_sign.png')
                #     meeting_ended_1 = pyautogui.locateCenterOnScreen('meeting has been ended by the host.png')
                #     meeting_ended_2 = pyautogui.locateCenterOnScreen('meeting has been ended by the host2.png')
                #     meeting_ended_3 = pyautogui.locateCenterOnScreen('meeting has been ended by the host3.png')
                #     meeting_ended_4 = pyautogui.locateCenterOnScreen('meeting has been ended by the host4.png')
                #     join_button = pyautogui.locateCenterOnScreen('Join.png')
                #     if meeting_ended_1 != None or meeting_ended_2 != None or meeting_ended_3 != None or meeting_ended_4 != None or join_button != None :
                #         break
                #     if just_start_recording_again != None  or recording_sign == None:
                #         pyautogui.screenshot(r"C:\\Users\\NAMAN\\Videos\\Captures\\For Development Purposes\\screenshot4.png")
                        # pyautogui.hotkey('win','alt','r')
                # present_present_time = float(datetime.now().strftime("%H.%M"))
                # present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                # if present_present_time_in_minutes <= 0 :
                #     present_left_time = 15.02 - present_present_time
                # elif present_present_time_in_minutes > 0 :
                #     present_left_time = 15.02 - present_present_time - 0.4
                # present_left_time_in_hours = int(present_left_time)
                # present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                # present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                if present_left_time_in_seconds >= 0 :
                    print_with_time('sleeping...')
                    time.sleep(present_left_time_in_seconds)
                else :
                    print_with_time('Time up, no time for sleep, none of the lectures ended early')
                n = 7
            elif present_time >= 15.02 and n != 0 and n!= 8:
                if n != 0:
                    close()
                print_with_time('Fourth lecture ended')
                print_with_time('All dlasses done for the day buddy!')
                n = 8
            
            elif present_time < 8.30:
                if present_time_in_minutes > 30:
                    time_left = 8.30 - present_time - 0.40
                else:
                    time_left = 8.30 - present_time
                time_left = round(time_left,2)
                time_left_in_hours = int(time_left)
                # print_with_time('Next lecture starts in...',present_left_time)
                time_left_in_minutes = int((time_left - int(time_left))*100)
                time_left_in_seconds =( (time_left_in_minutes * 60 + time_left_in_hours * 3600) + 60)
                print_with_time('The next class is in :',time_left)
                print_with_time('sleeping...')
                time.sleep(time_left_in_seconds)
            elif present_time > 15.02:
                if present_time_in_minutes != 0:
                    time_left = (24.00 - present_time - 0.40) 
                else:
                    time_left = (24.00 - present_time)   
                time_left = round(time_left,2)
                time_left_in_hours = int(time_left)
                time_left_in_minutes = int((time_left - int(time_left))*100)
                time_left_in_seconds =( (time_left_in_minutes * 60 + time_left_in_hours * 3600) + 60)
                print_with_time('The next day starts in :',time_left,'hrs')
                print_with_time(time_left_in_seconds)
                print_with_time('sleeping...')
                time.sleep(time_left_in_seconds)
                manual_time_table()
    
    elif day.lower() == 'fri':
        print_with_time("Today is friday")
        n = 0
        while True:
            present_time = float(datetime.now().strftime("%H.%M"))
            present_time_in_minutes = int((present_time - int(present_time))*100)
            if present_time >= 08.30 and present_time < 09.32 and n!= 1 :
                print_with_time('First lecture started')

                logging.signing_in(sociology)
                
                print_with_time('We are in the first lecture')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 32 :
                    present_left_time = 9.32 - present_present_time
                elif present_present_time_in_minutes > 32 :
                    present_left_time = 9.32 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                # print_with_time('sleeping...')
                # time.sleep(present_left_time_in_seconds)
                # print_with_time("Checking...")
                # for_for_loop = (present_left_time_in_seconds/3)+1
                # for_for_loop = int(for_for_loop)
                # print_with_time("In loop for this many times:",for_for_loop)
                # for i in range(0, for_for_loop):
                #     time.sleep(3)
                #     just_start_recording_again = pyautogui.locateCenterOnScreen('if recording stops in between.png')
                #     recording_sign = pyautogui.locateCenterOnScreen('recording_sign.png')
                #     meeting_ended_1 = pyautogui.locateCenterOnScreen('meeting has been ended by the host.png')
                #     meeting_ended_2 = pyautogui.locateCenterOnScreen('meeting has been ended by the host2.png')
                #     meeting_ended_3 = pyautogui.locateCenterOnScreen('meeting has been ended by the host3.png')
                #     meeting_ended_4 = pyautogui.locateCenterOnScreen('meeting has been ended by the host4.png')
                #     join_button = pyautogui.locateCenterOnScreen('Join.png')
                #     if meeting_ended_1 != None or meeting_ended_2 != None or meeting_ended_3 != None or meeting_ended_4 != None or join_button != None :
                #         break
                #     if just_start_recording_again != None  or recording_sign == None:
                #         pyautogui.screenshot(r"C:\\Users\\NAMAN\\Videos\\Captures\\For Development Purposes\\screenshot1.png")
                        # pyautogui.hotkey('win','alt','r')
                # present_present_time = float(datetime.now().strftime("%H.%M"))
                # present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                # if present_present_time_in_minutes <= 32 :
                #     present_left_time = 9.32 - present_present_time
                # elif present_present_time_in_minutes > 32 :
                #     present_left_time = 9.32 - present_present_time - 0.4
                # present_left_time_in_hours = int(present_left_time)
                # present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                # present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                if present_left_time_in_seconds >= 0 :
                    print_with_time('sleeping...')
                    time.sleep(present_left_time_in_seconds)
                else :
                    print_with_time('Time up, no time for sleep, none of the lectures ended early')
                n = 1
            elif present_time >= 09.32 and present_time < 09.45 and n!= 2:    #just to be on the safe side 2mins extra
                if n != 0:
                    close()
                print_with_time('First lecture ended')                                
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 45 :
                    present_left_time = 9.45 - present_present_time
                elif present_present_time_in_minutes > 45 :
                    present_left_time = 9.45 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                print_with_time('Next lecture starts in...',present_left_time)
                print_with_time('sleeping...')
                time.sleep(present_left_time_in_seconds)
                n = 2

            elif present_time >= 09.45 and present_time < 10.47 and  n!= 3:
                print_with_time('Second lecture started')

                logging.signing_in(electrical_engineering_lab)
                
                print_with_time('We are in the second lecture')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 47 :
                    present_left_time = 10.47 - present_present_time
                elif present_present_time_in_minutes > 47 :
                    present_left_time = 10.47 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                # print_with_time('sleeping...')
                # time.sleep(present_left_time_in_seconds)
                # print_with_time("Checking...")
                # for_for_loop = (present_left_time_in_seconds/3)+1
                # for_for_loop = int(for_for_loop)
                # print_with_time("In loop for this many times:",for_for_loop)
                # for i in range(0, for_for_loop):
                #     time.sleep(3)
                #     just_start_recording_again = pyautogui.locateCenterOnScreen('if recording stops in between.png')
                #     recording_sign = pyautogui.locateCenterOnScreen('recording_sign.png')
                #     meeting_ended_1 = pyautogui.locateCenterOnScreen('meeting has been ended by the host.png')
                #     meeting_ended_2 = pyautogui.locateCenterOnScreen('meeting has been ended by the host2.png')
                #     meeting_ended_3 = pyautogui.locateCenterOnScreen('meeting has been ended by the host3.png')
                #     meeting_ended_4 = pyautogui.locateCenterOnScreen('meeting has been ended by the host4.png')
                #     join_button = pyautogui.locateCenterOnScreen('Join.png')
                #     if meeting_ended_1 != None or meeting_ended_2 != None or meeting_ended_3 != None or meeting_ended_4 != None or join_button != None :
                #         break
                #     if just_start_recording_again != None  or recording_sign == None:
                #         pyautogui.screenshot(r"C:\\Users\\NAMAN\\Videos\\Captures\\For Development Purposes\\screenshot2.png")
                        # pyautogui.hotkey('win','alt','r')
                # present_present_time = float(datetime.now().strftime("%H.%M"))
                # present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                # if present_present_time_in_minutes <= 47 :
                #     present_left_time = 10.47 - present_present_time
                # elif present_present_time_in_minutes > 47 :
                #     present_left_time = 10.47 - present_present_time - 0.4
                # present_left_time_in_hours = int(present_left_time)
                # present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                # present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                if present_left_time_in_seconds >= 0 :
                    print_with_time('sleeping...')
                    time.sleep(present_left_time_in_seconds)
                else :
                    print_with_time('Time up, no time for sleep, none of the lectures ended early')
                n = 3
            elif present_time >= 10.47 and present_time < 11.30  and n!= 4:
                if n != 0:
                    close()
                print_with_time('Second ecture Ended')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 30 :
                    present_left_time = 11.30 - present_present_time
                elif present_present_time_in_minutes > 30 :
                    present_left_time = 11.30 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                print_with_time('Next lecture starts in...',present_left_time)
                print_with_time('sleeping...')
                time.sleep(present_left_time_in_seconds)
                n = 4

            elif present_time >= 11.30 and present_time < 12.32 and n!= 5:
                print_with_time('Third lecture started')

                logging.signing_in(maths)
                
                print_with_time('We are in the third lecture')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 32 :
                    present_left_time = 12.32 - present_present_time
                elif present_present_time_in_minutes > 32 :
                    present_left_time = 12.32 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                # print_with_time('sleeping...')
                # time.sleep(present_left_time_in_seconds)
                # print_with_time("Checking...")
                # for_for_loop = (present_left_time_in_seconds/3)+1
                # for_for_loop = int(for_for_loop)
                # print_with_time("In loop for this many times:",for_for_loop)
                # for i in range(0, for_for_loop):
                #     time.sleep(3)
                #     just_start_recording_again = pyautogui.locateCenterOnScreen('if recording stops in between.png')
                #     recording_sign = pyautogui.locateCenterOnScreen('recording_sign.png')
                #     meeting_ended_1 = pyautogui.locateCenterOnScreen('meeting has been ended by the host.png')
                #     meeting_ended_2 = pyautogui.locateCenterOnScreen('meeting has been ended by the host2.png')
                #     meeting_ended_3 = pyautogui.locateCenterOnScreen('meeting has been ended by the host3.png')
                #     meeting_ended_4 = pyautogui.locateCenterOnScreen('meeting has been ended by the host4.png')
                #     join_button = pyautogui.locateCenterOnScreen('Join.png')
                #     if meeting_ended_1 != None or meeting_ended_2 != None or meeting_ended_3 != None or meeting_ended_4 != None or join_button != None :
                #         break
                #     if just_start_recording_again != None  or recording_sign == None:
                #         pyautogui.screenshot(r"C:\\Users\\NAMAN\\Videos\\Captures\\For Development Purposes\\screenshot3.png")
                        # pyautogui.hotkey('win','alt','r')
                # present_present_time = float(datetime.now().strftime("%H.%M"))
                # present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                # if present_present_time_in_minutes <= 32 :
                #     present_left_time = 12.32 - present_present_time
                # elif present_present_time_in_minutes > 32 :
                #     present_left_time = 12.32 - present_present_time - 0.4
                # present_left_time_in_hours = int(present_left_time)
                # present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                # present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                if present_left_time_in_seconds >= 0 :
                    print_with_time('sleeping...')
                    time.sleep(present_left_time_in_seconds)
                else :
                    print_with_time('Time up, no time for sleep, none of the lectures ended early')
                n = 5
            elif present_time >= 12.32 and present_time < 14.00 and n!= 6:
                if n != 0:
                    close()
                print_with_time('Third lecture ended')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 0 :
                    present_left_time = 14.00 - present_present_time
                elif present_present_time_in_minutes > 0 :
                    present_left_time = 14.00 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                print_with_time('Next lecture starts in...',present_left_time)
                print_with_time('sleeping...')
                time.sleep(present_left_time_in_seconds)
                n = 6

            elif present_time >= 14.00 and present_time < 15.02 and n!= 7:
                print_with_time('Fourth lecture started')

                logging.signing_in(chemistry)
                
                print_with_time('We are in the fourth lecture')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 0 :
                    present_left_time = 15.02 - present_present_time
                elif present_present_time_in_minutes > 0 :
                    present_left_time = 15.02 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                # print_with_time('sleeping...')
                # time.sleep(present_left_time_in_seconds)
                # print_with_time("Checking...")
                # for_for_loop = (present_left_time_in_seconds/3)+1
                # for_for_loop = int(for_for_loop)
                # print_with_time("In loop for this many times:",for_for_loop)
                # for i in range(0, for_for_loop):
                #     time.sleep(3)
                #     just_start_recording_again = pyautogui.locateCenterOnScreen('if recording stops in between.png')
                #     recording_sign = pyautogui.locateCenterOnScreen('recording_sign.png')
                #     meeting_ended_1 = pyautogui.locateCenterOnScreen('meeting has been ended by the host.png')
                #     meeting_ended_2 = pyautogui.locateCenterOnScreen('meeting has been ended by the host2.png')
                #     meeting_ended_3 = pyautogui.locateCenterOnScreen('meeting has been ended by the host3.png')
                #     meeting_ended_4 = pyautogui.locateCenterOnScreen('meeting has been ended by the host4.png')
                #     join_button = pyautogui.locateCenterOnScreen('Join.png')
                #     if meeting_ended_1 != None or meeting_ended_2 != None or meeting_ended_3 != None or meeting_ended_4 != None or join_button != None :
                #         break
                #     if just_start_recording_again != None  or recording_sign == None:
                #         pyautogui.screenshot(r"C:\\Users\\NAMAN\\Videos\\Captures\\For Development Purposes\\screenshot4.png")
                        # pyautogui.hotkey('win','alt','r')
                # present_present_time = float(datetime.now().strftime("%H.%M"))
                # present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                # if present_present_time_in_minutes <= 0 :
                #     present_left_time = 15.02 - present_present_time
                # elif present_present_time_in_minutes > 0 :
                #     present_left_time = 15.02 - present_present_time - 0.4
                # present_left_time_in_hours = int(present_left_time)
                # present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                # present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                if present_left_time_in_seconds >= 0 :
                    print_with_time('sleeping...')
                    time.sleep(present_left_time_in_seconds)
                else :
                    print_with_time('Time up, no time for sleep, none of the lectures ended early')
                n = 7
            elif present_time >= 15.02 and n != 0 and n!= 8:
                if n != 0:
                    close()
                print_with_time('Fourth lecture ended')
                print_with_time('All dlasses done for the day buddy!')
                n = 8
            
            elif present_time < 8.30:
                if present_time_in_minutes > 30:
                    time_left = 8.30 - present_time - 0.40
                else:
                    time_left = 8.30 - present_time
                time_left = round(time_left,2)
                time_left_in_hours = int(time_left)
                # print_with_time(present_time)
                # print_with_time(present_time_in_minutes)
                # print_with_time('Next lecture starts in...',present_left_time)
                time_left_in_minutes = int((time_left - int(time_left))*100)
                time_left_in_seconds =( (time_left_in_minutes * 60 + time_left_in_hours * 3600) + 60)
                print_with_time('The next class is in :',time_left)
                print_with_time('sleeping...')
                time.sleep(time_left_in_seconds)
            elif present_time > 15.02:
                if present_time_in_minutes != 0:
                    time_left = (24.00 - present_time - 0.40) 
                else:
                    time_left = (24.00 - present_time)   
                time_left = round(time_left,2)
                time_left_in_hours = int(time_left)
                time_left_in_minutes = int((time_left - int(time_left))*100)
                time_left_in_seconds =( (time_left_in_minutes * 60 + time_left_in_hours * 3600) + 60)
                print_with_time('The next day starts in :',time_left,'hrs')
                print_with_time(time_left_in_seconds)
                print_with_time('sleeping...')
                time.sleep(time_left_in_seconds)
                manual_time_table()

    # elif day.lower() == ""
    elif day.lower() == 'sat':
        print_with_time("Today is Saturday")
        n = 0
        while True:
            present_time = float(datetime.now().strftime("%H.%M"))
            present_time_in_minutes = int((present_time - int(present_time))*100)
            if present_time >= 08.30 and present_time < 09.32 and n!= 1 :
                print_with_time('First lecture started')

                logging.signing_in(sociology)
                
                print_with_time('We are in the first lecture')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 32 :
                    present_left_time = 9.32 - present_present_time
                elif present_present_time_in_minutes > 32 :
                    present_left_time = 9.32 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                # print_with_time('sleeping...')
                # time.sleep(present_left_time_in_seconds)
                # print_with_time("Checking...")
                # for_for_loop = (present_left_time_in_seconds/3)+1
                # for_for_loop = int(for_for_loop)
                # print_with_time("In loop for this many times:",for_for_loop)
                # for i in range(0, for_for_loop):
                #     time.sleep(3)
                #     just_start_recording_again = pyautogui.locateCenterOnScreen('if recording stops in between.png')
                #     recording_sign = pyautogui.locateCenterOnScreen('recording_sign.png')
                #     meeting_ended_1 = pyautogui.locateCenterOnScreen('meeting has been ended by the host.png')
                #     meeting_ended_2 = pyautogui.locateCenterOnScreen('meeting has been ended by the host2.png')
                #     meeting_ended_3 = pyautogui.locateCenterOnScreen('meeting has been ended by the host3.png')
                #     meeting_ended_4 = pyautogui.locateCenterOnScreen('meeting has been ended by the host4.png')
                #     join_button = pyautogui.locateCenterOnScreen('Join.png')
                #     if meeting_ended_1 != None or meeting_ended_2 != None or meeting_ended_3 != None or meeting_ended_4 != None or join_button != None :
                #         break
                #     if just_start_recording_again != None  or recording_sign == None:
                #         pyautogui.screenshot(r"C:\\Users\\NAMAN\\Videos\\Captures\\For Development Purposes\\screenshot1.png")
                        # pyautogui.hotkey('win','alt','r')
                # present_present_time = float(datetime.now().strftime("%H.%M"))
                # present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                # if present_present_time_in_minutes <= 32 :
                #     present_left_time = 9.32 - present_present_time
                # elif present_present_time_in_minutes > 32 :
                #     present_left_time = 9.32 - present_present_time - 0.4
                # present_left_time_in_hours = int(present_left_time)
                # present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                # present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                if present_left_time_in_seconds >= 0 :
                    print_with_time('sleeping...')
                    time.sleep(present_left_time_in_seconds)
                else :
                    print_with_time('Time up, no time for sleep, none of the lectures ended early')
                n = 1
            elif present_time >= 09.32 and present_time < 09.45 and n!= 2:    #just to be on the safe side 2mins extra
                if n != 0:
                    close()
                print_with_time('First lecture ended')                                
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 45 :
                    present_left_time = 9.45 - present_present_time
                elif present_present_time_in_minutes > 45 :
                    present_left_time = 9.45 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                print_with_time('Next lecture starts in...',present_left_time)
                print_with_time('sleeping...')
                time.sleep(present_left_time_in_seconds)
                n = 2

            elif present_time >= 09.45 and present_time < 10.47 and  n!= 3:
                print_with_time('Second lecture started')

                logging.signing_in(maths)
                
                print_with_time('We are in the second lecture')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 47 :
                    present_left_time = 10.47 - present_present_time
                elif present_present_time_in_minutes > 47 :
                    present_left_time = 10.47 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                # print_with_time('sleeping...')
                # time.sleep(present_left_time_in_seconds)
                # print_with_time("Checking...")
                # for_for_loop = (present_left_time_in_seconds/3)+1
                # for_for_loop = int(for_for_loop)
                # print_with_time("In loop for this many times:",for_for_loop)
                # for i in range(0, for_for_loop):
                #     time.sleep(3)
                #     just_start_recording_again = pyautogui.locateCenterOnScreen('if recording stops in between.png')
                #     recording_sign = pyautogui.locateCenterOnScreen('recording_sign.png')
                #     meeting_ended_1 = pyautogui.locateCenterOnScreen('meeting has been ended by the host.png')
                #     meeting_ended_2 = pyautogui.locateCenterOnScreen('meeting has been ended by the host2.png')
                #     meeting_ended_3 = pyautogui.locateCenterOnScreen('meeting has been ended by the host3.png')
                #     meeting_ended_4 = pyautogui.locateCenterOnScreen('meeting has been ended by the host4.png')
                #     join_button = pyautogui.locateCenterOnScreen('Join.png')
                #     if meeting_ended_1 != None or meeting_ended_2 != None or meeting_ended_3 != None or meeting_ended_4 != None or join_button != None :
                #         break
                #     if just_start_recording_again != None  or recording_sign == None:
                #         pyautogui.screenshot(r"C:\\Users\\NAMAN\\Videos\\Captures\\For Development Purposes\\screenshot2.png")
                        # pyautogui.hotkey('win','alt','r')
                # present_present_time = float(datetime.now().strftime("%H.%M"))
                # present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                # if present_present_time_in_minutes <= 47 :
                #     present_left_time = 10.47 - present_present_time
                # elif present_present_time_in_minutes > 47 :
                #     present_left_time = 10.47 - present_present_time - 0.4
                # present_left_time_in_hours = int(present_left_time)
                # present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                # present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                if present_left_time_in_seconds >= 0 :
                    print_with_time('sleeping...')
                    time.sleep(present_left_time_in_seconds)
                else :
                    print_with_time('Time up, no time for sleep, none of the lectures ended early')
                n = 3
            elif present_time >= 10.47 and present_time < 11.30  and n!= 4:
                if n != 0:
                    close()
                print_with_time('Second ecture Ended')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 30 :
                    present_left_time = 11.30 - present_present_time
                elif present_present_time_in_minutes > 30 :
                    present_left_time = 11.30 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                print_with_time('Next lecture starts in...',present_left_time)
                print_with_time('sleeping...')
                time.sleep(present_left_time_in_seconds)
                n = 4

            elif present_time >= 11.30 and present_time < 12.32 and n!= 5:
                print_with_time('Third lecture started')

                logging.signing_in(electrical_engineering_lab)
                
                print_with_time('We are in the third lecture')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 32 :
                    present_left_time = 12.32 - present_present_time
                elif present_present_time_in_minutes > 32 :
                    present_left_time = 12.32 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                # print_with_time('sleeping...')
                # time.sleep(present_left_time_in_seconds)
                # print_with_time("Checking...")
                # for_for_loop = (present_left_time_in_seconds/3)+1
                # for_for_loop = int(for_for_loop)
                # print_with_time("In loop for this many times:",for_for_loop)
                # for i in range(0, for_for_loop):
                #     time.sleep(3)
                #     just_start_recording_again = pyautogui.locateCenterOnScreen('if recording stops in between.png')
                #     recording_sign = pyautogui.locateCenterOnScreen('recording_sign.png')
                #     meeting_ended_1 = pyautogui.locateCenterOnScreen('meeting has been ended by the host.png')
                #     meeting_ended_2 = pyautogui.locateCenterOnScreen('meeting has been ended by the host2.png')
                #     meeting_ended_3 = pyautogui.locateCenterOnScreen('meeting has been ended by the host3.png')
                #     meeting_ended_4 = pyautogui.locateCenterOnScreen('meeting has been ended by the host4.png')
                #     join_button = pyautogui.locateCenterOnScreen('Join.png')
                #     if meeting_ended_1 != None or meeting_ended_2 != None or meeting_ended_3 != None or meeting_ended_4 != None or join_button != None :
                #         break
                #     if just_start_recording_again != None  or recording_sign == None:
                #         pyautogui.screenshot(r"C:\\Users\\NAMAN\\Videos\\Captures\\For Development Purposes\\screenshot3.png")
                        # pyautogui.hotkey('win','alt','r')
                # present_present_time = float(datetime.now().strftime("%H.%M"))
                # present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                # if present_present_time_in_minutes <= 32 :
                #     present_left_time = 12.32 - present_present_time
                # elif present_present_time_in_minutes > 32 :
                #     present_left_time = 12.32 - present_present_time - 0.4
                # present_left_time_in_hours = int(present_left_time)
                # present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                # present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                if present_left_time_in_seconds >= 0 :
                    print_with_time('sleeping...')
                    time.sleep(present_left_time_in_seconds)
                else :
                    print_with_time('Time up, no time for sleep, none of the lectures ended early')
                n = 5
            elif present_time >= 12.32 and present_time < 14.00 and n!= 6:
                if n != 0:
                    close()
                print_with_time('Third lecture ended')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 0 :
                    present_left_time = 14.00 - present_present_time
                elif present_present_time_in_minutes > 0 :
                    present_left_time = 14.00 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                print_with_time('Next lecture starts in...',present_left_time)
                print_with_time('sleeping...')
                time.sleep(present_left_time_in_seconds)
                n = 6

            elif present_time >= 14.00 and present_time < 15.02 and n!= 7:
                print_with_time('Fourth lecture started')

                logging.signing_in(chemistry)
                
                print_with_time('We are in the fourth lecture')
                present_present_time = float(datetime.now().strftime("%H.%M"))
                present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                if present_present_time_in_minutes <= 0 :
                    present_left_time = 15.02 - present_present_time
                elif present_present_time_in_minutes > 0 :
                    present_left_time = 15.02 - present_present_time - 0.4
                present_left_time_in_hours = int(present_left_time)
                present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                # print_with_time('sleeping...')
                # time.sleep(present_left_time_in_seconds)
                # print_with_time("Checking...")
                # for_for_loop = (present_left_time_in_seconds/3)+1
                # for_for_loop = int(for_for_loop)
                # print_with_time("In loop for this many times:",for_for_loop)
                # for i in range(0, for_for_loop):
                #     time.sleep(3)
                #     just_start_recording_again = pyautogui.locateCenterOnScreen('if recording stops in between.png')
                #     recording_sign = pyautogui.locateCenterOnScreen('recording_sign.png')
                #     meeting_ended_1 = pyautogui.locateCenterOnScreen('meeting has been ended by the host.png')
                #     meeting_ended_2 = pyautogui.locateCenterOnScreen('meeting has been ended by the host2.png')
                #     meeting_ended_3 = pyautogui.locateCenterOnScreen('meeting has been ended by the host3.png')
                #     meeting_ended_4 = pyautogui.locateCenterOnScreen('meeting has been ended by the host4.png')
                #     join_button = pyautogui.locateCenterOnScreen('Join.png')
                #     if meeting_ended_1 != None or meeting_ended_2 != None or meeting_ended_3 != None or meeting_ended_4 != None or join_button != None :
                #         break
                #     if just_start_recording_again != None  or recording_sign == None:
                #         pyautogui.screenshot(r"C:\\Users\\NAMAN\\Videos\\Captures\\For Development Purposes\\screenshot4.png")
                        # pyautogui.hotkey('win','alt','r')
                # present_present_time = float(datetime.now().strftime("%H.%M"))
                # present_present_time_in_minutes = int((present_present_time - int(present_present_time))*100)
                # if present_present_time_in_minutes <= 0 :
                #     present_left_time = 15.02 - present_present_time
                # elif present_present_time_in_minutes > 0 :
                #     present_left_time = 15.02 - present_present_time - 0.4
                # present_left_time_in_hours = int(present_left_time)
                # present_left_time_in_minutes = (present_left_time - present_left_time_in_hours)*100
                # present_left_time_in_seconds = ((present_left_time_in_minutes * 60 + present_left_time_in_hours * 3600)+60)
                if present_left_time_in_seconds >= 0 :
                    print_with_time('sleeping...')
                    time.sleep(present_left_time_in_seconds)
                else :
                    print_with_time('Time up, no time for sleep, none of the lectures ended early')
                n = 7
            elif present_time >= 15.02 and n != 0 and n!= 8:
                if n != 0:
                    close()
                print_with_time('Fourth lecture ended')
                print_with_time('All dlasses done for the day buddy!')
                n = 8
            
            elif present_time < 8.30:
                if present_time_in_minutes > 30:
                    time_left = 8.30 - present_time - 0.40
                else:
                    time_left = 8.30 - present_time
                time_left = round(time_left,2)
                time_left_in_hours = int(time_left)
                # print_with_time(present_time)
                # print_with_time(present_time_in_minutes)
                # print_with_time('Next lecture starts in...',present_left_time)
                time_left_in_minutes = int((time_left - int(time_left))*100)
                time_left_in_seconds =( (time_left_in_minutes * 60 + time_left_in_hours * 3600) + 60)
                print_with_time('The next class is in :',time_left)
                print_with_time('sleeping...')
                time.sleep(time_left_in_seconds)
            elif present_time > 15.02:
                if present_time_in_minutes != 0:
                    time_left = (24.00 - present_time - 0.40) 
                else:
                    time_left = (24.00 - present_time)   
                time_left = round(time_left,2)
                time_left_in_hours = int(time_left)
                time_left_in_minutes = int((time_left - int(time_left))*100)
                time_left_in_seconds =( (time_left_in_minutes * 60 + time_left_in_hours * 3600) + 60)
                print_with_time('The next day starts in :',time_left,'hrs')
                print_with_time(time_left_in_seconds)
                print_with_time('sleeping...')
                time.sleep(time_left_in_seconds)
                manual_time_table()


    elif day.lower() == 'sun':
        print_with_time("Today is Sunday")
            # n = 0
        present_time = float(datetime.now().strftime("%H.%M"))
        present_time_in_minutes = int((present_time - int(present_time))*100)
        if present_time_in_minutes != 0:
            time_left = (24.00 - present_time - 0.40) 
        else:
            time_left = (24.00 - present_time)   
        time_left = round(time_left,2)
        time_left_in_hours = int(time_left)
        time_left_in_minutes = int((time_left - int(time_left))*100)
        time_left_in_seconds =( (time_left_in_minutes * 60 + time_left_in_hours * 3600) + 60)
        print_with_time('The next day starts in :',time_left,'hrs')
        print_with_time(time_left_in_seconds)
        print_with_time('sleeping...')
        time.sleep(time_left_in_seconds)
        manual_time_table()    
    
    return


if __name__ == "__main__":
    
    # computer_on()
    # network_connection_check()
    manual_time_table()
    print_with_time("Today we got hundered percent attendence")
