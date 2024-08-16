import pyautogui
import time

resposta = input("Deseja rodar o script? (S/N): ").strip().upper()

if resposta == 'S':
    print('Rodando ...')

    while True:

        time.sleep(2)
        pyautogui.hotkey('win', 's')
        time.sleep(2)

        pyautogui.hotkey('win', 'r')
        time.sleep(1)

        pyautogui.write('chrome.exe')
        pyautogui.press('enter')

        time.sleep(5)

        pyautogui.hotkey('alt', 'f4')
        time.sleep(3)
else:
    print("Programa fechado.")
