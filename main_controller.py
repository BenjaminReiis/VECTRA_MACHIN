import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MainController(Node):

    def __init__(self):

        super().__init__(
            'main_controller'
        )

        self.status_sub = self.create_subscription(
            String,
            '/world_model',
            self.world_callback,
            10
        )

        self.get_logger().info(
            '================================'
        )

        self.get_logger().info(
            ' PROJETO 2 - ROBOT AI'
        )

        self.get_logger().info(
            ' Multimodal Autonomous Robot'
        )

        self.get_logger().info(
            '================================'
        )

    def world_callback(self, msg):

        self.get_logger().debug(
            'World Model atualizado.'
        )


def main(args=None):

    rclpy.init(args=args)

    node = MainController()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
