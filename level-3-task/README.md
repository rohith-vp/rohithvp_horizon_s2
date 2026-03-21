# LEVEL 3 Task: ROS2

### Project Overview

This task involves setting up ROS2 Humble on Ubuntu 22.04 and create a ROS2 project that demonstrates communicaton between two nodes.

### Project Explanation

* Ubuntu 22.04 has been installed in a virtual machine using qemu+kvm on Fedora host.

* ROS2 setup with help from instructions in docs and reference videos

### Files
  
* **[video.mp4](./video.mp4):** Screen recording showing Ubuntu 22.04 installation, ROS2 setup and execution of project for communication between two nodes.

* **[publisher.py](./publisher.py):** Source code for Publisher Node

    * Simulates a distance sensor by generating random integers between 1 and 100.

    * Publishes these values as String messages.

    * Uses a create_timer callback to publish message every 1 second.

* **[subscriber.py](./subscriber.py):** Source code for Subscriber Node

    * Subscribes to the /distance topic.

    * Uses a callback function to get incoming messages.

    * Prints the received message to the terminal

### Execution Instructions

```bash
# Source ROS2 environment
source /opt/ros/humble/setup.bash
# Source Colcon
source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash

# Create and setup Workspace directory
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
colcon build
source ~/ros2_ws/install/setup.bash

# Create package
cd src
ros2 pkg create horizon_pkg --build-type ament_python --dependencies rclpy

# Create Nodes
cd horizon_pkg
# Paste the contents of source_code into this directory

# Build the packages
cd ~/ros2_ws
colcon build

# Run Publisher Node
ros2 run horizon_pkg publisher_node
# Run Subscriber Node (in seperate terminal instance)
ros2 run horizon_pkg subscriber_node
```


