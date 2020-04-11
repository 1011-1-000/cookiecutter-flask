import copy

from flask_restplus import Namespace, fields

# sample model dict
common_model_dict = {
    'public_id': fields.String(description='the public id'),
    'list': fields.List(fields.String(description='the list')),
    'args': fields.Raw(description='arguments dictionary'),
    'num': fields.Integer(description='percent ratio'),
}


class DTOHelper:

    def __init__(self, api, model_dict):
        self.api = api
        self.model_dict = model_dict

    def generate_dto_all(self, name='name'):
        return self.api.model(name, self.model_dict)

    def generate_dto_include(self, name='name', includes=[]):

        dic = {}
        for _property in includes:
            dic[_property] = self.model_dict[_property]
        return self.api.model(name, dic)

    def generate_dto_exclude(self, name='name', excludes=[]):
        dic = copy.deepcopy(self.model_dict)
        for _property in excludes:
            dic.remove(_property)
        return self.api.model(name, dic)
