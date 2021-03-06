from setuptools import setup

metadata = {}
with open("phioncli/metadata.py", encoding='utf-8') as fp:
    exec(fp.read(), metadata)

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name= 'phioncli',
    version=metadata['__version__'],
    author = 'sortedcord',
    author_email = 'aditsuyag@gmail.com',
    description= 'The command-line interface for the PHION project',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url= "https://github.com/phion-pm/cli",
    project_urls={
        "Bug Tracker": "https://github.com/phion-pm/cli/issues",
    },
    # 'Project.subdir': 'Project/subdir' 
    package_dir = {},
    # main project, project.subdir
    packages=['phioncli'],
    entry_points = {},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Topic :: Desktop Environment :: Window Managers"
    ],
    install_requires = [
        "loguru>=0.5.3"
    ],
    extras_require = {
        "dev": [
            "pytest>=3.7",
        ],
    },

)