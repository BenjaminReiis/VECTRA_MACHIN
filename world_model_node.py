import rclpy
from rclpy.node import Node

from std_msgs.msg import String

import json


class WorldModelNode(Node):

    def __init__(self):
        super().__init__('world_model_node')

        self.subscription = self.create_subscription(
            String,
            '/perception',
            self.perception_callback,
            10
        )

        self.world_pub = self.create_publisher(
            String,
            '/world_model',
            10
        )

        self.world = {
            "robot": {
                "position": [0.0, 0.0],
                "orientation": 0.0
            },

            "objects": [],

            "obstacles": [],

            "terrain": "unknown",

            "locations": [],

            "dynamic_entities": [],

            "uncertainty": {}
        }

        self.get_logger().info(
            'World Model iniciado.'
        )

    def perception_callback(self, msg):

        perception = json.loads(msg.data)

        self.update_world(
            perception
        )

        self.publish_world()

    def update_world(self, perception):

        objects = perception.get(
            "objects",
            []
        )

        self.world["objects"] = objects

        self.world["obstacles"] = perception.get(
            "obstacles",
            []
        )

        self.world["terrain"] = perception.get(
            "terrain",
            "unknown"
        )

        self.world["uncertainty"] = {
            "objects": 0.1,
            "position": 0.2,
            "terrain": 0.5
        }

    def publish_world(self):

        msg = String()

        msg.data = json.dumps(
            self.world
        )

        self.world_pub.publish(msg)


def main(args=None):

    rclpy.init(args=args)

    node = WorldModelNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
