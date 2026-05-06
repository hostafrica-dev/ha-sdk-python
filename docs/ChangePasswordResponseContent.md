# ChangePasswordResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.change_password_response_content import ChangePasswordResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of ChangePasswordResponseContent from a JSON string
change_password_response_content_instance = ChangePasswordResponseContent.from_json(json)
# print the JSON string representation of the object
print(ChangePasswordResponseContent.to_json())

# convert the object into a dict
change_password_response_content_dict = change_password_response_content_instance.to_dict()
# create an instance of ChangePasswordResponseContent from a dict
change_password_response_content_from_dict = ChangePasswordResponseContent.from_dict(change_password_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


