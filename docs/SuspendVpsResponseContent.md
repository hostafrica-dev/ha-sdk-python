# SuspendVpsResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.suspend_vps_response_content import SuspendVpsResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of SuspendVpsResponseContent from a JSON string
suspend_vps_response_content_instance = SuspendVpsResponseContent.from_json(json)
# print the JSON string representation of the object
print(SuspendVpsResponseContent.to_json())

# convert the object into a dict
suspend_vps_response_content_dict = suspend_vps_response_content_instance.to_dict()
# create an instance of SuspendVpsResponseContent from a dict
suspend_vps_response_content_from_dict = SuspendVpsResponseContent.from_dict(suspend_vps_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


