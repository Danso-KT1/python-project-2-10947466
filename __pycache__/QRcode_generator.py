import qrcode
import PySimpleGUI as sg
import os

layout=[    
        [sg.Text('Enter the Web address')],[sg.Input(size=[50,1 ], key='WEB_ADDRESS')],
        [sg.Text('select QR code color:')],
        [sg.Radio('black','color', default=True, key='color_black'),sg.Radio('yellow','color',key='color_yellow')],
        [sg.Text('select background color:')], [sg.Radio('white','BG_color',default=True,key='bg_color_white'),sg.Radio('green','BG_color',key='bg_color_green')],
    [sg.Button('Generate')],
    [sg.Image(key='-IMAGE-', size=(300,300))],
    [sg.Text('created by Danso Twum Kwadjo')]
]

window = sg.Window('QR Code Generator', layout)

def generate_qr_code(link):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black' if values['color_black'] else 'yellow',
                            back_color='white' if values['bg_color_white'] else 'green')

    file_name = 'qr_code' + '.png'
    path = os.path.join(os.getcwd(), file_name)
    img.save(path)
    return path

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Generate':
        web_address = values['WEB_ADDRESS']
        qr_code_image_path = generate_qr_code(web_address)
        window['-IMAGE-'].update(filename=qr_code_image_path)

window.close()
