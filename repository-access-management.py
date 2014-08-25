from trac.core import *
from trac.util.html import html
from trac.web import IRequestHandler
from trac.web.chrome import INavigationContributor

class RepositoryAccessManagementPlugin(Component):
    implements(INavigationContributor, IRequestHandler)

    # INavigationContributor methods
    def get_active_navigation_item(self, req):
        return 'helloworld'
    def get_navigation_items(self, req):
        yield ('mainnav', 'helloworld',
            html.A('Hello world', href= req.href.helloworld()))

    # IRequestHandler methods
    def match_request(self, req):
        return req.path_info == '/helloworld'
    def process_request(self, req):
        content = 'Hello World!'
        req.send_response(200)
        req.send_header('Content-Type', 'text/plain')
        req.send_header('Content-Length', len(content))
        req.end_headers()
        req.write(content)