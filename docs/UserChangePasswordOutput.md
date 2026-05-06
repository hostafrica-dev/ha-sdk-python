# UserChangePasswordOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**UserChangePasswordResponseData**](UserChangePasswordResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.user_change_password_output import UserChangePasswordOutput

# TODO update the JSON string below
json = "{}"
# create an instance of UserChangePasswordOutput from a JSON string
user_change_password_output_instance = UserChangePasswordOutput.from_json(json)
# print the JSON string representation of the object
print(UserChangePasswordOutput.to_json())

# convert the object into a dict
user_change_password_output_dict = user_change_password_output_instance.to_dict()
# create an instance of UserChangePasswordOutput from a dict
user_change_password_output_from_dict = UserChangePasswordOutput.from_dict(user_change_password_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


