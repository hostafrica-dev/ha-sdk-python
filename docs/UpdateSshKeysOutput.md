# UpdateSshKeysOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.update_ssh_keys_output import UpdateSshKeysOutput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSshKeysOutput from a JSON string
update_ssh_keys_output_instance = UpdateSshKeysOutput.from_json(json)
# print the JSON string representation of the object
print(UpdateSshKeysOutput.to_json())

# convert the object into a dict
update_ssh_keys_output_dict = update_ssh_keys_output_instance.to_dict()
# create an instance of UpdateSshKeysOutput from a dict
update_ssh_keys_output_from_dict = UpdateSshKeysOutput.from_dict(update_ssh_keys_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


