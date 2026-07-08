from launch.substitutions import LaunchConfiguration
from moveit_configs_utils import MoveItConfigsBuilder


def build_moveit_config():
    return (
        MoveItConfigsBuilder(
            "ur5_robotiq_85", package_name="ur5_robotiq85_moveit_config"
        )
        .robot_description(
            mappings={
                "ros2_control_hardware_type": LaunchConfiguration(
                    "ros2_control_hardware_type"
                ),
                "joint_commands_topic": LaunchConfiguration("joint_commands_topic"),
                "joint_states_topic": LaunchConfiguration("joint_states_topic"),
            }
        )
        .to_moveit_configs()
    )
