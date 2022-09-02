# coding: utf-8
from os.path import dirname
from os.path import join
import platform

from setuptools import find_packages
from setuptools import setup


linux_dependencies = tuple()
if platform.system() == 'Linux':
    linux_dependencies = ('distro>=1.3.0,<2',)


def main():
    setup(
        name='educommon',
        author="BARS Group",
        author_email='education_dev@bars-open.ru',
        description='Общая кодовая база для проектов БЦ Образование',
        url='https://stash.bars-open.ru/projects/EDUBASE/repos/educommon',
        classifiers=[
            'Intended Audience :: Developers',
            'Environment :: Web Environment',
            'Natural Language :: Russian',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Development Status :: 5 - Production/Stable',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Framework :: Django :: 1.7',
            'Framework :: Django :: 1.8',
            'Framework :: Django :: 1.9',
            'Framework :: Django :: 1.10',
            'Framework :: Django :: 1.11',
            'Framework :: Django :: 2.0',
            'Framework :: Django :: 2.1',
            'Framework :: Django :: 2.2',
        ],
        package_dir={'': 'src'},
        packages=find_packages('src'),
        include_package_data=True,
        dependency_links=(
            'http://pypi.bars-open.ru/simple/m3-builder',
        ),
        setup_requires=(
            'm3-builder>=1.2,<2',
        ),
        install_requires=(
            'six>=1.11,<2',
            'Django>=1.11,<2.3',
            'django-mptt',
            'python-dateutil',
            'termcolor',
            'django-sendfile',
            'requests',
            'celery',
            'spyne',
            'xlsxwriter>=0.9.3,<1',

            'm3-builder>=1.2,<2',
            'm3-django-compat>=1.9.1,<2',
            'm3-core>=2.2.16,<3',
            'm3-ui>=2.2.40,<3',
            'm3-objectpack>=2.2.36,<3',
            'm3-simple-report>=1.4.1,<2',
            'm3-spyne-smev>=0.2.4,<1',
            'python-magic==0.4.15'
        ) + linux_dependencies,
        set_build_info=join(dirname(__file__), 'src', 'educommon'),
    )


if __name__ == '__main__':
    main()
