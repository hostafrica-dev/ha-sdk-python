# CancelVpsRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**type** | [**VpsCancelType**](VpsCancelType.md) |  | [optional] 

## Example

```python
from ha_sdk_python.models.cancel_vps_request_content import CancelVpsRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of CancelVpsRequestContent from a JSON string
cancel_vps_request_content_instance = CancelVpsRequestContent.from_json(json)
# print the JSON string representation of the object
print(CancelVpsRequestContent.to_json())

# convert the object into a dict
cancel_vps_request_content_dict = cancel_vps_request_content_instance.to_dict()
# create an instance of CancelVpsRequestContent from a dict
cancel_vps_request_content_from_dict = CancelVpsRequestContent.from_dict(cancel_vps_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


