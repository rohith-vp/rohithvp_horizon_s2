#!usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random


class SensorNode(Node):
    
    def __init__(self):
        super().__init__("sensor_node")
        # Create publisher to topic /distance with type String and buffer 10
        self.publisher = self.create_publisher(String, "distance", 10)
        # Timer runs every 1 second
        timer_period = 1
        self.timer = self.create_timer(timer_period, self.timer_callback)


    def timer_callback(self):
        msg = String()
        # Get random distance value
        distance = random.randint(1, 100)
        msg.data = f"{distance}"
        # Publish distance value to topic /distance
        self.publisher.publish(msg)
        # Print it to terminal
        self.get_logger().info(f"Publishing to /distance: {msg.data}")


def main(args=None):
    rclpy.init(args=args)
    node = SensorNode()
    rclpy.spin(node)
    rclpy.shutdown()


# Run main() function only if script is run directly
if __name__ == "__main__":
    main()
