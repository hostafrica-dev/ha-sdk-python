# PrivateNameserverMutationData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**nameserver** | **str** | Child nameserver hostname | [optional] 
**ip_address** | **str** | Glue IP address when returned (register) | [optional] 

## Example

```python
from ha_sdk_python.models.private_nameserver_mutation_data import PrivateNameserverMutationData

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateNameserverMutationData from a JSON string
private_nameserver_mutation_data_instance = PrivateNameserverMutationData.from_json(json)
# print the JSON string representation of the object
print(PrivateNameserverMutationData.to_json())

# convert the object into a dict
private_nameserver_mutation_data_dict = private_nameserver_mutation_data_instance.to_dict()
# create an instance of PrivateNameserverMutationData from a dict
private_nameserver_mutation_data_from_dict = PrivateNameserverMutationData.from_dict(private_nameserver_mutation_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


