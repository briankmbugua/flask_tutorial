from flask import Flask

app = Flask('__main__')

@app.route('/')
def index():
    return 'Welcomee!'


"""You can use the test_request_context method to create a request context"""
# Using test_request_context method without using a context manager
from flask import request

request_context = app.test_request_context()
request_context.push()

print(f"the http method being used is {request.method}")
print(f"the path being used is {request.path}")

request_context.pop()


"""After using request_context.pop() the below print statements won't work and will generate the following error
raise RuntimeError(unbound_message) from None
RuntimeError: Working outside of request context.

This typically means that you attempted to use functionality that needed
an active HTTP request.  """
# print(f"the http method being used is {request.method}")
# print(f"the path being used is {request.path}")

# With a context manager
with app.test_request_context():
    print(f"from context manager {request.method}")
    print(f"from context manager {request.path}")

"""test_request_context is typically used during testing when you want to use request data without the overhead of a full request.The most common time to run into issues with the Application and Request context is when your app is under test."""





if __name__ == "__main__":
    app.run(debug=False)