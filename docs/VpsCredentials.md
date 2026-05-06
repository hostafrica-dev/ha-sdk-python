# VpsCredentials

VPS credentials

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Username for VPS access | 
**password** | **str** | Password for VPS access | 

## Example

```python
from hostafrica_sdk_python.models.vps_credentials import VpsCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of VpsCredentials from a JSON string
vps_credentials_instance = VpsCredentials.from_json(json)
# print the JSON string representation of the object
print(VpsCredentials.to_json())

# convert the object into a dict
vps_credentials_dict = vps_credentials_instance.to_dict()
# create an instance of VpsCredentials from a dict
vps_credentials_from_dict = VpsCredentials.from_dict(vps_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


