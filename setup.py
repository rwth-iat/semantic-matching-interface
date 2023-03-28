import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="semantic_matching_interface",
    version="0.0.1",
    author="Sebastian Heppner",
    author_email="s.heppner@plt.rwth-aachen.de",
    description="Providing an interface for a semantic matching service",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(exclude=["test", "test.*"])
)
