"""
 # Copyright (c) 2017 Boolein Integer Indonesia, PT.
 # suryakencana 4/5/17 @author nanang.suryadi@boolein.id
 #
 # You are hereby granted a non-exclusive, worldwide, royalty-free license to
 # use, copy, modify, and distribute this software in source code or binary
 # form for use in connection with the web services and APIs provided by
 # Boolein.
 #
 # As with any software that integrates with the Boolein platform, your use
 # of this software is subject to the Boolein Developer Principles and
 # Policies [http://developers.Boolein.com/policy/]. This copyright notice
 # shall be included in all copies or substantial portions of the software.
 #
 # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
 # THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 # FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
 # DEALINGS IN THE SOFTWARE
 # 
 # __main__
"""
from wsgiref.simple_server import make_server

from pyramid.config import Configurator
from pyramid.view import view_config


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include(__name__)
    return config.make_wsgi_app()


def includeme(config):
    config.include('baka_assets')
    # mako template
    config.include('pyramid_mako')
    # config.add_mako_renderer('.html')
    # config.add_static_view(settings.get('static_assets', 'static'),
    #                        '{egg}:public'.format(egg='example'),
    #                        cache_max_age=3600)

    config.add_route('home', '/')
    config.scan()


@view_config(route_name='home', renderer='example:_base.html')
def route_home(request):
    _ = request
    return {
        'egg': __name__,
        'project': 'Baka Assets',
        'pyramid_version': '1.8.3'
    }


if __name__ == '__main__':
    settings = {
        'baka.egg': 'example',
        'baka_assets.ext': '.html',
        'baka_assets.plim': False,
        'baka_assets.config': '{egg}:configs'.format(egg='example'),
        'baka_assets.assets': '{egg}:assets'.format(egg='example'),
        'baka_assets.bundles': 'assets.yaml',
        'baka_assets.url': 'static',
        'baka_assets.debug': False,
        'baka_assets.manifest': 'file',
        'baka_assets.cache': False,
        'baka_assets.auto_build': True
    }
    app = main({}, **settings)
    httpd = make_server('0.0.0.0', 6543, app)
    # httpd.socket = ssl.wrap_socket(httpd.socket, certfile='certificate.pem',
    #                                server_side=True)
    httpd.serve_forever()
