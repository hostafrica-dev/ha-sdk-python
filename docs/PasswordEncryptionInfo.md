# PasswordEncryptionInfo

Encryption metadata for an RSA-OAEP encrypted password

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** | Asymmetric encryption algorithm. Always \&quot;RSA-OAEP\&quot;. | 
**hash** | **str** | OAEP hash / MGF1 hash function. Always \&quot;SHA-256\&quot;. | 
**key_size** | **int** | RSA modulus size in bits. Always 4096. | 
**encoding** | **str** | Encoding of the password ciphertext field. Always \&quot;base64\&quot; (standard alphabet, not URL-safe). | 

## Example

```python
from ha_sdk_python.models.password_encryption_info import PasswordEncryptionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordEncryptionInfo from a JSON string
password_encryption_info_instance = PasswordEncryptionInfo.from_json(json)
# print the JSON string representation of the object
print(PasswordEncryptionInfo.to_json())

# convert the object into a dict
password_encryption_info_dict = password_encryption_info_instance.to_dict()
# create an instance of PasswordEncryptionInfo from a dict
password_encryption_info_from_dict = PasswordEncryptionInfo.from_dict(password_encryption_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


