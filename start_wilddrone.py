import asyncio
from wilddrone import WildDrone
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
import utm

class GPS_Data(Node):
	utm=[]

	def __init__(self):
		super().__init__('GPS_DATA')
		self.subscription = self.create_subscription(Int32MultiArray, '/object_points/camera_10_11_0_3', self.gps_callback, 10)
	
	def gps_callback(self, msg):
		print(msg.data)
		self.utm=msg.data
	
	def LatLon(self):
		latlon = utm.to_latlon(self.utm[0], self.utm[1], 33, 'T')
		return latlon


def main():
	rclpy.init()
	gps=GPS_Data()
	while len(gps.utm) < 2:
		print("waiting")
		rclpy.spin_once(gps)
	
	coord=gps.LatLon() 
	print(coord)
	wd = WildDrone()
	asyncio.run(wd.goto_alarm(lat=coord[0], lon=coord[1], eps=0.1))
	
def main_fix_latlon():
	wd = WildDrone()
	asyncio.run(wd.goto_alarm(lat=47.6941333, lon=17.623650, eps=0.1))

def main_fix_utm():
	wd = WildDrone()
	latlon = utm.to_latlon(5283285, 698268, 33, 'T')
	asyncio.run(wd.goto_alarm(latlon[0], latlon[1], eps=0.1))

if __name__ == "__main__":
	main_fix_latlon()
	#main_fix_utm()
	#main()