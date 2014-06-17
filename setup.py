from distutils.core import setup

setup(
    name='django-assets-svg',
    version='0.140617',
    author='Chris Wilson',
    author_email='support+django-assets-svg@aptivate.org',
    packages=['django_assets_svg'],
    url='http://github.com/aptivate/django-assets-svg',
    license='LICENSE.txt',
    description=('Django-Assets support for automatically generating '
        'optimised PNG files from SVG sources.'),
    install_requires=[
        'django-assets',
        'Wand>=0.3.7',
    ],
)
