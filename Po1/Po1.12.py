import pyautogui


def llenar_form_fb(nombre,apellido, correo, contrasena):
    pyautogui.click(231,342) #posicion nombre
    pyautogui.typewrite(nombre)
    pyautogui.click(231,342) #posicion apellido
    pyautogui.typewrite(apellido)
    pyautogui.click(231,342) #posicion correo
    pyautogui.typewrite(correo)
    pyautogui.click(231,342) #posicion nombre
    pyautogui.typewrite(nombre)
    pyautogui.click(231,342) #dar clic en enviar


llenar_form_fb(nombre="",apellido="",correo="",contrasena="")
