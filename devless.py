import requests
import random
import json 

class Sdk(object):

    connection = {};
    headers    = {};
    payload    = {};

    def __init__(self, instance_url, token):
        self.payload['user_token'] = ''
        self.payload['params'] = {}
        self.connection['instance_url'] = instance_url
        self.headers = {
                'content-type':  "application/json",
                'cache-control': "no-cache",
                'devless-token': token
                }
        
    def add_data(self, service, table, data):
        data   = json.dumps({"resource": [ {'name':table,"field":[data] } ]})
        sub_url = '/api/v1/service/{service}/db'.format(service=service)
        return self.request_processor(data, sub_url, 'POST')

    def get_data(self, service, table):
        data   = {}
        params = self.payload['params'] if 'params' in self.payload else ''
        def query_maker(params):
            query_params = ''
            for key, value in params.items():
                if(type(value) == list):
                    for key_word in value:
                        query_params += "&{key}={key_word}".format(key=key, key_word=key_word)
                else:
                    query_params = "&{key}={value}{query_params}".format(key=key, value=value,
                        query_params=query_params)
            return query_params
        query = query_maker(params) if params != None else ''    
        sub_url = '/api/v1/service/{service}/db?table={table}{query}'.format(service=service, table=table, query=query)
        return self.request_processor(data, sub_url, 'GET')
    
    def update_data(self, service, table, data):
        params = self.payload['params']['where'][0]
        data   = json.dumps({"resource":[{"name":table,"params":[{"where":params,"data":[data]}]}]})
        sub_url = '/api/v1/service/{service}/db'.format(service=service)
        return self.request_processor(data, sub_url, 'PATCH')

    def delete_data(self, service, table):
        params = self.payload['params']['where'][0]
        data   = json.dumps({"resource":[{"name":table,"params":[{"where":params,"delete":"true"}]}]})
        sub_url = '/api/v1/service/{service}/db'.format(service=service)
        return self.request_processor(data, sub_url, 'DELETE')

    def call(self, service, method, params={}):
        call_id = random.randint(1, 200000)
        params  = json.dumps({ "jsonrpc":"2.0","method":service,"id":call_id,"params":params})
        sub_url = "/api/v1/service/{service}/rpc?action={method}".format(service=service, method=method)
        return self.request_processor(params, sub_url, 'POST')

    def set_user_token(self, token):
        self.headers['devless-user-token'] = token
        return self 

    def where(self, column, value):
        param = "{column},{value}".format(column=column, value=value)
        self.bind_to_params('where', param)
        return self

    def offset(self, value):
        self.bind_to_params('offset', value)
        return self

    def order_by(self, value):
        self.bind_to_params('order_by', value)
        return self

    def size(self, value):
        self.bind_to_params('size', value)
        return self

    def bind_to_params(self, method_name, args):
        if method_name == 'where':
            self.payload['params'][method_name] =  [] if not method_name in self.payload['params'] else self.payload['params'][method_name]
            self.payload['params'][method_name].append(args)
        else:
            self.payload['params'][method_name] = None if method_name in self.payload['params'] else ''
            self.payload['params'][method_name] = args;

    def seq_iter(self, obj):
        return obj if isinstance(obj, list) else iter(obj)     

    def request_processor(self, data, sub_url, method):
        url = "{instance_url}{sub_url}".format(
            instance_url = self.connection['instance_url'], sub_url
            = sub_url)
        response = requests.request(method,
         url, data=data, headers=self.headers)
        output_text = response.text
        start  = output_text.find('{')
        end    = output_text.rfind('}')
        json_output = output_text[start:end+1] if start is not -1 or end is not -1 else output_text
        return json.loads(json_output)
