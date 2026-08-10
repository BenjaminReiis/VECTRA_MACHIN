from setuptools import setup
import os
from glob import glob


package_name = 'projeto2_robot'


setup(
    name=package_name,
    version='0.0.1',

    packages=[
        package_name
    ],

    data_files=[

        (
            'share/ament_index/resource_index/packages',
            [
                'resource/' + package_name
            ]
        ),

        (
            'share/' + package_name,
            [
                'package.xml'
            ]
        ),

        (
            os.path.join(
                'share',
                package_name,
                'launch'
            ),
            glob('launch/*.py')
        ),

        (
            os.path.join(
                'share',
                package_name,
                'config'
            ),
            glob('config/*.yaml')
        ),
    ],

    install_requires=[
        'setuptools'
    ],

    zip_safe=True,

    description=
        'Projeto 2 - IA Multimodal para Robos Autonomos',

    license='Apache-2.0',

    entry_points={

        'console_scripts': [

            'perception_node =
                projeto2_robot.perception_node:main',

            'world_model_node =
                projeto2_robot.world_model_node:main',

            'decision_node =
                projeto2_robot.decision_node:main',

            'navigation_node =
                projeto2_robot.navigation_node:main',

            'motor_adaptation_node =
                projeto2_robot.motor_adaptation_node:main',

            'safety_node =
                projeto2_robot.safety_node:main',

            'main_controller =
                projeto2_robot.main_controller:main',
        ],
    },
)
