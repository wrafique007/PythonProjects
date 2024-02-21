import PySimpleGUI as sg
import time

sg.theme = 'blue'

label = sg.Text('Todo Desktop Application',key='label')
clock = sg.Text('',key='clock')
col1 = sg.InputText("Tell me something and then press button on right", key='Input', tooltip="Enter something")
col2=sg.Listbox(values=["Prepare for Turing Test","Apply for a new drivign license","Get Apache Spark certification","Do Machine Learning exercises"],key='lb', enable_events=True, size=[45,10])
button = sg.Button(size=2, image_source='./add.png',mouseover_colors='lightblue',tooltip='click it', key='button')
display_text = sg.Text('',key='displaytext')
column = sg.Column([[col1,button,col2]])

layout = [[label,clock],
          [column],
          [display_text]]

window = sg.Window('I am window', layout=layout, font=('Helvetica',20))


while True:

    events,values = window.read(timeout=200)
    window['clock'].update(value=time.strftime('"%m/%d/%Y, %H:%M:%S"'))
    print(events)
    print(values)
    match events:
        case sg.WIN_CLOSED:
            break
        case 'Input':
            sg.popup(f'An Input event has taken place')
        case 'lb':
            sg.popup(f'A listbox event has taken place')
        case 'button':
            sg.popup(f'button has been pressed')
            window['displaytext'].update(value=values['Input'])

window.close()
        