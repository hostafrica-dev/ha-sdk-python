# VpsSimpleActionResponseData

Standard response data for VPS power management operations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result of the operation | 

## Example

```python
from ha_sdk_python.models.vps_simple_action_response_data import VpsSimpleActionResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of VpsSimpleActionResponseData from a JSON string
vps_simple_action_response_data_instance = VpsSimpleActionResponseData.from_json(json)
# print the JSON string representation of the object
print(VpsSimpleActionResponseData.to_json())

# convert the object into a dict
vps_simple_action_response_data_dict = vps_simple_action_response_data_instance.to_dict()
# create an instance of VpsSimpleActionResponseData from a dict
vps_simple_action_response_data_from_dict = VpsSimpleActionResponseData.from_dict(vps_simple_action_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


