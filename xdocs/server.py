import os

from bottle import static_file, Bottle, abort, request
from faker import Factory
from yaml import load

app = Bottle(__name__)

app.cwd = os.getcwd()
fake = Factory.create('zh_CN')
base_path = os.getcwd()
source_path = os.path.join(base_path, 'docs')
app.data = {}
app.resources = {}

fake = Factory.create("zh_CN")
for file in os.listdir(source_path):
    if '.yml' in file:
        resource = load(open(os.path.join(source_path, file)).read())
        app.resources[resource['name']] = resource


def generate_mock_data(file_type):
    return eval("fake.{}()".format(file_type))


def setup_data(resources):
    for k, v in resources.items():
        app.data[k] = {}
        temp = {}
        for field in v['model']:
            temp[field["field"]] = generate_mock_data("name")
        app.data[k][temp["id"]] = temp


setup_data(app.resources)


def dict_filter_by_array(source_dict, array):
    result = {}
    for field in array:
        if field in source_dict:
            result[field] = source_dict[field]
    return result


@app.route('/')
def index():
    return static_file("index.html", app.cwd + "/client/")


@app.route('/resource')
def resource():
    return static_file("resource", app.cwd + "/client/")


@app.route('/docs/<filename>')
def docs(filename):
    return static_file(filename, root=app.cwd + '/docs')


@app.route('/static/<filename>')
def static(filename):
    return static_file(filename, root=app.cwd + '/client/static')


@app.route('/api/<resources>/', method='GET')
def list(resources):
    try:
        results = []
        for data in app.data[resources].values():
            return_fields = app.resources[resources]['action']['list']['return']
            results.append(dict_filter_by_array(data, return_fields))
        return {'data': results}
    except:
        abort(404)


@app.route('/api/<resources>/', method='POST')
def create(resources):
    try:
        new_data = dict.fromkeys([field['field'] for field in app.resources[resources]["model"]])
        print(request.POST)
        for key in new_data:
            if key in request.POST:
                new_data[key] = request.POST[key]
        return {'data': new_data}
    except:
        abort(404)


@app.route('/api/<resources>/<resource_id>/', method='GET')
def retrieve(resources, resource_id):
    try:
        return {'data': app.data[resources][resource_id]}
    except:
        abort(404)


@app.route('/api/<resources>/<resource_id>/', method='PUT')
def replace(resources, resource_id):
    try:
        del app.data[resources][resource_id]
        return {'detail': 'success'}
    except:
        abort(404)


@app.route('/api/<resources>/<resource_id>/', method='PATCH')
def update(resources, resource_id):
    try:
        del app.data[resources][resource_id]
        return {'detail': 'success'}
    except:
        abort(404)


@app.route('/api/<resources>/<resource_id>/', method='DELETE')
def destroy(resources, resource_id):
    try:
        del app.data[resources][resource_id]
        return {'detail': 'success'}
    except:
        abort(404)
