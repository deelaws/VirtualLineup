from flask_restful import Resource
from VirtualLineup import api
from VirtualLineup.mod_store.models import VirtualStore


class VirtualStoreRest(Resource):
    def get(set, store_id):
        store = VirtualStore.query.get(store_id)
        return {'store-name': store.name}

api.add_resource(VirtualStoreRest, '/vstore/<int:store_id>')