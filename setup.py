from setuptools import setup, find_packages


setup(
    name="mansplain",
    description="It basically explains stuff for you.",
    long_description="",
    author="Evan Doyle",
    author_email="evanmdoyle@gmail.com",
    version="0.1.0",
    license="MIT",
    url="https://github.com/emdoyle/homebrew-mansplain",
    packages=find_packages(),
    python_requires=">=3.5",
    entry_points={
        "console_scripts": [
            "mansplain = bin.mansplain:mansplain",
        ]
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Framework",
    ],
)
