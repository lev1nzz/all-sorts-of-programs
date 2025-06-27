import os
from segno import helpers

username = os.getlogin()
desktop = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")
save_path = os.path.join(desktop, "qr_WiFi.png")  # => "C:/Users/user/Desktop/my_qr.png"


Name = input('Enter Name WI-Fi:') 
Passw = input('Enter a Password:')
secu = input('Enter type Securiti (WPA/WPA2):')


qcode = helpers.make_wifi(Name, password= Passw, security= secu,)
qcode.save(save_path, dark="#7D29B9", border=8, scale=15)

# ## Параметры:
# # ssid -  SSID сети
# # password -  пароль
# # security -  тип аутентификации ("WEP" или "WPA").
# # hidden -  является ли сеть скрытой