#Prettified Stopwatch
import time, pyperclip

def pretty_stopwatch():
    print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. " \
        Press Ctrl-C to quit.')
    input()                    # press Enter to begin
    print('Started.')
    startTime = time.time()    # get the first lap's start time
    lastTime = startTime
    lapNum = 1

    try:
        while True:
            input()
            lapTime = round(time.time() - lastTime, 2)
            totalTime = round(time.time() - startTime, 2)
            print(f'Lap # {str(lapNum).rjust(3)}: {str(totalTime).ljust(4)} ({str(lapTime).ljust(4)})')   #prettifed with left and right just
            pyperclip.copy(f'Lap # {str(lapNum).rjust(3)}: {str(totalTime).rjust(16)} ({str(lapTime).rjust(6)})') # automatically copy to user clipboard
            # print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
            lapNum += 1
            lastTime = time.time() # reset the last lap time

    except KeyboardInterrupt:
        # Handle the Ctrl-C exception to keep its error message from displaying.
        print('\nDone.')

if __name__ == "__main__":
    pretty_stopwatch()