import PySimpleGUI as sg

def end():
    #　レイアウト（1段目：テキスト、２段目：テキスト、３段目：テキスト出力欄、４段目：テキスト入力欄、５段目：ボタン、ボタン、ボタン）
    layout = [[sg.Text('完了しました！')],[sg.Button('終了')] ]

    window = sg.Window('完了', layout)
    
    while True:
        event, value = window.read()
        
        if event == '終了':
            break
        