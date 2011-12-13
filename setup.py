from setuptools import setup, find_packages

setup(
    name='letterbox',
    version=__import__('letterbox').__version__,
    description='User notification management for django',
    long_description="",
    author='Matt George',
    author_email='mgeorge@gmail.com',
    url='https://github.com/stratasan/letterbox',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
)

