# Exercise 9 - Shoutouts to Everyone | Python Tutorial - Day #83

# https://www.youtube.com/watch?v=1WjwnlRXfHc&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=83


import os

def speak(x):
    command = f'''PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}');"'''
    os.system(command)

lst = ['Rahul','Nishant', 'Harry', 'Kunal', 'Yash', 'Nisha']

for i in lst:
    speak(f'Shoutout to {i}')
    # print(i)

# speak(f'Shoutout to {list[0]}')
# speak(f'Shoutout to {list[1]}')
# speak(f'Shoutout to {list[2]}')
# speak(f'Shoutout to {list[3]}')