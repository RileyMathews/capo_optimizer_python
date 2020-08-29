import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="capo_optimizer",
    version="0.0.1",
    author="Riley Mathews",
    author_email="rileymathews80@gmail.com",
    description="A library to optimize guitar capo position",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rileymathews/capo_optimizer_python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
