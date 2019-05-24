import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='The Shape Of You',
    version='0.1.0',
    author='Yi Sheng Siow',
    author_email='siowyisheng@gmail.com',
    packages=setuptools.find_packages(),
    url='http://pypi.python.org/pypi/the-shape-of-you/',
    license='LICENSE.txt',
    description=
    'Generate images for objects which show their scores in different dimensions in a shape.',
    long_description=open('README.md').read(),
    install_requires=[
        "Pillow >= 2.0",
    ],
    data_files=[(['fonts/LemonMilk.otf'])],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Programming Language :: Python',
        "License :: OSI Approved :: MIT License",
        'Topic :: Multimedia :: Graphics',
        "Operating System :: OS Independent",
    ],
)
