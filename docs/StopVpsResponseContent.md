# StopVpsResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from ha_sdk_python.models.stop_vps_response_content import StopVpsResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of StopVpsResponseContent from a JSON string
stop_vps_response_content_instance = StopVpsResponseContent.from_json(json)
# print the JSON string representation of the object
print(StopVpsResponseContent.to_json())

# convert the object into a dict
stop_vps_response_content_dict = stop_vps_response_content_instance.to_dict()
# create an instance of StopVpsResponseContent from a dict
stop_vps_response_content_from_dict = StopVpsResponseContent.from_dict(stop_vps_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


