import pyautogui
#Looking Busy
#nudge your mouse cursor slightly every ten seconds
def looking_busy():
    try:
        while True:
            print('moving')
            pyautogui.moveRel(1,0)
            pyautogui.PAUSE = 3
    except:
        print('mouse moved to top left of the screen, quit moving mouse')
if __name__ == "__main__":
    # looking_busy()
    # Instant Messenger_Bot()
    # game_playing_bot()