import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        Node(
            package='hls_lfcd_lds_driver',
            executable='hlds_laser_publisher',
            name='lds_publisher',
            output='screen',
            parameters=[{
                'port': '/dev/ttyUSB0',
                'frame_id': 'laser_frame',
                'baud_rate': 230400
            }]
)
    ])