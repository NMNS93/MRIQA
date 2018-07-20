"""Setup script"""
from setuptools import setup, find_packages


setup(
    name='mriqa',
    version='0.1',
    description='UCLH Medical Physics QA Protocol',
    url='https://github.com/nmns93/STP',
    packages=find_packages(),
    include_package_data=True,
    python_requires='==3.6.6',
    install_requires=[
        'matplotlib==2.2.2',
        'numpy==1.14.5',
        'opencv-python==3.4.1.15',
        'pydicom==1.1.0'
    ],
    entry_points={
        'console_scripts': [
            'mriqa=mriqa.mriqa:main',
        ],
        'gui_scripts': [
            'mriqagui=mriqa.gui:main',
        ]
    }
)
