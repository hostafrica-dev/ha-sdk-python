# UserChangePasswordResponseData

Response data for user change password operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether the operation was successful | 
**message** | **str** | Status message indicating the result | 
**data** | [**UserChangePasswordDetails**](UserChangePasswordDetails.md) |  | 

## Example

```python
from ha_sdk_python.models.user_change_password_response_data import UserChangePasswordResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UserChangePasswordResponseData from a JSON string
user_change_password_response_data_instance = UserChangePasswordResponseData.from_json(json)
# print the JSON string representation of the object
print(UserChangePasswordResponseData.to_json())

# convert the object into a dict
user_change_password_response_data_dict = user_change_password_response_data_instance.to_dict()
# create an instance of UserChangePasswordResponseData from a dict
user_change_password_response_data_from_dict = UserChangePasswordResponseData.from_dict(user_change_password_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


