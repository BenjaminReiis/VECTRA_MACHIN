import rclpy
from rclpy.node import Node

from std_msgs.msg import String

import json
import math


class NavigationNode(Node):

    def __init__(self):
        super().__init__('navigation_node')

        self.goal_sub = self.create_subscription(
            String,
            '/navigation_goal',
            self.goal_callback,
            10
        )

        self.world_sub = self.create_subscription(
            String,
            '/world_model',
            self.world_callback,
            10
        )

        self.trajectory_pub = self.create_publisher(
            String,
            '/trajectory',
            10
        )

        self.current_position = [
            0.0,
            0.0
        ]

        self.obstacles = []

        self.get_logger().info(
            'Navigation Node iniciado.'
        )

    def world_callback(self, msg):

        world = json.loads(
            msg.data
        )

        self.current_position = (
            world["robot"]["position"]
        )

        self.obstacles = (
            world["obstacles"]
        )

    def goal_callback(self, msg):

        goal = json.loads(
            msg.data
        )

        target = goal["position"]

        trajectory = self.plan(
            self.current_position,
            target
        )

        self.publish_trajectory(
            trajectory
        )

    def plan(
        self,
        start,
        goal
    ):

        trajectory = []

        steps = 20

        for i in range(steps + 1):

            t = i / steps

            x = (
                start[0]
                +
                t * (goal[0] - start[0])
            )

            y = (
                start[1]
                +
                t * (goal[1] - start[1])
            )

            trajectory.append(
                [x, y]
            )

        return trajectory

    def publish_trajectory(
        self,
        trajectory
    ):

        msg = String()

        msg.data = json.dumps({
            "trajectory": trajectory
        })

        self.trajectory_pub.publish(
            msg
        )

        self.get_logger().info(
            'Nova trajetória calculada.'
        )


def main(args=None):

    rclpy.init(args=args)

    node = NavigationNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
