#!usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random


class PublisherNode(Node):
    
    def __init__(self):
        super().__init__("publisher_node")
        self.publisher = self.create_publisher(String, "distance", 10)
        timer_period = 1
        self.timer = self.create_timer(timer_period, self.timer_callback)


    def timer_callback(self):
        msg = String()
        distance = random.randint(1, 100)
        msg.data = f"{distance}"
        self.publisher.publish(msg)
        self.get_logger().info(f"Publishing: {msg.data}")


def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
