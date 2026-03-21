#!usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class DecisionNode(Node):
    def __init__(self):
        super().__init__("decision_node")
        # Subscribe to topic /distance
        self.subscription = self.create_subscription(String, "distance", self.callback, 10)
        # Create publisher to topic /rover_command
        self.publisher = self.create_publisher(String, "rover_command", 10)


    def callback(self, msg):
        # Get the distance value from the message
        distance = int(msg.data)
        # Print the received distance value to terminal
        self.get_logger().info(f"Received Distance: {distance}")
        
        # If distance < 30, command is STOP, otherwise MOVE_FORWARD
        if distance < 30:
            command = "STOP"
        else:
            command = "MOVE_FORWARD"
        
        # Publish the command to topic /rover_command
        msg = String()
        msg.data = command
        self.publisher.publish(msg)
        # Print the published message to terminal
        self.get_logger().info(f"Publishing to /rover_command: {msg.data}")



def main(args=None):
    rclpy.init(args=args)
    node = DecisionNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
