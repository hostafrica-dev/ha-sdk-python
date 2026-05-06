# UserChangePasswordDetails

Detailed information about password change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password_changed** | **bool** | Whether the password was changed successfully | 
**sessions_revoked** | **int** | Number of active sessions that were revoked | 
**requires_relogin** | **bool** | Whether the user needs to login again | 

## Example

```python
from hostafrica_sdk_python.models.user_change_password_details import UserChangePasswordDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UserChangePasswordDetails from a JSON string
user_change_password_details_instance = UserChangePasswordDetails.from_json(json)
# print the JSON string representation of the object
print(UserChangePasswordDetails.to_json())

# convert the object into a dict
user_change_password_details_dict = user_change_password_details_instance.to_dict()
# create an instance of UserChangePasswordDetails from a dict
user_change_password_details_from_dict = UserChangePasswordDetails.from_dict(user_change_password_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


