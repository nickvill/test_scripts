import rospy
from std_msgs.msg import String
from sensor_msgs.msg import PointCloud2
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
import tf
from tf2_msgs import TFMessage


class zed_listener(object):

    def __init__(self):

        # self.sub = rospy.Subscriber('/zed/point_cloud/cloud_registered', PointCloud2, self.pc_callback, queue_size=5)
        self.sub = rospy.Subscriber('/zed/rgb/image_raw_color', Image, self.callback, queue_size=5)
        # self.tfsub = rospy.Subscriber('/tf', TFMessage, self.broadcast, queue_size = 1)
        self.pc_pub = rospy.Publisher('depth', PointCloud2, queue_size=5)
        self.img_pub = rospy.Publisher('zed_img', Image, queue_size=1)
        self.bridge = CvBridge()

    def pc_callback(self, msg):

        self.pub.publish(msg)
        print "pubbed pt cloud"



    def img_callback(self, msg):

        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        except CvBridgeError as e:
            print e

        self.img_pub.publish(msg)
        print 'pubbed img'
        # height, width, channels = cv_image.shape

        # print 'width: ', width, 'height: ', height


        
    
if __name__ == '__main__':
    rospy.init_node('listener', anonymous=True)
    zed_list = zed_listener()
    rospy.spin()
