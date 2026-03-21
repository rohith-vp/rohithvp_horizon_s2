#!usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class CommandListenerNode(Node):
    def __init__(self):
        super().__init__("command_listener_node")
        # Subscribe to topic /rover_command
        self.subscription = self.create_subscription(String, "rover_command", self.callback, 10)


    def callback(self, msg):
        # Print the received command to terminal
        self.get_logger().info(f"Received Command: {msg.data}")



def main(args=None):
    rclpy.init(args=args)
    node = CommandListenerNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
