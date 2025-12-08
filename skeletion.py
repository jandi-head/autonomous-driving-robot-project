import threading
from time import sleep

# 대충 핀 설정
zoneID = {'IDLE' : 0, 'CHILD' : 1, 'HIGHACCIDENT' : 2, 'SPEEDBUMP' : 3}
current_zone = 0
Child_pwm = 30 # 어린이 보호구역 목표 속도
HighAccident_pwm = 50 # 사고다발지역 목표 속도
SpeedBump_pwm = 20 # 과속 방지턱 목표 속도

stop_event = threading.Event()

def getCurZoneTask(stop_flag: threading.Event, 추가로 인자들):
    while not stop_flag.is_set():
        zoneInfo = getCurZone(인자)
        sleep(0.1)

def getObjInfoTask(stop_flag: threading.Event, 추가로 인자들):
    while not stop_flag.is_set():
        isObjDetected, isObjInRoad = getObjInfo(인자)
        sleep(0.1)

# 이게 메인 로직
def mainTask(stop_flag: threading.Event, ZoneInfo, isObjDetected, isObjInRoad):
    while not stop_flag.is_set():
         if isObjDetected == 1 and isObjInRoad == 1:
            current_pwm = 0
         elif ZoneInfo == zoneID['IDLE']:
            continue
         elif ZoneInfo == zoneID['CHILD']:
            current_pwm = Child_pwm
         elif ZoneInfo == zoneID['HIGHACCIDENT']:
            current_pwm = HighAccident_pwm
         elif ZoneInfo == zoneID['SPEEDBUMP']:
            while SpeedBump_pwm > current_pwm:
               current_pwm -= 2
            if current_pwm < SpeedBump_pwm:
               current_pwm == SpeedBump_pwm    
               
               sleep(0.1)
    
         sleep(0.1)

def getCurZone(인자):
    # 여기 짜면 돼
    zoneInfo = 0
    return zoneInfo

def getObjDetected(인자):
    # 여기 짜면 돼
    isObjDetected = 0
    return isObjDetected

def getObjInRoad(인자):
    # 여기 짜면 돼
    isObjInRoad = 0
    return isObjInRoad

def getObjInfo(인자):
    # 여기 짜면 돼
    
    # 센서퓨전
    isObjDetected = getObjDetected(인자)
    isObjInRoad = getObjInRoad(인자)
    return isObjDetected, isObjInRoad


if __name__ == "__main__":
    
    curZoneTaskThread = threading.Thread(인자들)
    
    objInfoTaskThread = threading.Thread(인자들)
    
    mainTaskThread = threading.Thread(인자들)
    
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