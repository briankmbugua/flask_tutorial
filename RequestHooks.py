"""Sometimes it is useful to execute code before or after each request is processed.E.g at the start of every request it may be necessary to create a database connection or authenticate the user making the request.Instead of duplicating the code that does this in every view function, Flask gieves you the option common functions to be invoked before or after a request is dispatched to a view function."""
# before_first_request - Register a function to run before the first request is dispatched
# before_request - Register a function to run before each request
# after_request - Register a function to run after each request, if no unhandled exceptions occured.
# teardown-request - Register a function to run after each request, even if unhandled exceptions occurred.