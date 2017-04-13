# -*- coding: utf-8 -*-
"""
baka_assets for baka framework or pyramid
------------------------------------------


Management assets for baka framework and Pyramid using
`webassets <http://webassets.readthedocs.org>`_.


Basic usage
```````````

.. code:: python

    baka_assets.config = {your_root_package_or_egg}:configs
    baka_assets.assets = {your_root_package_or_egg}:assets

    baka_assets.bundles = assets.yaml
    baka_assets.url = static
    baka_assets.debug = False
    baka_assets.manifest = file
    baka_assets.cache = False
    baka_assets.auto_build = True


in assets.yaml

.. code::

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


.. code:: python

    config.include('baka_assets')


in development.ini


.. code::

    pyramid.includes =
        pyramid_debugtoolbar
        baka_assets


Usage in mako template
```````````````````````

.. code::
    % for url in request.web_env['js-vendor'].urls():
      <script src="${request.static_url(url)}" />
    % endfor


.. code:: python

    js = Bundle('js/main.js', filters='uglifyjs', output='bundle.js',
                depends='js/**/*.js')

"""
from setuptools import setup, find_packages


setup(name='baka_assets',
      version='0.3.9',
      description='Assets for Baka and Pyramid',
      long_description=__doc__,
      author='Nanang Suryadi',
      license='MIT',
      author_email='nanang.jobs@gmail.com',
      url='https://github.com/baka-framework/baka_assets',
      packages=find_packages(),
      keywords=['webpack', 'webassets', 'baka assets', 'pyramid assets'],
      install_requires=['pyramid',
                        'webassets',
                        'six',
                        'PyYAML',
                        'pyScss',
                        'PyExecJS',
                        'jsmin',
                        'cssmin'],
      test_suite='',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6'
      ])
