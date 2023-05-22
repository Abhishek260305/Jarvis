from pywinauto.application import Application

app=Application(backend='uia').start("whatsapp.exe").connect(title = 'WhatsApp',timeout=20)
app.WhatsApp.print_control_identifiers()