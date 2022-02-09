import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray


class GPS(Node):
	lat=0.0
	lon=0.0

	def __init__(self, lat, lon):
		super().__init__('gps')
		self.lat=lat
		self.lon=lon
		self.publisher_ = self.create_publisher(Float32MultiArray, 'gps', 10)
		timer_period = 0.5
		self.timer = self.create_timer(timer_period, self.gps_callback)

	def gps_callback(self):
		msg = Float32MultiArray()
		msg.data = [self.lat, self.lon]
		self.publisher_.publish(msg)
		self.get_logger().info('Publishing: "%s"' % msg.data)


def main():
	rclpy.init()
	gps=GPS(lat=47.397, lon=8.5449)
	rclpy.spin(gps)
	gps.destroy_node()
	rclpy.shutdown()


if __name__ == '__main__':
	main()

