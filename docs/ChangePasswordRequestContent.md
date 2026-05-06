# ChangePasswordRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**password** | **str** | New root password for the VPS | 

## Example

```python
from hostafrica_sdk_python.models.change_password_request_content import ChangePasswordRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of ChangePasswordRequestContent from a JSON string
change_password_request_content_instance = ChangePasswordRequestContent.from_json(json)
# print the JSON string representation of the object
print(ChangePasswordRequestContent.to_json())

# convert the object into a dict
change_password_request_content_dict = change_password_request_content_instance.to_dict()
# create an instance of ChangePasswordRequestContent from a dict
change_password_request_content_from_dict = ChangePasswordRequestContent.from_dict(change_password_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


