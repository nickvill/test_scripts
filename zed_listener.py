import rospy
from std_msgs.msg import String
from sensor_msgs.msg import PointCloud2
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np


class zed_listener(object):

    def __init__(self):

        # self.sub = rospy.Subscriber('/zed/point_cloud/cloud_registered', PointCloud2, self.callback, queue_size=5)
        self.sub = rospy.Subscriber('/zed/rgb/image_raw_color', Image, self.callback, queue_size=5)

        self.pub = rospy.Publisher('depth', PointCloud2, queue_size=5)
        self.bridge = CvBridge()

    def callback(self, msg):

        self.pub.publish(msg)
        print "pubbed"

        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        except CvBridgeError as e:
            print e

        height, width, channels = cv_image.shape

        print 'width: ', width, 'height: ', height
        
        

if __name__ == '__main__':
    rospy.init_node('listener', anonymous=True)
    zed_list = zed_listener()
    rospy.spin()
