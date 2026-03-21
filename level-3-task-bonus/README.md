# Bonus Task: ROS2 Rover Command Node

### Project Overview

This task involves extending the ROS2 communication project Level 3 Task with a decision making node.

### Files
  
* **[video.mp4](./video.mp4):** Screen recording showing 

* **[sensor_node.py](./sensor_node.py):** Source code for Sensor Node

    * Simulates a distance sensor by generating random integers between 1 and 100.

    * Publishes these values as String messages.

    * Uses a create_timer callback to publish message every 1 second.

* **[decision_node.py](./decision_node.py):** Source code for Decision Node

    * Subscribes to the /distance topic.

    * Uses a callback function to get incoming messages.

    * If distance < 30, publishes command STOP to topic /rover_command

    * If distance >= 30, publishes command MOVE_FORWARD to topic /rover_command

* **[command_listener.py](./command_listener.py):** Source code for Command Listener Node

    * Subscribes to the /rover_command topic.

    * Uses a callback function to get incoming messages.

    * Prints the received command to the terminal.

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
ros2 pkg create horizon_bonus_pkg --build-type ament_python --dependencies rclpy

# Create Nodes
cd horizon_bonus_pkg
# Paste the contents of source_code into this directory

# Build the packages
cd ~/ros2_ws
colcon build

# Run Sensor Node
ros2 run horizon_bonus_pkg sensor_node
# Run Decision Node (in second terminal instance)
ros2 run horizon_bonus_pkg decision_node
# Run Command Listener Node (in third terminal instance)
ros2 run horizon_bonus_pkg command_listener_node
```


