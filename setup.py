import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="beewi_smartclim",
    version=os.getenv('VERSION'),
    author="Vroume",
    author_email="none",
    description="Library to read data from BeeWi SmartClim sensor using Bluetooth LE (using bleak instead of bluepy).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Vroume/beewi_smartclim_bleak",
    packages=setuptools.find_packages(),
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires=['bleak>=0.19.4'],
    keywords='temperature and humidity sensor bluetooth low-energy ble beewi smartclim',
)
