# GetEncryptedPasswordResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**EncryptedPasswordResponseData**](EncryptedPasswordResponseData.md) |  | 

## Example

```python
from ha_sdk_python.models.get_encrypted_password_response_content import GetEncryptedPasswordResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncryptedPasswordResponseContent from a JSON string
get_encrypted_password_response_content_instance = GetEncryptedPasswordResponseContent.from_json(json)
# print the JSON string representation of the object
print(GetEncryptedPasswordResponseContent.to_json())

# convert the object into a dict
get_encrypted_password_response_content_dict = get_encrypted_password_response_content_instance.to_dict()
# create an instance of GetEncryptedPasswordResponseContent from a dict
get_encrypted_password_response_content_from_dict = GetEncryptedPasswordResponseContent.from_dict(get_encrypted_password_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


