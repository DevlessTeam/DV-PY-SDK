DevlessTeam/DV-PY-SDK)
## Install

# DV-PY-SDK
Official Devless py sdk

# Getting started 

### To connect to the Devless instance 

```


devless = Sdk("http://example.com", "1234567abcdefghijklmnopqrst");

```
### To add data to table 

```
data = {"name":"edmond"}
results = devless.addData('service_name', 'service_table', data)
print results

```

### To query data from the Devless instance 

```
results = devless.getData('service_name','service_table')
print results

```
### Also you may filter your query with : 

``size`` : determine the number of results to return 

``` eg: results = devless.size(3).getData('service_name', 'service_table')

``offset`` : Set step in data data to be sent back 

## NB: This is to be used in combination with size

`` eg: results = devless.offset(2).size(6).getData('service_name', 'service_table') ```

`` where `` : Get data based where a key matches a certain value 

``` eg: results = devless.where('name', 'edmond').getData('service_name', 'service_table') ```

``orderBy`` : Order incoming results in descending order based on a key 

`` eg: results = devless.orderBy('name').getData('service_name', 'service_table') ``


### To update data to table 

```
results = devless.where('id',1).updateData('service_name', 'service_table', {'name':'edmond'})

print results 

```

### To delete data from a Devless instance 

```
results = devless.where('id',1).deleteData('service_name','service_table')

```

## Make a call to an Action Class 

```
results = devless.call('service_name','method_name', {})

print results

```

## Authenticating with a Devless instance

```
token = devless.call('devless','login', {'email':'k@gmail.com', 'password':'password'});

devless.setUserToken(token['payload']['result']);

```



