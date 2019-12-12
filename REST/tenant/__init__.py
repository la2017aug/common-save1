from flask import Blueprint
from flask_restful import Api
from tenant.tenants import TenantsRes


tenants_bp = Blueprint('tenants', __name__)
api = Api(tenants_bp, catch_all_404s=True)
api.add_resource(TenantsRes, '/tenants', '/tenants/<passport_id>')
