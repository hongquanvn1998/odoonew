# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from werkzeug.utils import redirect
DEFAULT_IMAGE = '/home/static/src/img/material-background.jpg'

class DasboardBackground(http.Controller):
    @http.route(['/dashboard'], type='http', auth='user', website=False)
    def dashboard(self, **post):
        user = request.env.user
        company = user.company_id
        if company.dashboard_background:
            image = base64.b64decode(company.dashboard_background)
        else:
            return redirect(DEFAULT_IMAGE)

        return request.make_response(
            image, [('Content-Type', 'image')])

class Home(http.Controller):
    @http.route('/', type='http', auth="none")
    def index(self, s_action=None, db=None, **kw):
        return http.local_redirect('/trangdangnhap', query=request.params, keep_hash=True)
    #def _render_template(self, **d):
        # d.setdefault('manage',True)
        # d['insecure'] = odoo.tools.config.verify_admin_password('admin')
        # d['list_db'] = odoo.tools.config['list_db']
        # d['langs'] = odoo.service.db.exp_list_lang()
        # d['countries'] = odoo.service.db.exp_list_countries()
        # d['pattern'] = DBNAME_PATTERN
        # # databases list
        # d['databases'] = []
        # try:
        #     d['databases'] = http.db_list()
        #     d['incompatible_databases'] = odoo.service.db.list_db_incompatible(d['databases'])
        # except odoo.exceptions.AccessDenied:
        #     monodb = db_monodb()
        #     if monodb:
        #         d['databases'] = [monodb]
        return  http.request.env.get_template("templates.xml").render()
    @http.route('/home/dashboard',  type='http', methods=['GET'], website=True, auth='public')
    def index(self,**kw):
        menu =  request.__dict__
        #return self._render_template() Khong tao duoc template
        #return "Hello, world"
        #return  request.render("home.home_template")
        base_url = request.env['ir.config_parameter'].get_param('module')
        context =  request.env['ir.http'].webclient_rendering_context()
        _temp = "home.home_template"
        _model = kw.get('model')
        if _model == "home.home": 
            printf("Da goi duoc model la %s" ,kw.get('model') )
            _temp = "home.home_template"
        else: 
            {}
        response = request.render(_temp, qcontext=context)
        response.headers['X-Frame-Options'] = 'DENY'
        return response

    @http.route('/home/home/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('home.listing', {
            'root': '/home/home',
            'objects': http.request.env['home.home'].search([]),
        })

    @http.route('/home/home/objects/<model("home.home"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('home.object', {
            'object': obj
        })