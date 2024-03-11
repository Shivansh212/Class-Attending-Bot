
import subprocess
import pyautogui
import time
from subprocess import Popen
from datetime import datetime
import requests

url="https://discord.com/api/webhooks/933789982466928740/1gb-KPcUyjDubgDKTvpLKvxRHNfqj9cwbcGjew4fRqFrJEBZAlIwOA5XeDIa9YpzuWyO"

itClass_ls=["07:20","08:00"]
chemClass_ls=["08:00","08:40"]
engClass_ls=["14:00","14:40"]
itClass=False
chemClass=False
engClass=False
while itClass is False:
    nowtime=str(datetime.now().strftime("%H:%M"))
    if str(nowtime) == itClass_ls[0]:
        
        r = requests.post(url, data={"content":"---------------Starting IT Class---------------------"})
        subprocess.Popen("C:\Program Files\Google\Chrome\Application\chrome.exe")
        time.sleep(2)

        r = requests.post(url, data={"content":"Open Chrome"})


        mitra_start=pyautogui.locateCenterOnScreen("C:/Users/Aaroegun/Desktop/Class Attending Bot/Mitra_start.png")
        pyautogui.moveTo(mitra_start)
        pyautogui.click()
        time.sleep(1)

        r = requests.post(url, data={"content":"Open School Mitra"})


        attend=pyautogui.locateCenterOnScreen("C:/Users/Aaroegun/Desktop/Class Attending Bot/Computer Science class.png")
        x=attend[0]+200
        y=attend[1]
        pyautogui.moveTo(x,y)
        pyautogui.click()
        time.sleep(1)

        r = requests.post(url, data={"content":"Opne IT Class"})

        chrome_close = pyautogui.locateCenterOnScreen("C:/Users/Aaroegun/Desktop/Class Attending Bot/close_button.png")
        pyautogui.moveTo(chrome_close)
        pyautogui.click()

        r = requests.post(url, data={"content":"Chrome Close"})



        joinit=False
        while joinit is False:
            
            
            try:
                join_with=pyautogui.locateCenterOnScreen("C:/Users/Aaroegun/Desktop/Class Attending Bot/join with.png")
                pyautogui.moveTo(join_with)
                pyautogui.click()
                joinit=True

                r = requests.post(url, data={"content":"IT Class Joined"})
            
            
            except:
                joinit=False
                time.sleep(45)
        
        quitit=False
        
        while quitit is False:
            quit_time = datetime.now().strftime("%h:%M")
            if quit_time == itClass_ls[1]:
                
                
                try:
                    quit_button = pyautogui.locateCenterOnScreen("C:/Users/Aaroegun/Desktop/Class Attending Bot/zoom close.png")
                    pyautogui.moveTo(quit_button)
                    pyautogui.click()

                    leave_mett = pyautogui.locateCenterOnScreen("C:/Users/Aaroegun/Desktop/Class Attending Bot/leave meet.png")
                    pyautogui.moveTo(leave_mett)
                    pyautogui.click()
                    quitit = True

                    r = requests.post(url, data={"content":"IT Class Quit"})


                except:
                    quitit = False
        
        
        itClass = True

        r = requests.post(url, data={"content":"-------------------IT Class Completed----------------------"})


while chemClass is False:
    nowtime=str(datetime.now().strftime("%H:%M"))
    
    if str(nowtime) == chemClass_ls[0]:
        
        r = requests.post(url, data={"content":"------------Chemistry Class-------------"})


        subprocess.Popen("C:\Program Files\Google\Chrome\Application\chrome.exe")
        time.sleep(2)

        r = requests.post(url, data={"content":"Open Chrome"})

        
        mitra_start=pyautogui.locateCenterOnScreen("C:/Users/Aaroegun/Desktop/Class Attending Bot/Mitra_start.png")
        pyautogui.moveTo(mitra_start)
        pyautogui.click()
        time.sleep(1)

        r = requests.post(url, data={"content":"Open School Mitra"})

        
        attend=pyautogui.locateCenterOnScreen("C:/Users/Aaroegun/Desktop/Class Attending Bot/Chemistry Science class.png")
        x=attend[0]+200
        y=attend[1]
        pyautogui.moveTo(x,y)
        pyautogui.click()

        r = requests.post(url, data={"content":"Opne Chemistry Class"})

        chrome_close = pyautogui.locateCenterOnScreen("C:/Users/Aaroegun/Desktop/Class Attending Bot/close_button.png")
        pyautogui.moveTo(chrome_close)
        pyautogui.click()

        r = requests.post(url, data={"content":"Chrome Close"})


        joinche=False
        while joinche is False:
            
            
            try:
                join_with=pyautogui.locateCenterOnScreen("C:/Users/Aaroegun/Desktop/Class Attending Bot/join with.png")
                pyautogui.moveTo(join_with)
                pyautogui.click()
                joinche=True

                r = requests.post(url, data={"content":"Chemistry Class Joined"})
            
            
            except:
                joinche=False
                time.sleep(45)
        
        quitche=False
        
        while quitche is False:
            quit_time = datetime.now().strftime("%h:%M")
            
            if quit_time == chemClass_ls[1]:
                
                
                try:
                    quit_button = pyautogui.locateCenterOnScreen("C:/Users/Aaroegun/Desktop/Class Attending Bot/zoom close.png")
                    pyautogui.moveTo(quit_button)
                    pyautogui.click()

                    leave_mett = pyautogui.locateCenterOnScreen("C:/Users/Aaroegun/Desktop/Class Attending Bot/leave meet.png")
                    pyautogui.moveTo(leave_mett)
                    pyautogui.click()
                    quitche = True

                    r = requests.post(url, data={"content":"Chemistry Class Quit"})
                
                
                except:
                    quitche = False

        chemClass = True
        r = requests.post(url, data={"content":"-------------------Chemistry Class Completed----------------------"})





while engClass is False:
    nowtime=str(datetime.now().strftime("%H:%M"))
    if str(nowtime) == engClass_ls[0]:
        
        r = requests.post(url, data={"content":"---------------Starting English Class---------------------"})
        subprocess.Popen("C:\Program Files\Google\Chrome\Application\chrome.exe")
        time.sleep(2)

        r = requests.post(url, data={"content":"Open Chrome"})


        mitra_start=pyautogui.locateCenterOnScreen("C:/Users/Aaroegun/Desktop/Class Attending Bot/Mitra_start.png")
        pyautogui.moveTo(mitra_start)
        pyautogui.click()
        time.sleep(1)

        r = requests.post(url, data={"content":"Open School Mitra"})


        attend=pyautogui.locateCenterOnScreen("C:/Users/Aaroegun/Desktop/Class Attending Bot/English class.png")
        x=attend[0]+200
        y=attend[1]-20
        pyautogui.moveTo(x,y)
        pyautogui.click()
        time.sleep(1)

        r = requests.post(url, data={"content":"Opne IT Class"})

        chrome_close = pyautogui.locateCenterOnScreen("C:/Users/Aaroegun/Desktop/Class Attending Bot/close_button.png")
        pyautogui.moveTo(chrome_close)
        pyautogui.click()

        r = requests.post(url, data={"content":"Chrome Close"})



        joineng=False
        while joineng is False:
            
            
            try:
                join_with=pyautogui.locateCenterOnScreen("C:/Users/Aaroegun/Desktop/Class Attending Bot/join with.png")
                pyautogui.moveTo(join_with)
                pyautogui.click()
                joineng=True

                r = requests.post(url, data={"content":"English Class Joined"})
            
            
            except:
                joineng=False
                time.sleep(45)
        
        quiteng=False
        
        while quiteng is False:
            quit_time = datetime.now().strftime("%h:%M")
            if quit_time == itClass_ls[1]:
                
                
                try:
                    quit_button = pyautogui.locateCenterOnScreen("C:/Users/Aaroegun/Desktop/Class Attending Bot/zoom close.png")
                    pyautogui.moveTo(quit_button)
                    pyautogui.click()

                    leave_mett = pyautogui.locateCenterOnScreen("C:/Users/Aaroegun/Desktop/Class Attending Bot/leave meet.png")
                    pyautogui.moveTo(leave_mett)
                    pyautogui.click()
                    quiteng = True

                    r = requests.post(url, data={"content":"English Class Quit"})


                except:
                    quiteng = False
        
        
        engClass = True

        r = requests.post(url, data={"content":"-------------------English Class Completed----------------------"})



    
        

