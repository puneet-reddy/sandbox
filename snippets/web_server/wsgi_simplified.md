#First, the server starts and loads an ‘application’ callable provided by your Web framework/application
#Then, the server reads a request
#Then, the server parses it
#Then, it builds an ‘environ’ dictionary using the request data
#Then, it calls the ‘application’ callable with the ‘environ’ dictionary and a #‘start_response’ callable as parameters and gets back a response body.
#Then, the server constructs an HTTP response using the data returned by the call to the ‘application’ object and the status and response headers set by the ‘start_response’ callable.
#And finally, the server transmits the HTTP response back to the client