from setuptools import setup, find_packages

setup(
    name="mpox-model",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'streamlit>=1.24.0',
        'numpy>=1.24.0',
        'scipy>=1.10.0',
        'matplotlib>=3.7.0',
        'pillow>=9.5.0',
    ],
    python_requires='>=3.10',
)