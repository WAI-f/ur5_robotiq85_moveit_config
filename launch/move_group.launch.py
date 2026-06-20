import os
import sys

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from moveit_configs_utils.launches import generate_move_group_launch

sys.path.append(os.path.dirname(__file__))
from moveit_config_builder import build_moveit_config


def _hardware_launch_arguments():
    return [
        DeclareLaunchArgument("ros2_control_hardware_type", default_value="mock"),
        DeclareLaunchArgument("joint_commands_topic", default_value="/isaac_joint_commands"),
        DeclareLaunchArgument("joint_states_topic", default_value="/isaac_joint_states"),
    ]


def generate_launch_description():
    moveit_config = build_moveit_config()
    launch_description = generate_move_group_launch(moveit_config)
    return LaunchDescription([
        *_hardware_launch_arguments(),
        *launch_description.entities,
    ])
