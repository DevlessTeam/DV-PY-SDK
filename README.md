# Devless Python SDK
Allows you manage and administer your Devless service integrations in Python.

## Install

In your project python file, simply import the devless.py module

`import Devless` 


## Getting started 

### To connect to the Devless instance 

```python

devless = Sdk("http://example.com", "1234567abcdefghijklmnopqrst")

```

### To add data to table 

```python

data = {"name":"edmond"}
results = devless.add_data('service_name', 'service_table', data)
print results

```

### To query data from the Devless instance 

```python

results = devless.get_data('service_name','service_table')
print(results)

```
### Optional filters for your query : 

``size`` : determine the number of results to return, like this:

```python

results = devless.size(3).get_data('service_name', 'service_table')

```

``offset`` : Set step in data data to be sent back: 

#### NB: This is to be used in combination with size

```python

results = devless.offset(2).size(6).get_data('service_name', 'service_table') 

```

``where`` : Get data based where a key matches a certain value: 

```python

results = devless.where('name', 'edmond').get_data('service_name', 'service_table') 

```

``orderBy`` : Order incoming results in descending order based on a key 

```python

results = devless.orderBy('name').get_data('service_name', 'service_table') 

```


### To update data to table 

```python

results = devless.where('id',1).update_data('service_name', 'service_table', {'name':'edmond'})

print(results) 

```

### To delete data from a Devless instance 

```
results = devless.where('id',1).delete_data('service_name','service_table')

```

## Make a call to an Action Class 

```python

results = devless.call('service_name','method_name', {})

print(results)

```

## Authenticating with a Devless instance

```python

token = devless.call('devless','login', {'email':'k@gmail.com', 'password':'password'});

devless.set_user_token(token['payload']['result']);

```



