import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kings_selenium",
    version="1.0.2",
    author="kings",
    author_email="963987632@qq.com",
    url="https://github.com/kings1990/kings_selenium",
    description="encapsulation the web and phone(appium) functions used by selenium ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "Appium-Python-Client == 1.0.1",
        "selenium == 3.141.0"
    ],
    python_requires='>=3'

)