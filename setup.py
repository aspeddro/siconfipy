from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

__version__ = "0.0.4b1"

install_requires = ["requests>=2.25.1", "pandas>=1.2.1"]

setup(
    name="siconfipy",
    version=__version__,
    url="https://github.com/pedrocastroo/siconfipy",
    author="Pedro Castro",
    maintainer="Pedro Castro",
    author_email="pdesacastro@gmail.com",
    description="Access data from the Brazilian Public Sector (SICONFI)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    package_data={"siconfipy": ["data/br_cods.csv"]},
    package_dir={"siconfipy": "siconfipy"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Topic :: Database",
    ],
    python_requires=">=3.6",
    install_requires=install_requires,
)
