'''
자료형 bool
isObjDetected
isObjInRoad
'''

import threading
from time import sleep

# 대충 핀 설정

stop_event = threading.Event()

def getCurZoneTask(stop_flag: threading.Event, image):
    while not stop_flag.is_set():
        zoneInfo = getCurZone(image)
        sleep(0.1)

def getObjInfoTask(stop_flag: threading.Event, distUS, image):
    while not stop_flag.is_set():
        isObjDetected, isObjInRoad = getObjInfo(distUS, image)
        sleep(0.1)

# 이게 메인 로직
def mainTask(stop_flag: threading.Event,ZoneInfo, isObjDetected, isObjInRoad):
    while not stop_flag.is_set():
        # 여기에 짜면 돼
        sleep(0.1)
    limVel = 20.0 # [-100 100]   
    return limVel
def getCurZone(image):
    # 여기 짜면 돼
    zoneInfo = 0
    return zoneInfo

def getObjDetected(image):
    # 여기 짜면 돼
    isObjDetected = True
    return isObjDetected

def getObjInRoad(image):
    # 여기 짜면 돼
    isObjInRoad = True
    return isObjInRoad

def getObjInfo(image):
    # 여기 짜면 돼
    
    # 센서퓨전
    isObjDetected = getObjDetected(image)
    isObjInRoad = getObjInRoad(image)
    return isObjDetected, isObjInRoad


if __name__ == "__main__":
    
    curZoneTaskThread = threading.Thread(target=getCurZoneTask, args=(stop_event,),
 name="curZoneTaskThread")
    
    objInfoTaskThread = threading.Thread(target=getObjInfoTask, args=(stop_event,),
 name="ObjInfoTaskThread")

    mainTaskThread = threading.Thread(target=mainTask, args=(stop_event,),
 name="mainTaskThread")
    
    curZoneTaskThread.start()
    objInfoTaskThread.start()
    mainTaskThread.start()
    
    try:
        while True:
            sleep(1.0)
    
    finally:
        stop_event.set()
        curZoneTaskThread.join(timeout=1.0)
        ObjInfoTaskThread.join(timeout=1.0)
        mainTaskThread.join(timeout=1.0)
        print("Stopped.")