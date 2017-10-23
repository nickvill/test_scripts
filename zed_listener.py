import rospy
from std_msgs.msg import String
from sensor_msgs.msg import PointCloud2

class zed_listener(object):

    def __init__(self):

        self.sub = rospy.Subscriber('/zed/point_cloud/cloud_registered', PointCloud2, self.callback, queue_size=5)

        self.pub = rospy.Publisher('depth', PointCloud2, queue_size=5)

    def callback(data):
        self.pub.publish(data)
        print "pubbed"

if __name__ == '__main__':
    rospy.init_node('listener', anonymous=True)
    zed_list = zed_listener()
    rospy.spin()
