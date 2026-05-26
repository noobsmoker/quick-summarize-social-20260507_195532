from setuptools import setup, find_packages

setup(
    name="quick-summarize-social-20260507_195532",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'quick=quick:main',
        ],
    },
)
