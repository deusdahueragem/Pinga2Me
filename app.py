import PIL.Image, pystray, os, time
from datetime import datetime

clicks = []

green_icon = PIL.Image.open("./green_icon.png")
red_icon = PIL.Image.open("./red_icon.png")

def ping(ip):
    response = os.system("ping -n 1 " + ip + " >nul")
    return response

def on_clicked(icon, item):
    if str(item) == "Iniciar":
        pingar = True
        while(pingar == True):
            data_e_hora_atuais = datetime.now()
            data_e_hora_em_texto = data_e_hora_atuais.strftime(f'%d/%m/%Y %H:%M')
            if ping('192.168.8.198') == 0:
                print (data_e_hora_em_texto + ' - 192.168.8.198' + ' is up !')
                icon.icon = green_icon
                time.sleep(5)
            else:
                print (data_e_hora_em_texto + ' - 192.168.8.198' + ' is down !')
                icon.icon = red_icon
                time.sleep(5)
    elif str(item) == "Exit":
        icon.stop()

icon = pystray.Icon("Icone", green_icon, menu=pystray.Menu(
    pystray.MenuItem("Iniciar", on_clicked),
    pystray.MenuItem("Exit", on_clicked)
))

icon.run()