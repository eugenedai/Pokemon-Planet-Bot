
# # 
# import osddddddddadaada
# os.environ["DISPLAY"] = ":0"
# import pyautogui
# import timeaddadddaa

# count = 0

# import serial

# # Open the serial port
# ser = serial.Serial('/dev/ttyACM0', 9600)
# # 
# # Add a small delay to allow the user to prepare the screen
# # time.sleep(4)
# # 
# # Coordinates for primary monitor (left screen)

# # 
# # Capture secondary monitoraadadadddaaadaaaadadadaaad
# # 

# # 
# # 
# # adaa
# # # 
# # import pytesseract

# # # Use Tesseract to extract text from the screenshot
# # text = pytesseract.image_to_string(primary_screenshot)

# # # Print the extracted text
# # print("Extracted Text:")
# # print(text)

# # pyautogui.write()
# import random
# from pynput.keyboard import Key, Controller
# keyboard = Controller()

# while True:
#     for i in range(20):
#         num = random.randint(1,10)
#         if num <= 5:
#             keyboard.press('a')
#             num = random.uniform(0.2, 0.4)
#             time.sleep(num)
#             keyboard.release('a')
#             # num = random.uniform(0.05, 0.1)
#             # time.sleep(num)
#         else:
#             keyboard.press('d')
#             num = random.uniform(0.2, 0.4)
#             time.sleep(num)
#             keyboard.release('d')
#             # num = random.uniform(0.05, 0.1)
#             # time.sleep(num)
#     # # keyboard = Controller()
#     # keyboard.press('a')
#     # time.sleep(0.3)
#     # keyboard.release('a')
#     # time.sleep(0.05)
#     # # keyboard.press('w')
#     # # time.sleep(0.3)
#     # # keyboard.release('w')
#     # # time.sleep(0.05)
#     # keyboard.press('d')
#     # time.sleep(0.3)
#     # keyboard.release('d')
#     # time.sleep(0.05)
#     # # keyboard.press('s')
#     # # time.sleep(0.3)
#     # # keyboard.release('s')
#     # # time.sleep(0.05)
#     # keyboard.press('a')
#     # time.sleep(0.3)
#     # keyboard.release('a')
#     # time.sleep(0.05)
#     # # keyboard.press('w')
#     # # time.sleep(0.3)
#     # # keyboard.release('w')
#     # # time.sleep(0.05)
#     # keyboard.press('d')
#     # time.sleep(0.3)
#     # keyboard.release('d')
#     # time.sleep(0.05)
#     # # keyboard.press('s')
#     # # time.sleep(0.3)
#     # # keyboard.release('s')
#     # # time.sleep(0.05)
#     # # del keyboard

#     primary_screen = (1030, 700, 400, 60)
#     # 
#     # Coordinates for secondary monitor (right screen)
#     secondary_screen = (1920, 0, 2560, 1440)
#     # 
#     # Capture primary monitor
#     primary_screenshot = pyautogui.screenshot(region=primary_screen)
#     primary_screenshot.save("primary_screen.png")

#     import pytesseract

#     # Use Tesseract to extract text from the screenshot
#     text = pytesseract.image_to_string(primary_screenshot)

#     # Print the extracted textaadaaddd11adaaaaaad
#     print("Extracted Text:")
#     print(text)
#     with open("encounters.txt", 'a') as file:
#         file.write(text)
#     time.sleep(1)
#     listofmon = {"Sneasel", "Snorunt", "Shiny", "Snover", "Spheal", "Swinub", "Xerneas"}
#     listofkil = {"Beautifly", "Butterfree", "Fearow", "Pidgeot", "Maril", "Cryogonal", "Delibird", "Stantler", "Bergmite", "Cubchoo", "Dewgong", "Vanillite"}
#     # substring = "Pidgeot, Butterfree, Fearow, Beautifly, Maril, Cryogonal, Delibird, Stantler"    
#     # # Using index() to find the position
#     x = 1
#     mon = ''
#     print("hi")
#     for substring in listofmon:
#         # print(substring)
#         index = text.find(str(substring))
#         # print(str(index)+'\n')1
#         # index1 = text.find('shiny')
#         # index2 = text.find('elite')
#         # if index1 != -1 or index2 != -1:
#         #     x = 0
#         if index != -1:
#             mon = substring
#             x=0
#     print("bye")
#     if x ==0:
#         if mon == 'Abra':
#             keyboard.press('2')
#             keyboard.release('2')
#             num = random.uniform(0.3, 0.5)
#             time.sleep(num)
#             keyboard.press('3')
#             keyboard.release('3')
#         else:
#             ser.write(b"catch\n")
#             # print("high")
#         with open("encounters.txt", 'a') as file:
#             file.write(mon+'\n'+'\n')
#     else:
#         for substring in listofkil:
#             # print(substring)
#             index = text.find(str(substring))
#             # print(str(index)+'\n')1

#             if index != -1:
#                 with open("encounters.txt", 'a') as file:
#                     file.write(substring+'\n')
#         # print("kill")
#         keyboard.press('1')
#         keyboard.release('1')
#         num = random.uniform(0.3, 0.5)
#         print("cry")
#         time.sleep(num)
#         keyboard.press('1')
#         keyboard.release('1')
#         count +=1
#         print(count)
#     time.sleep(1.5)
# ser.close()






























import os
os.environ["DISPLAY"] = ":0"
import pyautogui
import time
from PIL import Image
import numpy as np
import serial
import random
from pynput.keyboard import Key, Controller
import datetime


def preserve_only_white_low(image):
    # Convert image to numpy array
    img_array = np.array(image)
    
    # Define white threshold with a lower value to catch more off-white pixels
    white_threshold = 30  # Lowered from 240 to catch more off-white dadddddddad
    
    # Find white pixels (where all RGB values are above threshold)
    white_mask = (img_array[:, :, 0] > white_threshold) & \
                 (img_array[:, :, 1] > white_threshold) & \
                 (img_array[:, :, 2] > white_threshold)
    
    # Create a copy of the array to modify
    modified_array = img_array.copy()
    
    # Set all non-white pixels to black while preserving original 
    modified_array[~white_mask, 0:3] = 0
    
    # Convert back to PIL Image
    return Image.fromarray(modified_array)


def preserve_only_white_high(image):
    # Convert image to numpy array
    img_array = np.array(image)
    
    # Define white threshold with a lower value to catch more off-white pixels
    white_threshold = 240  # Lowered from 240 to catch more off-white 3
    
    # Find white pixels (where all RGB values are above threshold)
    white_mask = (img_array[:, :, 0] > white_threshold) & \
                 (img_array[:, :, 1] > white_threshold) & \
                 (img_array[:, :, 2] > white_threshold)
    
    # Create a copy of the array to modify
    modified_array = img_array.copy()
    
    # Set all non-white pixels to black while preserving original alpha
    modified_array[~white_mask, 0:3] = 0
    
    # Convert back to PIL Image
    return Image.fromarray(modified_array)

keyboard = Controller()

# Open the serial port

count = 0  # Initialize count variable
count2 = 0
counttime = 0
place = 0
while True:
    if place==0:
        keyboard.press(Key.f8)
        keyboard.release(Key.f8)
        place = 1
    for i in range(15):
        num = random.randint(1,10)
        if num <= 5:
            keyboard.press('a')
            num = random.uniform(0.2, 0.4)
            time.sleep(num)
            keyboard.release('a')
            print('a')
            counttime +=1
            print(counttime)
        else:
            keyboard.press('d')
            num = random.uniform(0.2, 0.4)
            time.sleep(num)
            keyboard.release('d')
            print('d')
            counttime +=1
            print(counttime)
    # keyboard.press('4')
    # keyboard.release('4')aaaadaaddddadaaad
    # print('4')
    
    # using now() to get current timed3
    # current_time = datetime.datetime.now()
    # print(current_time.minute)ad
    # print(current_time.second)
    # print(current_time.minute*60+current_time.second)d3672
    print(counttime)
    if counttime >= 500:
        ser = serial.Serial('/dev/ttyACM0', 9600)
        keyboard.press(Key.f8)
        keyboard.release(Key.f8)
        place = 0
        primary_screen = (760, 760, 150, 20)
        # secondary_screen = (1920, 0, 2560, 1440)daaddad
        # Capture and process primary monitor
        primary_screenshot = pyautogui.screenshot(region=primary_screen)
        # Convert non-white to black before saving
        processed_screenshot = preserve_only_white_low(primary_screenshot)
        processed_screenshot.save("primary_screen.png")

        import pytesseract

        # Use Tesseract to extract text from the processed screenshot
        text = pytesseract.image_to_string(processed_screenshot)

        print("Extracted Text:\n" + text)
        with open("encounters.txt", 'a') as file:
            file.write(text)
        time.sleep(1)
        
        
        listofmon = {"Zapdos", "Cyndaquil", "Druddigon", "[S]"}
        listofkil = {"Voltorb", "Emolga", "Magnemite", "Pikachu"}
        
        x = 1
        mon = ''
        print("hi")
        for substring in listofmon:
            index = text.find(str(substring))
            if index != -1:
                mon = substring
                x=0
        print("bye")
        y = 0
        # for substring in listofmon:
        #     index = text.find(str(substring))
        #     if index != -1:
        #         y=1
        for substring in listofkil:
            index = text.find(str(substring))
            if index != -1:
                y=1
        # if y==0:
        #     count2+=1
        # if count2 == 5:
        #     break

        print("mon: " +mon)






        # primary_screen = (1030, 700, 400, 60)
        secondary_screen = (400, 730, 350, 45)
        
        # Capture and process primary monitor
        primary_screenshot = pyautogui.screenshot(region=secondary_screen)
        # Convert non-white to black before saving
        # processed_screenshot = preserve_only_white(secondary_screen)
        primary_screenshot.save("secondary_screen.png")
        import pytesseract
        text = ''
        # Use Tesseract to extract text from the processed screenshot
        text = pytesseract.image_to_string(primary_screenshot)

        print("Extracted Text:")
        print(text)
        with open("encounters.txt", 'a') as file:
            file.write(text)
        time.sleep(1)
        
        # listofmon = {"Pidgeot", "Sneasel", "Snorunt", "[S]", "Snover", "Spheal", "Swinub", "Xerneas"}aaadaaddaaaa
        # listofkil = {"Beautifly", "Butterfree", "Fearow", "Pidgeot", "Maril", "Cryogonal", "Delibird", "Stantler", "Bergmite", "Cubchoo", "Dewgong", "Vanillite"}
        
        # mon = ''
        print("hi")
        for substring in listofmon:
            index = text.find(str(substring))
            if index != -1:
                mon = substring
                x=0
        print("bye")
        # for substring in listofmon:
        #     index = text.find(str(substring))
        #     if index != -1:
        #         y=1
        for substring in listofkil:
            index = text.find(str(substring))
            if index != -1:
                y=1
        # if y==0:
        #     count2+=1
        # if count2 == 5:
        #     break

        print("mon: " +mon)


        if x == 0:
            if mon == 'Xerneas':
                ser.write(b"catch\n")
                break
            else:
                w = 1
                while w == 1:
                    print('\n\n\n\n\n')
                    ser.write(b"catch\n")
                    keyboard.press('3')
                    keyboard.release('3')
                    print('3')
                    num = random.uniform(0.2, 0.4)
                    time.sleep(num)
                    keyboard.press('6')
                    keyboard.release('6')
                    print('6')
                    num = random.uniform(0.2, 0.4)
                    time.sleep(num)
                    keyboard.press('7')
                    keyboard.release('7')
                    print('7')
                    num = random.uniform(0.2, 0.4)
                    time.sleep(num)
                    keyboard.press('2')
                    keyboard.release('2')
                    print('2')
                    num = random.uniform(0.2, 0.4)
                    time.sleep(num)
                    keyboard.press('3')
                    keyboard.release('3')
                    print('3')
                    num = random.uniform(0.2, 0.4)
                    time.sleep(num)


                    with open("encounters.txt", 'a') as file:
                        file.write(mon+'\n'+'\n')

                    z1 = 0
                    z2 = 0
                    z3 = 0
                    print(mon)
                    # Capture and process primary monitor
                    primary_screenshot = pyautogui.screenshot(region=primary_screen)
                    # Convert non-white to black before saving
                    processed_screenshot = preserve_only_white_low(primary_screenshot)
                    processed_screenshot.save("primary_screen.png")
                    # Use Tesseract to extract text from the processed screenshot
                    text = pytesseract.image_to_string(processed_screenshot)
                    print("Extracted Text:")
                    print(text)

                    index = text.find(str(mon))
                    if index != -1:
                        z1=0
                    else:
                        z1=1
                    text = ''
                    # Capture and process primary monitor
                    primary_screenshot = pyautogui.screenshot(region=secondary_screen)
                    # Convert non-white to black before saving
                    # processed_screenshot = preserve_only_white(secondary_screen)
                    primary_screenshot.save("secondary_screen.png")
                    # import pytesseract
                    # Use Tesseract to extract text from the processed screenshot
                    text = pytesseract.image_to_string(primary_screenshot)

                    
                    print("Extracted Text:")
                    print(text)
                    print(mon)

                    index = text.find(str(mon))
                    if index != -1:
                        z2=0
                    else:
                        z2=1
                    

                    # Capture and process primary monitor
                    primary_screenshot = pyautogui.screenshot(region=primary_screen)
                    # Convert non-white to black before saving
                    processed_screenshot = preserve_only_white_high(primary_screenshot)
                    # processed_screenshot.save("primary_screen.png")
                    # Use Tesseract to extract text from the processed screenshot
                    text = pytesseract.image_to_string(processed_screenshot)
                    print("Extracted Text:")
                    print(text)

                    index = text.find(str(mon))
                    if index != -1:
                        z3=0
                    else:
                        z3=1


                    print('z1: '+ str(z1) + '\nz2: ' + str(z2)+'\nz3: ' + str(z3))
                    if z1 == 1 and z2 == 1 and z3 ==1:
                        w = 0
                    else:
                        w = 1
        elif y== 1:
            for substring in listofkil:
                index = text.find(str(substring))
                if index != -1:
                    with open("encounters.txt", 'a') as file:
                        file.write(substring+'\n')
            keyboard.press('4')
            keyboard.release('4')
            count += 1
            print(count)
            count2 == 0
        time.sleep(1.5)
        counttime = 0
        ser.close()


