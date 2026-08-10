import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image, LaserScan, Imu
from std_msgs.msg import String

import json


class PerceptionNode(Node):

    def __init__(self):
        super().__init__('perception_node')

        self.camera_sub = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.camera_callback,
            10
        )

        self.lidar_sub = self.create_subscription(
            LaserScan,
            '/scan',
            self.lidar_callback,
            10
        )

        self.imu_sub = self.create_subscription(
            Imu,
            '/imu/data',
            self.imu_callback,
            10
        )

        self.perception_pub = self.create_publisher(
            String,
            '/perception',
            10
        )

        self.camera_data = None
        self.lidar_data = None
        self.imu_data = None

        self.get_logger().info(
            'Perception Node iniciado.'
        )

    def camera_callback(self, msg):

        self.camera_data = msg

        # Aqui futuramente entra:
        #
        # YOLO
        # Segmentação
        # Depth estimation
        # Vision Transformer
        # VLM
        #
        # Por enquanto usamos dados simulados.

        detected_objects = [
            {
                "class": "door",
                "confidence": 0.94,
                "position": [4.2, 2.1]
            },
            {
                "class": "table",
                "confidence": 0.87,
                "position": [2.0, 3.5]
            }
        ]

        self.publish_perception(
            detected_objects
        )

    def lidar_callback(self, msg):

        self.lidar_data = msg

        min_distance = min(
            msg.ranges
        ) if msg.ranges else float('inf')

        if min_distance < 0.7:

            self.get_logger().warn(
                'Obstáculo próximo!'
            )

    def imu_callback(self, msg):

        self.imu_data = msg

    def publish_perception(self, objects):

        data = {
            "objects": objects,
            "terrain": "unknown",
            "obstacles": [],
            "free_space": []
        }

        msg = String()

        msg.data = json.dumps(data)

        self.perception_pub.publish(msg)


def main(args=None):

    rclpy.init(args=args)

    node = PerceptionNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
