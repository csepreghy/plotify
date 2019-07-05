from distutils.core import setup
setup(
    name='pyplotify',
    packages=['pyplotify'],
    version='0.2.0',
    license='MIT',
    description='A simple class to give plots some styling. It is a very light skin over matplotlib.pyplot.',
    author='Andrew Chepreghy',
    author_email='andris788@gmail.com',
    url='https://github.com/csepreghy/plotify',
    download_url='https://github.com/csepreghy/plotify/archive/v0.1.tar.gz',
    keywords=['matplotlib', 'visualization', 'plot', 'plots', 'python', 'data science', 'machine learning', 'ai'],
    install_requires=[
        'numpy',
        'matplotlib'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Visualization',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
)
