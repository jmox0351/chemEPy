import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chemEPy-Jacob-Moxley",
    version="0.0.1",
    author="Jacob Moxley",
    author_email="jacob.moxley@colorado.edu",
    description="A package for chemical engineering",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jmox0351/chemEPy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data = True,
    package_data = {'':['data/*.csv']},
    python_requires='>=3.8',
)
