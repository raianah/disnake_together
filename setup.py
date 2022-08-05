from setuptools import setup, find_packages

classifiers = [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
]

setup(
    name='disnake_together',
    version='1.2.6',
    description="A 3rd party library to use discord's VC Party Games feature with disnake",
    long_description="A 3rd party library to use discord's VC Party Games feature i.e YouTube together, "
                     "Betrayal.io, Fishington.io, Chess in the park, Poker night",
    url='https://github.com/raianah/disnake_together',
    author='raianah',
    author_email='raianah.twilight@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords=['disnake_together', 'disnake', 'disnake-vc-interactions'],
    packages=find_packages(),
    install_requires=['aiohttp>=3.7.2']
)
