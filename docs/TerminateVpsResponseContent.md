# TerminateVpsResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.terminate_vps_response_content import TerminateVpsResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of TerminateVpsResponseContent from a JSON string
terminate_vps_response_content_instance = TerminateVpsResponseContent.from_json(json)
# print the JSON string representation of the object
print(TerminateVpsResponseContent.to_json())

# convert the object into a dict
terminate_vps_response_content_dict = terminate_vps_response_content_instance.to_dict()
# create an instance of TerminateVpsResponseContent from a dict
terminate_vps_response_content_from_dict = TerminateVpsResponseContent.from_dict(terminate_vps_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


