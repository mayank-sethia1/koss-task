import time
import threading
from collections.abc import Mapping

class mayhem(threading.Thread):
    def __init__(self,map: Mapping[str,int]):
        super().__init__()
        self.map=map
    def run(self):
        for key,value in self.map.items():
            time.sleep(value)
d = {"k1":11,"k2":2,"k3":3}
m= mayhem(d)
m.start()
d["k4"]=4