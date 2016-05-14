from setuptools import setup

with open("README.md", "rb") as md:
    README = md.read().decode("utf-8")

setup(
    name="cypher",
    packages=["cypher"],
    entry_points={"console_scripts": ["cypher=cypher.cypher:main"]},
    version="0.0.1",
    description="A source code identification tool.",
    include_package_data=True,
    long_description=README,
    author="Joseph Kato"
)
