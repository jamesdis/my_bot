🧩 2️⃣ Tinh chỉnh lại trong lidar.xacro (Gazebo)
<gazebo reference="laser_frame">
  <material>Gazebo/Red</material>

  <sensor name="lds_laser" type="ray">
    <pose>0 0 0 0 0 0</pose>
    <visualize>true</visualize>

    <!-- LDS quay 5Hz ~ 300rpm -->
    <update_rate>5</update_rate>

    <ray>
      <scan>
        <horizontal>
          <samples>360</samples>        <!-- Độ phân giải góc 1° -->
          <min_angle>-3.14159</min_angle>
          <max_angle>3.14159</max_angle>
        </horizontal>
      </scan>

      <range>
        <min>0.12</min>                 <!-- Theo datasheet -->
        <max>3.5</max>                  <!-- Theo datasheet -->
      </range>

      <noise>
        <type>gaussian</type>
        <mean>0.0</mean>
        <stddev>0.01</stddev>          <!-- Mô phỏng sai số ±10mm -->
      </noise>
    </ray>


⚡ 3️⃣ ROS2 Launch (driver thực tế)

Trong file lds.launch.py (thay cho rplidar.launch.py):

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



    

    <plugin name="laser_controller" filename="libgazebo_ros_ray_sensor.so">
      <ros><argument>~/out:=scan</argument></ros>
      <output_type>sensor_msgs/LaserScan</output_type>
      <frame_name>laser_frame</frame_name>
    </plugin>
  </sensor>
</gazebo>


Cài gói cho LDS HLS-LFCD2 trên ROS2 Foxy là:

sudo apt update
sudo apt install ros-foxy-hls-lfcd-lds-driver


Sau đó chạy node:
ros2 run hls_lfcd_lds_driver hlds_laser_publisher \
  --ros-args -p port:=/dev/ttyUSB0 -p frame_id:=laser_frame -p baud_rate:=230400

