# CancelVpsResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsCancelResponseData**](VpsCancelResponseData.md) |  | 

## Example

```python
from ha_sdk_python.models.cancel_vps_response_content import CancelVpsResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of CancelVpsResponseContent from a JSON string
cancel_vps_response_content_instance = CancelVpsResponseContent.from_json(json)
# print the JSON string representation of the object
print(CancelVpsResponseContent.to_json())

# convert the object into a dict
cancel_vps_response_content_dict = cancel_vps_response_content_instance.to_dict()
# create an instance of CancelVpsResponseContent from a dict
cancel_vps_response_content_from_dict = CancelVpsResponseContent.from_dict(cancel_vps_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


