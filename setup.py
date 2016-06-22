"""Packaging entry point."""
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand  # noqa


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        pytest.main(self.test_args)


with open('requirements.txt') as f:
    requirements = f.read().split()


with open('requirements-test.txt') as f:
    test_requirements = f.read().split()


with open('VERSION') as f:
    version = f.read().strip()


setup(
    name='ndkrm',
    version=version,
    packages=find_packages(),
    install_requires=requirements,
    tests_require=test_requirements,
    cmdclass={'test': PyTest},
    entry_points={
        'console_scripts': [
            'ndkrm = ndkrm:main'
        ]
    }
)
