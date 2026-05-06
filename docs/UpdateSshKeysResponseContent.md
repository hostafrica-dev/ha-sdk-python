# UpdateSshKeysResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.update_ssh_keys_response_content import UpdateSshKeysResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSshKeysResponseContent from a JSON string
update_ssh_keys_response_content_instance = UpdateSshKeysResponseContent.from_json(json)
# print the JSON string representation of the object
print(UpdateSshKeysResponseContent.to_json())

# convert the object into a dict
update_ssh_keys_response_content_dict = update_ssh_keys_response_content_instance.to_dict()
# create an instance of UpdateSshKeysResponseContent from a dict
update_ssh_keys_response_content_from_dict = UpdateSshKeysResponseContent.from_dict(update_ssh_keys_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


