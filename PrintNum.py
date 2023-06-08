import PySimpleGUI as sg
from Judge import judge

def printNum(sepa,unit):
    layout = [[sg.Text('のこり')],
        [sg.Text(size=(8, 1), font=('Helvetica', 20),justification='center', key='-RATE-')],
        [sg.Text('%です')]]
    window = sg.Window('完了までの時間', layout)
    
    length=len(sepa)
    Numlist=[0]*length
    for i in range(length):
        event,values = window.read(timeout=10,timeout_key='-timeout-')
        Numlist[i]=judge(sepa[i],unit)
        rate = str(int(100-i/length*100))
        window['-RATE-'].update(rate)
  
    window.close()
    return Numlist