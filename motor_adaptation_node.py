import rclpy
from rclpy.node import Node

from std_msgs.msg import String

import json


class MotorAdaptationNode(Node):

    def __init__(self):
        super().__init__(
            'motor_adaptation_node'
        )

        self.trajectory_sub = self.create_subscription(
            String,
            '/trajectory',
            self.trajectory_callback,
            10
        )

        self.feedback_pub = self.create_publisher(
            String,
            '/motor_command',
            10
        )

        self.speed = 0.5

        self.get_logger().info(
            'Motor Adaptation iniciado.'
        )

    def trajectory_callback(
        self,
        msg
    ):

        data = json.loads(
            msg.data
        )

        trajectory = data[
            "trajectory"
        ]

        self.execute_trajectory(
            trajectory
        )

    def execute_trajectory(
        self,
        trajectory
    ):

        for i in range(
            len(trajectory) - 1
        ):

            current = trajectory[i]

            next_point = trajectory[i + 1]

            dx = (
                next_point[0]
                -
                current[0]
            )

            dy = (
                next_point[1]
                -
                current[1]
            )

            command = {
                "linear_velocity":
                    self.speed,

                "angular_velocity":
                    0.0
            }

            self.publish_command(
                command
            )

    def publish_command(
        self,
        command
    ):

        msg = String()

        msg.data = json.dumps(
            command
        )

        self.feedback_pub.publish(
            msg
        )


def main(args=None):

    rclpy.init(args=args)

    node = MotorAdaptationNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
