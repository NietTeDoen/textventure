import time
import textgame

startup = float(0)
endlaunch = float(0)

async def startup():
    startup = time.time()
    print(f'starting up application...')
    endlaunch = time.time()
    print(f'it took {endlaunch - startup}ms to launch the application \n')
    txtgame = await textgame.textgame()
    

startup()