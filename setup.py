import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="uteis",
    version="0.1.2",
    author="Ran#",
    author_email="ran-n@tutanota.com",
    description="Paquetes con funcións uteis para programar en python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ran-n/uteis",
    project_urls={
        "Bug Tracker": "https://github.com/ran-n/uteis/issues",
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)
