import rospy
from std_msgs.msg import String
from sensor_msgs.msg import PointCloud2

def callback(data):
    pub.publish(data)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('/zed/depth/depth_registered', PointCloud2, callback)

    pub = rospy.Publisher('depth', PointCloud2, queue_size=5)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()