import rclpy
from rclpy.node import Node
from person_msgs.msg import Person #使う型を変更
    
rclpy.init()
node = Node("talker")
pub = node.create_publisher(Person, "person", 10) #変更
n = 0
h = 30
def cb():
       global n
       global h
       msg = Person()         #受信するデータ
       msg.name = "身長年齢　比例君" #msgファイルに書いた「name」
       msg.age = n           #msgファイルに書いた「age」
       msg.height = h        #msgファイルに書いた「height」
       pub.publish(msg)
       n += 1
       h += 3
node.create_timer(0.5, cb)
rclpy.spin(node)
