# GetEncryptedPasswordRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**public_key** | **str** | PEM-encoded RSA public key only (never the private key). Accepts SPKI (&#x60;-----BEGIN PUBLIC KEY-----&#x60;) or PKCS#1 (&#x60;-----BEGIN RSA PUBLIC KEY-----&#x60;). Must be exactly 4096-bit. Used with RSA-OAEP and SHA-256 to encrypt the password. | 

## Example

```python
from ha_sdk_python.models.get_encrypted_password_request_content import GetEncryptedPasswordRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncryptedPasswordRequestContent from a JSON string
get_encrypted_password_request_content_instance = GetEncryptedPasswordRequestContent.from_json(json)
# print the JSON string representation of the object
print(GetEncryptedPasswordRequestContent.to_json())

# convert the object into a dict
get_encrypted_password_request_content_dict = get_encrypted_password_request_content_instance.to_dict()
# create an instance of GetEncryptedPasswordRequestContent from a dict
get_encrypted_password_request_content_from_dict = GetEncryptedPasswordRequestContent.from_dict(get_encrypted_password_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


