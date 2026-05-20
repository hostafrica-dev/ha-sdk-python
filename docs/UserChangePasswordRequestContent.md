# UserChangePasswordRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_password** | **str** | Current password | 
**password** | **str** | New password | 
**confirm_password** | **str** | Confirm new password (must match password) | 

## Example

```python
from ha_sdk_python.models.user_change_password_request_content import UserChangePasswordRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of UserChangePasswordRequestContent from a JSON string
user_change_password_request_content_instance = UserChangePasswordRequestContent.from_json(json)
# print the JSON string representation of the object
print(UserChangePasswordRequestContent.to_json())

# convert the object into a dict
user_change_password_request_content_dict = user_change_password_request_content_instance.to_dict()
# create an instance of UserChangePasswordRequestContent from a dict
user_change_password_request_content_from_dict = UserChangePasswordRequestContent.from_dict(user_change_password_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


