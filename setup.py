from setuptools import setup

setup(
    name='frecog',
    version='0.0.1',
    install_requires=[
        'Click',
        'nose2',
        'face_recognition',
        'configparser',
        'opencv-python',
        'matplotlib',
        'sklearn',
        'keras',
        'tensorflow',
        'pymysql',
        'sqlalchemy',
        'dlib',
        'gunicorn',
        'flask_sqlalchemy'
    ],
    author='TeamOne',
)