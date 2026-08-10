from launch import LaunchDescription

from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription([

        Node(
            package='projeto2_robot',
            executable='perception_node',
            name='perception',
            output='screen',
            parameters=[
                {
                    'obstacle_distance': 0.7,
                    'confidence_threshold': 0.5
                }
            ]
        ),

        Node(
            package='projeto2_robot',
            executable='world_model_node',
            name='world_model',
            output='screen'
        ),

        Node(
            package='projeto2_robot',
            executable='decision_node',
            name='decision',
            output='screen'
        ),

        Node(
            package='projeto2_robot',
            executable='navigation_node',
            name='navigation',
            output='screen'
        ),

        Node(
            package='projeto2_robot',
            executable='motor_adaptation_node',
            name='motor_adaptation',
            output='screen'
        ),

        Node(
            package='projeto2_robot',
            executable='safety_node',
            name='safety',
            output='screen'
        ),

        Node(
            package='projeto2_robot',
            executable='main_controller',
            name='main_controller',
            output='screen'
        )
    ])
