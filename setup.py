from setuptools import find_packages, setup

from info import author, author_email, description, package_name


def parse_requirements(filename):
    """load requirements from a pip requirements file"""
    with open(filename, "r") as f:
        lineiter = (line.strip() for line in f)
        return [
            line.strip()
            for line in lineiter
            if line and not line.startswith("#")
        ]


requirements = parse_requirements("requirements.txt")

setup(
    name=package_name,
    version="0.1",  # Replace with your package's version
    packages=find_packages(),
    include_package_data=False,
    install_requires=requirements,
    entry_points={
        # Optional: if you have scripts or executables
        # 'console_scripts': ['your_script = your_package.module:function'],
    },
    # Add additional metadata about your package
    author=author,
    author_email=author_email,
    description=description,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",  # This is important if your README is in Markdown
    # url="http://github.com/yourusername/your_package_name",  # Replace with the URL to your project
    # classifiers=[
    #     # Choose your license and development status
    #     "License :: OSI Approved :: MIT License",
    #     "Development Status :: 3 - Alpha",
    #     # Specify the Python versions you support here
    #     "Programming Language :: Python :: 3",
    #     "Programming Language :: Python :: 3.7",
    #     "Programming Language :: Python :: 3.8",
    #     "Programming Language :: Python :: 3.9",
    # ],
)
