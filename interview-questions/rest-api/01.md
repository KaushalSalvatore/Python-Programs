#### Q-1 what is serializers ?

```bash
Django’s serialization framework provides a mechanism for “translating” Django models into other formats.
Serializers in Django REST Framework are responsible for converting objects into data types understandable by javascript and front-end frameworks. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data. The serializers in REST framework work very similarly to Django’s Form and ModelForm classes. The two major serializers that are most popularly used are ModelSerializer and HyperLinkedModelSerialzer.
```

#### Q-2 differance between PUT and PATCH request ?

```bash
PUT and PATCH requests are HTTP verbs and both relate to updating the resources at a location.
PUT is a method of modifying resources where the client sends data that updates the entire resource.
PATCH does partial update e.g. Fields that need to be updated by the client, only that field is updated without modifying the other field.
```

#### Q-3 differance beteen Put and post request ? 

```bash
PUT is best used when you are updating or replacing existing data on the server, while POST is best used when you are creating new data.
Remember that PUT is idempotent, while POST is not. PUT is also not safe, while POST is. Finally, PUT is generally not cacheable, while POST is usually cacheable.
```

#### Q-4 differance beteen SOAP and Rest API ?

```bash
SOAP stands for Simple Object Access Protocol and REST stands for Representational State Transfer.
SOAP uses only XML for exchanging information in its message format whereas REST is not restricted to XML and its the choice of implementer which Media-Type to use like XML, JSON, Plain-text. Moreover, REST can use SOAP protocol but SOAP cannot use REST.
```

#### Q-5 whats is CORS in web api ? 

```bash
Cross-origin resource sharing (CORS) is a browser security feature that restricts cross-origin HTTP requests that are initiated from scripts running in the browser.
```

#### Q-6 what is the concept of statelessness in rest API ? 

```bash
Statelessness means that every HTTP request happens in complete isolation
As per the REST{Representational “State” Transfer } architecture, the server does not store any information about the client-side on the server-side.
```

#### Q-7 is it posible to send the payload in get/delete method ?

```bash
A payload in API is the actual data pack that is sent with the GET method in HTTP.
The payload can be sent or received in various formats, including JSON.
There can be some client libraries that do not support the payload with these two methods.
It’s better not to include payload with these two methods.
```

#### Q-8 maximim payload size for post method ?

```bash
The POST method itself does not have any limit on the size of data.
```

#### Q-9 whats is the advantage of using restAPI in web APi ?

```bash
Lightweight
Independent
Scalable and flexible.
Statelessness
```

#### Q-10 what are the Restfull web services ?

```bash
REST or Representational State Transfer is an architectural style that can be applied to web services to create and enhance properties like performance, scalability, and modifiability. RESTful web services are generally highly scalable, light, and maintainable and are used to create APIs for web-based applications.
```


#### Q-11 what are the disadvantages of restfull web services ?

```bash
Security risks are also a concern, as URIs and HTTP methods can be intercepted or manipulated by malicious actors. Finally, tight coupling between the client and the server can occur due to the need for both parties to agree on the format and structure of requests and responses.
```


#### Q-12 what are the payloads in terms of restfull web servics  ?

```bash
The payload of an API is the data you are interested in transporting to the server when you make an API request. Simply put, it is the body of your HTTP request and response message.
```


#### Q-13 can we use a get/post method instend of put method to create a resource ?

```bash
Since both can be used to submit data, you can use either POST or PUT to create or update a resource.
```


#### Q-14 what are the main componets of Http Request ?

```bash
 request line, headers and message body.
```


#### Q-15 HTTP status code in web services ?

```bash
OK 200
CREATED 201
Accepted 202
No Response 204
Bad request 400
Unauthorized 401
PaymentRequired 402
Forbidden 403
Not found 404
Internal Error 500
```