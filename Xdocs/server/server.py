from bottle import route, run, request


@route('/<resources>/', method='GET')
def list(resources):
    return {resources: request.method}


@route('/<resources>/', method='POST')
def create(resources):
    return {resources: request.method}


@route('/<resources>/<resource_id>/', method='GET')
def retrieve(resources, resource_id):
    return {resources: resource_id + request.method}


@route('/<resources>/<resource_id>/', method='PUT')
def replace(resources, resource_id):
    return {resources: resource_id + request.method}


@route('/<resources>/<resource_id>/', method='PATCH')
def update(resources, resource_id):
    return {resources: resource_id + request.method}


@route('/<resources>/<resource_id>/', method='DELETE')
def delete(resources, resource_id):
    return {resources: resource_id + request.method}


run(host='localhost', port=8881)
