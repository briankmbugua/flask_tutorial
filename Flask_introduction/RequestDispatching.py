"""When the application receives a request from a clinet, it needs to find what view function to invoke to service it.For this task, Flask looks up the URL given in the request in the application's URL map, which contains a mapping of URLs to the view functions that handle them.Flask builds this map using the app.route decoraters or the equivalent nondecorator version app.add_url_rule()"""

from flask import Flask

app = Flask('__main__')

@app.route('/')
def index():
    return '<h1>Welcome</h1>'

@app.route('/hello')
def hello():
    return '<h1>Hello</h1>'

print(f"url map {app.url_map}")

"""url map Map([<Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>-This is a special route added by flask to give access to static files,
 <Rule '/' (HEAD, OPTIONS, GET) -> index>,
 <Rule '/hello' (HEAD, OPTIONS, GET) -> hello>])
 The HEAD, OPTIONS, GET elements shown in the url map are the request methods that are handled by the route, Flask attaches methods to each route so that different request methods sent to the same URL can be handled by different view functions.The HEAD and OPTIONS methods are managed by automatically by flask"""



if __name__ == '__main__':
    app.run(debug=True)