from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    Shutdown,
)
from launch.conditions import IfCondition
from launch.substitutions import (
    Command,
    LaunchConfiguration,
    PathJoinSubstitution,
)
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterFile, ParameterValue
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    deploy_package = FindPackageShare("ur5_workbench_description")

    arguments = []
    arguments.append(
        DeclareLaunchArgument(
            "use_sim_time",
            default_value="false",
        )
    )
    arguments.append(
        DeclareLaunchArgument(
            "rviz_config_file",
            default_value="view.rviz",
        ),
    )

    rviz_config_file = PathJoinSubstitution(
        [deploy_package, "rviz", LaunchConfiguration("rviz_config_file")]
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
        parameters=[
            {"use_sim_time": ParameterValue(LaunchConfiguration("use_sim_time"))},
        ],
        arguments=["-d", rviz_config_file],
    )

    return LaunchDescription(
        arguments
        + [
            rviz_node,
        ]
    )
