# StartVpsResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.start_vps_response_content import StartVpsResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of StartVpsResponseContent from a JSON string
start_vps_response_content_instance = StartVpsResponseContent.from_json(json)
# print the JSON string representation of the object
print(StartVpsResponseContent.to_json())

# convert the object into a dict
start_vps_response_content_dict = start_vps_response_content_instance.to_dict()
# create an instance of StartVpsResponseContent from a dict
start_vps_response_content_from_dict = StartVpsResponseContent.from_dict(start_vps_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


