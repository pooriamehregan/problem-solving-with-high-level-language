import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Instapy",
    version="0.0.1",
    author="pooriam",
    author_email="pooriam@student.matnat.uio.no",
    description="A small filter package for Instagram.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.uio.no/IN3110/IN3110-pooriam/tree/master/assignment4",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6, <3.9',
    install_requires=['numpy==1.19.4', 'numba', 'opencv-python', 'pytest', 'llvmlite'],
    scripts=['bin/Instapy']
)
