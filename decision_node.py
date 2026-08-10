import rclpy
from rclpy.node import Node

from std_msgs.msg import String

import json


class DecisionNode(Node):

    def __init__(self):
        super().__init__('decision_node')

        self.world_sub = self.create_subscription(
            String,
            '/world_model',
            self.world_callback,
            10
        )

        self.goal_pub = self.create_publisher(
            String,
            '/navigation_goal',
            10
        )

        # Objetivo recebido do humano.
        self.command = (
            'Vá até a área livre próxima à porta.'
        )

        self.get_logger().info(
            f'Objetivo: {self.command}'
        )

    def world_callback(self, msg):

        world = json.loads(msg.data)

        goal = self.interpret_command(
            self.command,
            world
        )

        if goal is not None:

            self.publish_goal(
                goal
            )

    def interpret_command(
        self,
        command,
        world
    ):

        objects = world.get(
            "objects",
            []
        )

        # Procurar uma porta.
        doors = [
            obj for obj in objects
            if obj["class"] == "door"
        ]

        if not doors:

            self.get_logger().warn(
                'Nenhuma porta encontrada.'
            )

            return None

        door = doors[0]

        door_position = door[
            "position"
        ]

        # Futuramente isso será calculado
        # pela IA multimodal.

        goal = {
            "type": "semantic_goal",

            "target": "free_area",

            "reference": "door",

            "position": [
                door_position[0] + 1.0,
                door_position[1]
            ],

            "confidence":
                door["confidence"]
        }

        return goal

    def publish_goal(self, goal):

        msg = String()

        msg.data = json.dumps(
            goal
        )

        self.goal_pub.publish(msg)

        self.get_logger().info(
            f'Objetivo espacial: {goal}'
        )


def main(args=None):

    rclpy.init(args=args)

    node = DecisionNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
