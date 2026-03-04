#!/ur/bin/env python

import rospy
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Header
import numpy as np
import os



from visualization_msgs.msg import Marker


        
        
        
def create_pose(x, y, z, frame_id):
    pose = PoseStamped()
    pose.header = Header()
    pose.header.frame_id = frame_id
    pose.header.stamp = rospy.Time.now()
    pose.pose.position.x = x
    pose.pose.position.y = y
    pose.pose.position.z = z
    pose.pose.orientation.w = 1.0  # 简单起见，忽略朝向
    return pose

def publish_path(matrix,marker_vec1,marker_vec2,marker_vec3,ida):




    marker1 = Marker()
    marker1.header.frame_id = "world"
    marker1.header.stamp = rospy.Time.now()

    
    marker1.ns = "drone_t1"


    marker1.type = Marker.MESH_RESOURCE
    marker1.action = Marker.ADD

    marker1.pose.position.x = marker_vec1[0,0]
    marker1.pose.position.y = marker_vec1[1,0]
    marker1.pose.position.z = marker_vec1[2,0]
    marker1.pose.orientation.x = 0.0
    marker1.pose.orientation.y = 0.0
    marker1.pose.orientation.z = 0.0
    marker1.pose.orientation.w = 1.0

    marker1.scale.x = 0.5
    marker1.scale.y = 0.5
    marker1.scale.z = 0.5

    marker1.color.a = 1.0 # Don't forget to set the alpha!
    marker1.color.r = 0.0
    marker1.color.g = 0.0
    marker1.color.b = 0.0
    
    marker1.mesh_resource = "package://plt_trajectory/scripts/hummingbird.mesh"









    marker2 = Marker()
    marker2.header.frame_id = "world"
    marker2.header.stamp = rospy.Time.now()

    
    marker2.ns = "drone_t2"


    marker2.type = Marker.MESH_RESOURCE
    marker2.action = Marker.ADD

    marker2.pose.position.x = marker_vec2[0,0]
    marker2.pose.position.y = marker_vec2[1,0]
    marker2.pose.position.z = marker_vec2[2,0]
    marker2.pose.orientation.x = 0.0
    marker2.pose.orientation.y = 0.0
    marker2.pose.orientation.z = 0.0
    marker2.pose.orientation.w = 1.0

    marker2.scale.x = 0.5
    marker2.scale.y = 0.5
    marker2.scale.z = 0.5

    marker2.color.a = 1.0 # Don't forget to set the alpha!
    marker2.color.r = 0.0
    marker2.color.g = 0.0
    marker2.color.b = 0.0
    
    marker2.mesh_resource = "package://plt_trajectory/scripts/hummingbird.mesh"
    
    
    
    marker3 = Marker()
    marker3.header.frame_id = "world"
    marker3.header.stamp = rospy.Time.now()

    
    marker3.ns = "drone_t3"


    marker3.type = Marker.MESH_RESOURCE
    marker3.action = Marker.ADD

    marker3.pose.position.x = marker_vec3[0,0]
    marker3.pose.position.y = marker_vec3[1,0]
    marker3.pose.position.z = marker_vec3[2,0]
    marker3.pose.orientation.x = 0.0
    marker3.pose.orientation.y = 0.0
    marker3.pose.orientation.z = 0.0
    marker3.pose.orientation.w = 1.0

    marker3.scale.x = 0.5
    marker3.scale.y = 0.5
    marker3.scale.z = 0.5

    marker3.color.a = 1.0 # Don't forget to set the alpha!
    marker3.color.r = 0.0
    marker3.color.g = 0.0
    marker3.color.b = 0.0
    
    marker3.mesh_resource = "package://plt_trajectory/scripts/hummingbird.mesh"
    
    
    
    
    



    path_msg = Path()
    path_msg.header = Header()
    path_msg.header.frame_id = "world"

    for i in range(matrix.shape[1]):
        x, y, z = matrix[:, i]
        pose = create_pose(x, y, z, frame_id="world")
        path_msg.poses.append(pose)

    while not rospy.is_shutdown():
        marker3.id = ida
        marker2.id = ida
        marker1.id = ida
        ida = ida + 1
        marker_pub1.publish(marker1)
        marker_pub2.publish(marker2)        
        marker_pub3.publish(marker3)
        path_msg.header.stamp = rospy.Time.now()
        path_pub.publish(path_msg)
        rate.sleep()

if __name__ == '__main__':
    rospy.init_node('path_publisher', anonymous=True)
    ida = 0
    path_pub = rospy.Publisher('/path', Path, queue_size=100)
    marker_pub1 = rospy.Publisher('/odom/robot1', Marker, queue_size=3)
    marker_pub2 = rospy.Publisher('/odom/robot2', Marker, queue_size=3)
    marker_pub3 = rospy.Publisher('/odom/robot3', Marker, queue_size=3)
    rate = rospy.Rate(10)  # 1 Hz
    
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, '__path__fix.npy')
    # 从参数服务器获取矩阵参数
    drone_id = rospy.get_param('~ID')
    path_array = np.load(file_path)
    marker_vec1 = path_array[(drone_id-1)*3:drone_id*3,100:101].reshape(3,1)  # 转置以适应3xN格式
    marker_vec2 = path_array[(drone_id-1)*3:drone_id*3,200:201].reshape(3,1)  # 转置以适应3xN格式
    marker_vec3 = path_array[(drone_id-1)*3:drone_id*3,298:299].reshape(3,1)  # 转置以适应3xN格式
    matrix = path_array[(drone_id-1)*3:drone_id*3,:]  # 转置以适应3xN格式
    publish_path(matrix,marker_vec1,marker_vec2,marker_vec3,ida)





# import rospy
# from visualization_msgs.msg import Marker
# from geometry_msgs.msg import Point

# def create_marker(marker_id, frame_id, position, color):
#     marker = Marker()
#     marker.header.frame_id = frame_id
#     marker.header.stamp = rospy.Time.now()
#     marker.ns = "drone_markers"
#     marker.id = marker_id
#     marker.type = Marker.SPHERE
#     marker.action = Marker.ADD

#     marker.pose.position.x = position[0]
#     marker.pose.position.y = position[1]
#     marker.pose.position.z = position[2]
#     marker.pose.orientation.x = 0.0
#     marker.pose.orientation.y = 0.0
#     marker.pose.orientation.z = 0.0
#     marker.pose.orientation.w = 1.0

#     marker.scale.x = 0.2
#     marker.scale.y = 0.2
#     marker.scale.z = 0.2

#     marker.color.a = 1.0
#     marker.color.r = color[0]
#     marker.color.g = color[1]
#     marker.color.b = color[2]

#     marker.lifetime = rospy.Duration()
    
#     return marker

# def publish_markers():
#     rospy.init_node('drone_marker_publisher', anonymous=True)
#     marker_pub = rospy.Publisher('drone_markers', Marker, queue_size=10)

#     rate = rospy.Rate(1)  # 1 Hz
#     marker_id = 0

#     drone_id = rospy.get_param('~drone_id', 'drone_1')
#     position = rospy.get_param('~position', [0.0, 0.0, 0.0])
#     color = rospy.get_param('~color', [1.0, 1.0, 1.0])

#     while not rospy.is_shutdown():
#         marker = create_marker(marker_id, drone_id, position, color)
#         marker_pub.publish(marker)
#         marker_id += 1

#         rate.sleep()

# if __name__ == '__main__':
#     try:
#         publish_markers()
#     except rospy.ROSInterruptException:
#         pass
