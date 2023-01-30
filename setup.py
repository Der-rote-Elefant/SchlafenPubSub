try:
    from setuptools import setup
except:
    from distutils.core import setup

NAME = "schlafen_pubsub"
"""
名字，一般放你包的名字即可
"""
PACKAGES = ["SchlafenPubSub"]
"""
包含的包，可以多个，这是一个列表
"""

DESCRIPTION = "SchlafenPubSub: PUB/SUB MODEL"
KEYWORDS = ["rabbitmq", "redis"]
AUTHOR_EMAIL = "625180414@qq.com"
AUTHOR = 'schlafen'
URL = "https://github.com/Der-rote-Elefant/SchlafenPubSub"


LICENSE = "MIT"

setup(
    name=NAME,
    version='1.0.0',
    description=DESCRIPTION,
    long_description='publisher and subscriber',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    # install_requires=['pika==1.1.0'],
    entry_points={
        'console_scripts': [
            'schlafen_ps_pub = SchlafenPubSub.__init__:debug_pub',
            'schlafen_ps_sub = SchlafenPubSub.__init__:debug_sub'
        ]
    },
    keywords=KEYWORDS,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=True
)
