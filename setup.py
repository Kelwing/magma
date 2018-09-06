from distutils.core import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name='magma',
    version='v3',
    author='init0',
    packages=['magma',],
    license='GPLv3',
    description='The Python connector for Lavalink',
    url='https://github.com/initzx/magma',
    python_requires='>=3.6.6',
    install_requires=["discord.py"],
    long_description=readme,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ]
)
