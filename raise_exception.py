class Accident (Exception):
    def __init__(self,msg):
        self.msg=msg
    def handle (self):
        print("accident occured. take detour")




try:
    raise Accident ('crash between two cars')
except Accident as e:
    e.handle()


             