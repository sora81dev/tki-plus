from setuptools import setup, find_packages

setup(
    name='tki-plus',
    version='1.0.3',
    packages=find_packages(),
    install_requires=[
        "tkinter"
    ],
    author='sora81dev',
    author_email='sora81dev@gmail.com',
    description='This library make tkinter more useful.',
    long_description=open('./readme.md', encoding="UTF-8").read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sora81dev/tki-plus',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)