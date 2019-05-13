
import time, pyperclip
import requests, bs4, os, datetime, re


#Prettified Stopwatch
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

def Scheduled_Web_Comic_Downloader():
    #Assume task schedule will run this program on a daily basis
    #check if website has new comic
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    res = requests.get('https://www.buttersafe.com/', headers=headers)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    dateElement = soup.select('#headernav-date')
    latestReleaseDate_str = dateElement[0].text.strip() #string
    #regex to take needed element
    dateRegex = r'.* (\w*) (\d+).*, (\d{4})'
    m = re.search(dateRegex, latestReleaseDate_str)
    #turn month string into integer
    latestReleaseDate = datetime.datetime.strptime(m.group(3)+m.group(1)+m.group(2), '%Y%b%d')

    if datetime.datetime.now() != latestReleaseDate:
        print('still the same old comic today :(')
        pass #do nothing if latest comic release date isn't today
    else:
        print('There is new comic today :)')
        #scrap image to folder
        os.makedirs('buttersafe_comic', exist_ok=True)
        picElement = soup.select('#comic img')
        picUrl = picElement[0].get('src')
        res = requests.get(picUrl, headers=headers)
        res.raise_for_status()

        with open(os.path.join('buttersafe_comic',os.path.basename(picUrl)), 'wb') as imageFile:
            print(f'downloading {picUrl}')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
 
if __name__ == "__main__":
    # pretty_stopwatch()
    # Scheduled_Web_Comic_Downloader()