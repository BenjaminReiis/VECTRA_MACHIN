import json

import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class SafetyNode(Node):

    def __init__(self):

        super().__init__(
            'safety_node'
        )

        self.declare_parameter(
            'emergency_distance',
            0.35
        )

        self.declare_parameter(
            'max_velocity',
            0.8
        )

        self.motor_sub = self.create_subscription(
            String,
            '/cmd_vel_ai',
            self.motor_callback,
            10
        )

        self.lidar_sub = self.create_subscription(
            String,
            '/safety_obstacle',
            self.obstacle_callback,
            10
        )

        self.cmd_pub = self.create_publisher(
            String,
            '/cmd_vel',
            10
        )

        self.minimum_distance = 999.0

    def obstacle_callback(self, msg):

        data = json.loads(
            msg.data
        )

        self.minimum_distance = data.get(
            'distance',
            999.0
        )

    def motor_callback(self, msg):

        command = json.loads(
            msg.data
        )

        emergency_distance = self.get_parameter(
            'emergency_distance'
        ).value

        max_velocity = self.get_parameter(
            'max_velocity'
        ).value

        velocity = command.get(
            'linear_velocity',
            0.0
        )

        if self.minimum_distance < emergency_distance:

            self.get_logger().error(
                'EMERGENCIA: obstaculo muito proximo!'
            )

            velocity = 0.0

        velocity = max(
            -max_velocity,
            min(
                velocity,
                max_velocity
            )
        )

        safe_command = {

            'linear_velocity':
                velocity,

            'angular_velocity':
                command.get(
                    'angular_velocity',
                    0.0
                )
        }

        output = String()

        output.data = json.dumps(
            safe_command
        )

        self.cmd_pub.publish(
            output
        )


def main(args=None):

    rclpy.init(args=args)

    node = SafetyNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
