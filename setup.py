try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

GITHUB_URL = 'https://github.com/tiyberius/project-euler'
doclink = 'Please visit {}.'.format(GITHUB_URL)

setup(
    name='project_euler',
    version=0.0,
    description='Solutions to a few problems from http://projecteuler.net',
    author='Tobias Work',
    author_email='tiyberius@gmail.com',
    url=GITHUB_URL,
    packages=[
        'names_scores',
    ],
    package_dir={'project-euler': 'names_scores'},
    include_package_data=True,
    install_requires=[
        'contexttimer==0.3.1',
    ],
    license='MIT',
    zip_safe=False,
    keywords='euler',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
