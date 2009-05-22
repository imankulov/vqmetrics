from distutils.core import setup
setup(
        name='vqmetrics',
        version='0.1.0',
        py_modules=['vqmetrics'],
        author='Roman Imankulov',
        author_email='roman@netangels.ru',
        url='http://github.com/imankulov/vqmertics/',
        description='Set of functions to convert between different speech ' + \
        'quality estimation metrics, helper class with Speex codec options',
        long_description = """
vqmetrics module contains a set of functions to convert between different
speech quality estimation metrics such as PESQ MOS, MOS LQO, R-factor.

This module Contains also one helper class with Speex codec options:

    - mapping between speex "quality" and "mode" option

    - size (in bits) for earch speex frame with given mode

    - required bandwidth estimation
""",

)
