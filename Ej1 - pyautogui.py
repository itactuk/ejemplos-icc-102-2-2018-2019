# La línea de abajo le da a python la capacidad de utilizar el mouse y el teclado
import pyautogui

# para más información sobre pyautogui ver http://automatetheboringstuff.com/chapter18/
# para escribir con el teclado usar pyautogui.typewrite("Hola escribe esto")

# mueve el mouse a la posición 49,179
pyautogui.moveTo(49,179, duration=0.25)
# el mouse da click en la posición que se encuentre. En este caso 49, 179
pyautogui.click()
pyautogui.moveTo(74,714, duration=0.25)
pyautogui.dragTo(524,719, duration=4)
pyautogui.moveTo(593,112, duration=0.25)
pyautogui.click()
pyautogui.moveTo(529,147, duration=0.25)
pyautogui.click()
pyautogui.moveTo(385,334, duration=0.25)
pyautogui.click()
pyautogui.moveTo(385,334, duration=0.25)
pyautogui.click()
# Usa el teclado para escribir "Repo Automático"
pyautogui.typewrite("Repo Automatico")
# Mueve el mouse a la posición 160, 558 y da clic
pyautogui.click(160,558)
pyautogui.moveTo(669,289, duration=0.25)
# Arrastra el teclado desde la posición actual hasta la posición 672, 446
pyautogui.dragTo(672,446, duration=4)
pyautogui.click(218,536)

# Las líneas de abajo son para mostrar la posición del cursor (x, y)
# No deben de ser incluídas en su programa final
while True:
    print(pyautogui.position())
