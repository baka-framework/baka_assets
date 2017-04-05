## baka_assets for baka framework or pyramid [baka_assets](https://github.com/suryakencana/baka_assets)

##### Baka assets add-ons
 
Management assets for baka framework and Pyramid using  `webassets <http://webassets.readthedocs.org>`_.


##### Basic usage


in development.ini

```

    baka_assets.config = {your_root_package_or_egg}:configs
    baka_assets.assets = {your_root_package_or_egg}:assets

    baka_assets.bundles = assets.yaml
    baka_assets.url = static
    baka_assets.debug = False
    baka_assets.manifest = file
    baka_assets.cache = False
    baka_assets.auto_build = True
    
```


in assets.yaml

```yaml

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

```




##### setup to config

in python code

```python

    config.include('baka_assets')

```

in development.ini

```

    pyramid.includes =
        pyramid_debugtoolbar
        baka_assets

```


##### Usage in mako template


```html
    % for url in request.web_env['js-vendor'].urls():
      <script src="${request.static_url(url)}" />
    % endfor

```


```python

    js = Bundle('js/main.js', filters='uglifyjs', output='bundle.js',
                depends='js/**/*.js')

```


##### Example


```
   yarn init or npm init
   yarn or npm install
   python -m example      
```

