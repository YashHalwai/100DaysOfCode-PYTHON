# Exercise 9: Solution - Shoutouts to Everyone | Python Tutorial - Day #88

# https://www.youtube.com/watch?v=C9VP-56RXNM&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=88



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