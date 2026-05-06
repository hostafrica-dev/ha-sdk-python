# ListBackupsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**ServiceBackupsResponseData**](ServiceBackupsResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.list_backups_output import ListBackupsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ListBackupsOutput from a JSON string
list_backups_output_instance = ListBackupsOutput.from_json(json)
# print the JSON string representation of the object
print(ListBackupsOutput.to_json())

# convert the object into a dict
list_backups_output_dict = list_backups_output_instance.to_dict()
# create an instance of ListBackupsOutput from a dict
list_backups_output_from_dict = ListBackupsOutput.from_dict(list_backups_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


