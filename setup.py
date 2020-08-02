from glob import glob

import setuptools
from setuptools.command.build_ext import build_ext
from setuptools.extension import Extension


class BuildExtWithoutPlatformSuffix(build_ext):
    def get_ext_filename(self, ext_name):
        super().get_ext_filename(ext_name)
        return ext_name + '.so'


with open("README.md", "r") as fh:
    long_description = fh.read()

setup = setuptools.setup(
    name='FastBLEU',
    version="0.0.41",
    author="Danial Alihosseini",
    author_email="danial.alihosseini@gmail.com",
    description="A fast multithreaded C++ implementation of nltk BLEU.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Danial-Alh/fast-bleu",
    cmdclass={'build_ext': BuildExtWithoutPlatformSuffix},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 7 - Inactive",
    ],
    python_requires='>=3',
    install_requires=["fast-bleu"],
    platforms=['POSIX :: Linux'],
    license='OSI Approved :: MIT License'
)
