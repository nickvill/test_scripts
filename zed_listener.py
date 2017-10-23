import rospy
from std_msgs.msg import String
from sensor_msgs.msg import PointCloud2

class zed_listener:
    
    def __init__(self):

        self.sub = rospy.Subscriber('/zed/depth/depth_registered', PointCloud2, callback)

        self.pub = rospy.Publisher('depth', PointCloud2, queue_size=5)
        

    def callback(data):
        self.pub.publish(data)

if __name__ == '__main__':
    rospy.init_node('listener', anonymous=True)
    rospy.spin()
