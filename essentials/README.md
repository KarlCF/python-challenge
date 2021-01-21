# HTTP

HTTP stands for Hyper Text Transfer Protocol. WWW is about communication between web clients and servers. Communication between client computers and web servers is done by sending HTTP Requests and receiving HTTP Responses.

Principal HTTP methods:
  - GET
  - POST
  - PUT
  - DELETE

Principal HTTP Headers:
  - User-Agent
  - Content-Type
  - Authorization

Principal HTTP Response Header Field:
  - Content-Type

Query String
  - Whenever you need to get a content, using a simple filter
    - Example: https://www.google.com.br/search?q=python

Body
  - As the name suggests, the body of the response to the client's request


## Notes

* The difference between POST and PUT is that PUT requests are idempotent. That is, calling the same PUT request multiple times will always produce the same result. In contrast, calling a POST request repeatedly have side effects of creating the same resource multiple times.
* Extra reading:
  * [What is HTTP?](https://www.w3schools.com/whatis/whatis_http.asp)
  * [HTTP Basics - Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP)
  * [HTTP Request Methods](https://www.w3schools.com/tags/ref_httpmethods.asp)
  * [HTTP Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)
  * [HTTP Headers - Extra](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html)
  * [HTTP responses explained](https://www.tutorialspoint.com/http/http_responses.htm)
  * [Response Codes Cheat Sheet - !!!IMPORTANT!!!](https://cheatography.com/kstep/cheat-sheets/http-status-codes/)
  * [Inspect Element Tutorial](https://zapier.com/blog/inspect-element-tutorial/)

# JSON


JSON stands for JavaScript Object Notation

JSON is a lightweight format for storing and transporting data

JSON is often used when data is sent from a server to a web page

JSON is "self-describing" and easy to understand

JSON data is written as name/value pairs

Data types:
* Key can be:
  * string
* value can be:
  * string
  * number (not inside curly braces)
  * bool (not inside curly braces)
  * object
  * null (not inside curly braces)

Working with JSON:
* Serializing
  * It's the process of transforming objects into JSON
* Deserialize
  * It's the process of transforming JSON into objects

JSON objects are written inside curly braces 


``` json
{
	"name": "Karl de Castro Fonseca",
	"age": "29",
	"home-office": true,
	"programmer": null,
	"job": {
		"name": "Solutions Architect",
		"level": 4,
    "tasks": 
    [
			"Cloud Custodian Policies Creation",
			"Secrets management",
			"Automation",
			"Learning",
			"Training"
		]
	}
}

```

## Notes

* Extra reading:
  * [What is Json?](https://www.w3schools.com/whatis/whatis_json.asp)
* Resources:
  * [JSON Editor](http://jsoneditoronline.org/)
  * [JSON Lint](https://jsonlint.com/)
  * [Star Wars API](https://swapi.dev/)
    * [Documentation](https://swapi.dev/documentation)

# YAML



## Notes

