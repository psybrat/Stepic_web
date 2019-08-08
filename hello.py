

def echo(env, start_response):
    result = '\r\n'.join(env['QUERY_STRING'].split('&'))
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    return result


