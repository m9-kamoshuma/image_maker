import PySimpleGUI as sg

def name():
    #　レイアウト（1段目：テキスト、２段目：テキスト、３段目：テキスト出力欄、４段目：テキスト入力欄、５段目：ボタン、ボタン、ボタン）
    layout = [[sg.Text('下の入力欄に保存時の写真名を入力してください')],
              [sg.Text('入力欄'),sg.In(key='-NAME-')],
              [sg.Text('下の入力欄に構成写真のサイズを入力してください')],
              [sg.Text('高さ'),sg.In(key='-HEIGHT-')],
              [sg.Text('横幅'),sg.In(key='-WIDTH-')],
              [sg.Text('下の入力欄に構成写真の縦と横の枚数を入力してください')],
              [sg.Text('縦の枚数'),sg.In(key='-NUM_H-')],
              [sg.Text('横の枚数'),sg.In(key='-NUM_W-')],
              [sg.Button('決定'), sg.Button('クリア')]  ]

    window = sg.Window('設定', layout)

    while True:

        #　ユーザからの入力を待ちます。入力があると、次の処理に進みます。
        event, value = window.read()
        
        if event in (sg.WIN_CLOSED, '決定'):
            break
        #　「Clear」ボタンを押したときの処理
        if event == 'クリア':
            #　「-OUTPUT-」領域を、空白で更新します。
            window['-OUTPUT-'].update('')
            
    window.close()
    return value['-NAME-'], value['-HEIGHT-'] , value['-WIDTH-'], value['-NUM_H-'], value['-NUM_W-'] 