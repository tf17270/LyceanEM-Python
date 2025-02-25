from setuptools import setup
from setuptools import find_packages  # This line replaces 'from setuptools import setup'
import os
import sys



# Monkey patch msvc compiler environment, so scikit-build does not overwrite
# it. Make sure to set desired environment using:
# > vcvars64.bat -vcvars_ver=<vcvars_ver>
windows._get_msvc_compiler_env = lambda version, toolset: windows.CachedEnv()
# move to the directory of the setup.py file

# Read metadata from setup.cfg
def read_setup_cfg():
    from configparser import ConfigParser

    config = ConfigParser()
    config.read("setup.cfg")
    return config["metadata"]

metadata = read_setup_cfg()
print("hi")
setup(
    name=metadata.get("name"),
    version=metadata.get("version"),
    author=metadata.get("author"),
    author_email=metadata.get("author_email"),
    description=metadata.get("description"),
    long_description=metadata.get("long_description"),
    long_description_content_type=metadata.get("long_description_content_type"),
    url=metadata.get("url"),
    python_requires=metadata.get("python_requires"),
    install_requires=metadata.get("install_requires"),
    classifiers=metadata.get("classifiers", "").split("\n"),
    license=metadata.get("license"),
    license_file=metadata.get("license_file"),
    packages = find_packages(),
    include_package_data=True,
)
