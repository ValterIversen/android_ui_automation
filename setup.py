from setuptools import setup, find_packages

setup(
    name="robotframework-androiduiautomation",
    version="0.1.7",
    description="Robot Framework library for Android automation using uiautomator2",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Seu Nome",
    packages=find_packages(),
    py_modules=["AndroidUiAutomation"], 
    install_requires=[
        "uiautomator2",
        "robotframework",
    ],
    python_requires=">=3.8",
)
