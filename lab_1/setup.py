from setuptools import setup, find_packages

setup(
    name='garden_plot_core',
    version='0.1.0',
    packages=find_packages(where='.', include=['src', 'src.*']),
    package_dir={'': '.'},
    install_requires=[],
    python_requires='>=3.8',
)