# RdnsPool

A subnet pool entry within an available rDNS item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool** | **str** | Network address of the pool | 
**mask** | **int** | CIDR prefix length | 

## Example

```python
from ha_sdk_python.models.rdns_pool import RdnsPool

# TODO update the JSON string below
json = "{}"
# create an instance of RdnsPool from a JSON string
rdns_pool_instance = RdnsPool.from_json(json)
# print the JSON string representation of the object
print(RdnsPool.to_json())

# convert the object into a dict
rdns_pool_dict = rdns_pool_instance.to_dict()
# create an instance of RdnsPool from a dict
rdns_pool_from_dict = RdnsPool.from_dict(rdns_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


