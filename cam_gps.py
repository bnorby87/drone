import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray


class GPS(Node):
	utm_x=0.0
	utm_y=0.0

	def __init__(self, utm_x, utm_y):
		super().__init__('gps')
		self.utm_x=utm_x
		self.utm_y=utm_y
		self.publisher_ = self.create_publisher(Int32MultiArray, '/object_points/camera_10_11_0_3', 10)
		timer_period = 0.5
		self.timer = self.create_timer(timer_period, self.gps_callback)

	def gps_callback(self):
		msg = Int32MultiArray()
		msg.data = [self.utm_x, self.utm_y]
		self.publisher_.publish(msg)
		self.get_logger().info('Publishing: "%s"' % msg.data)


def main():
	rclpy.init()
	gps=GPS(utm_x=698249, utm_y=5283294)
	rclpy.spin(gps)
	gps.destroy_node()
	rclpy.shutdown()


if __name__ == '__main__':
	main()

