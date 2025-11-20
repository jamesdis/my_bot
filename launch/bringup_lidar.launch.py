import os
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import xacro

def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time')

    # URDF processing
    pkg_path = os.path.join(get_package_share_directory('my_bot'))
    xacro_file = os.path.join(pkg_path, 'description', 'robot.urdf.xacro')
    robot_description_config = xacro.process_file(xacro_file)

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{
            'robot_description': robot_description_config.toxml(),
            'use_sim_time': use_sim_time
        }],
        output='screen'
    )

    # Lidar real device
    lidar_node = Node(
        package='hls_lfcd_lds_driver',
        executable='hlds_laser_publisher',
        name='lds_lidar',
        output='screen',
        parameters=[{
            'port': '/dev/ttyUSB0',
            'frame_id': 'laser_frame',
            'baud_rate': 230400
        }]
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use sim time if true'),
        robot_state_publisher_node,
        lidar_node
    ])
