# -*- coding: utf-8 -*-
"""
baka_assets for baka framework or pyramid
------------------------------------------

Management assets for baka framework and Pyramid using  `webassets <http://webassets.readthedocs.org>`_.


Basic usage
```````````

in development.ini

.. code::

    baka_assets.config = {your_root_package_or_egg}:configs
    baka_assets.assets = {your_root_package_or_egg}:assets

    baka_assets.bundles = assets.yaml
    baka_assets.url = static
    baka_assets.debug = False
    baka_assets.manifest = file
    baka_assets.cache = False
    baka_assets.auto_build = True


in assets.yaml

.. code::yaml

css-vendor:
    filters: scss,cssmin
    depends: '**/*.scss'
    output: {your_root_package_or_egg}:public/vendor.%(version)s.css
    contents: styles/app.scss


js-vendor:
    config:
      UGLIFYJS_BIN: ./node_modules/.bin/uglifyjs
    filters: uglifyjs
    output: {your_root_package_or_egg}:public/vendor.%(version)s.js
    contents:
      - javascripts/pace.js
      - javascripts/moment-with-locales.js
      - javascripts/jquery.js
      - javascripts/handlebars.js
      - javascripts/handlers-jquery.js
      - javascripts/cookies.js
      - javascripts/lodash.js
      - javascripts/materialize.js


setup to config
```````````````
in python code

.. code::python

    config.include('baka_assets')


in development.ini

.. code::

    pyramid.includes =
        pyramid_debugtoolbar
        baka_assets


Usage in mako template
```````````````````````

.. code::html
    % for url in request.web_env['js-vendor'].urls():
      <script src="${request.static_url(url)}" />
    % endfor


.. code:: python

    js = Bundle('js/main.js', filters='uglifyjs', output='bundle.js',
                depends='js/**/*.js')


"""
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.md')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'webassets',
    'six',
    'PyYAML',
    'pyScss',
    'PyExecJS',
    'jsmin',
    'cssmin'
    ]

setup(name='baka_assets',
      version='0.3.6',
      description='baka_assets',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid baka_assets',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="baka_assets",
      entry_points="""\
      """,
      )
