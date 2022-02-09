import asyncio
from wilddrone import WildDrone
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

class GPS_Data(Node):
	gps=[]

	def __init__(self):
		super().__init__('GPS_DATA')
		self.subscription = self.create_subscription(Float32MultiArray, 'gps', self.gps_callback, 10)
	
	def gps_callback(self, msg):
		print(msg.data)
		self.gps=msg.data
	
	def LatLon(self):
		return self.gps


def main():
	rclpy.init()
	gps=GPS_Data()
	rclpy.spin_once(gps)
	coord=gps.LatLon()
	gps.destroy_node()
	rclpy.shutdown()
	
	wd = WildDrone("udp://:14540")
	asyncio.run(wd.goto_alarm(lat=coord[0], lon=coord[1], eps=0.1))

if __name__ == "__main__":
	main()

