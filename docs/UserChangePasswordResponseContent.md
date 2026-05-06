# UserChangePasswordResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**UserChangePasswordResponseData**](UserChangePasswordResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.user_change_password_response_content import UserChangePasswordResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of UserChangePasswordResponseContent from a JSON string
user_change_password_response_content_instance = UserChangePasswordResponseContent.from_json(json)
# print the JSON string representation of the object
print(UserChangePasswordResponseContent.to_json())

# convert the object into a dict
user_change_password_response_content_dict = user_change_password_response_content_instance.to_dict()
# create an instance of UserChangePasswordResponseContent from a dict
user_change_password_response_content_from_dict = UserChangePasswordResponseContent.from_dict(user_change_password_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


