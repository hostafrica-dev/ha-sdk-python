# EncryptedPasswordResponseData

Response data for get-encrypted-password

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Username for VPS access (plaintext) | 
**password** | **str** | Base64-encoded ciphertext of the VPS password. Produced with RSA-OAEP (SHA-256) and the request public_key. Decode from base64, then decrypt with the matching private key via openssl pkeyutl -decrypt -pkeyopt rsa_padding_mode:oaep -pkeyopt rsa_oaep_md:sha256 -pkeyopt rsa_mgf1_md:sha256. | 
**encryption** | [**PasswordEncryptionInfo**](PasswordEncryptionInfo.md) |  | 

## Example

```python
from ha_sdk_python.models.encrypted_password_response_data import EncryptedPasswordResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptedPasswordResponseData from a JSON string
encrypted_password_response_data_instance = EncryptedPasswordResponseData.from_json(json)
# print the JSON string representation of the object
print(EncryptedPasswordResponseData.to_json())

# convert the object into a dict
encrypted_password_response_data_dict = encrypted_password_response_data_instance.to_dict()
# create an instance of EncryptedPasswordResponseData from a dict
encrypted_password_response_data_from_dict = EncryptedPasswordResponseData.from_dict(encrypted_password_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


