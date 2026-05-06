# UserChangePasswordInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_password** | **str** | Current password | 
**password** | **str** | New password | 
**confirm_password** | **str** | Confirm new password (must match password) | 

## Example

```python
from hostafrica_sdk_python.models.user_change_password_input import UserChangePasswordInput

# TODO update the JSON string below
json = "{}"
# create an instance of UserChangePasswordInput from a JSON string
user_change_password_input_instance = UserChangePasswordInput.from_json(json)
# print the JSON string representation of the object
print(UserChangePasswordInput.to_json())

# convert the object into a dict
user_change_password_input_dict = user_change_password_input_instance.to_dict()
# create an instance of UserChangePasswordInput from a dict
user_change_password_input_from_dict = UserChangePasswordInput.from_dict(user_change_password_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


