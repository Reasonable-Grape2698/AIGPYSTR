from setuptools import setup, find_packages

setup(
    name = 'aigpy',
    version = '2021.2.18.1',
    license = "MIT Licence",
    description = "Python Common Tool",

    author = 'Yaronzz',
    author_email = "yaronhuang@foxmail.com",

    packages = find_packages(),
    platforms = "any",
    include_package_data = True,
    install_requires=["requests", "colorama", "mutagen"],
)
