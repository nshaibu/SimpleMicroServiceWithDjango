# SimpleMicroServiceWithDjango
Two django apps(setter, getter) communicate via a service broker(redis) using the producer-consumer model. The app `setter` set data and the app `getter` comsumes the data.

## Build
Clone the project and change to the root of the project. Then run the command below to build it:
```
docker-compose up
```

## Setter App
* Endpoint: ```http://127.0.0.1:8120/setter/set/values/```
* Request Type: ```POST```
* DATA: ```{key: value}```

#### Using `Curl`:
Run the command below to set the key `hello` to the value `world`.
```
curl  -X POST "http://127.0.0.1:8120/setter/set/values/" -d '{"hello": "Hello World"}'
```

## Getter App
* Endpoint: ```http://127.0.0.1:8000/getter/get/<key:string>/```
* Request Type: ```GET```
* DATA: ```Key```

#### Using `Curl`:
Run the command below the get the value of key `hello`.
```
curl http://127.0.0.1:8000/getter/get/hello/
```

