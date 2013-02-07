from setuptools import setup

setup(
    name='twitter-text-python',
    version='1.0',
    description='A tweet parser and formatter',
    long_description=open('README.md').read(),
    author='Ivo Wetzel',
    author_email='',
    url='http://github.com/BonsaiDen/twitter-text-python',
    license='GPL',
    py_modules=['ttp'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
