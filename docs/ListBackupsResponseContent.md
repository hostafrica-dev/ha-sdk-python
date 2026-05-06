# ListBackupsResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**ServiceBackupsResponseData**](ServiceBackupsResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.list_backups_response_content import ListBackupsResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of ListBackupsResponseContent from a JSON string
list_backups_response_content_instance = ListBackupsResponseContent.from_json(json)
# print the JSON string representation of the object
print(ListBackupsResponseContent.to_json())

# convert the object into a dict
list_backups_response_content_dict = list_backups_response_content_instance.to_dict()
# create an instance of ListBackupsResponseContent from a dict
list_backups_response_content_from_dict = ListBackupsResponseContent.from_dict(list_backups_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


