# ModifyPrivateNameserverData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**nameserver** | **str** | Existing nameserver hostname that was modified | [optional] 
**new_nameserver** | **str** | New hostname when a rename was requested | [optional] 
**old_ip_address** | **str** | Previous glue IP when supplied | [optional] 
**new_ip_address** | **str** | New glue IP when supplied | [optional] 

## Example

```python
from ha_sdk_python.models.modify_private_nameserver_data import ModifyPrivateNameserverData

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyPrivateNameserverData from a JSON string
modify_private_nameserver_data_instance = ModifyPrivateNameserverData.from_json(json)
# print the JSON string representation of the object
print(ModifyPrivateNameserverData.to_json())

# convert the object into a dict
modify_private_nameserver_data_dict = modify_private_nameserver_data_instance.to_dict()
# create an instance of ModifyPrivateNameserverData from a dict
modify_private_nameserver_data_from_dict = ModifyPrivateNameserverData.from_dict(modify_private_nameserver_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


