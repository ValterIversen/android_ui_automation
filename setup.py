from setuptools import setup, find_packages

setup(
    name="android_ui_automation",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "uiautomator2>=2.16.1",
    ],
    python_requires=">=3.8",
    description="Python library for Android UI automation using uiautomator2",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Valter Souza",
    url="https://github.com/seuusuario/android_ui_automation",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
