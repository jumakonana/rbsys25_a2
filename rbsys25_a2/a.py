import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

rclpy.init()
node = Node("a")

def main():
    rclpy.spin(node)
