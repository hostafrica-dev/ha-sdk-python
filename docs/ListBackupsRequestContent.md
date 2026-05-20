# ListBackupsRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 

## Example

```python
from ha_sdk_python.models.list_backups_request_content import ListBackupsRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of ListBackupsRequestContent from a JSON string
list_backups_request_content_instance = ListBackupsRequestContent.from_json(json)
# print the JSON string representation of the object
print(ListBackupsRequestContent.to_json())

# convert the object into a dict
list_backups_request_content_dict = list_backups_request_content_instance.to_dict()
# create an instance of ListBackupsRequestContent from a dict
list_backups_request_content_from_dict = ListBackupsRequestContent.from_dict(list_backups_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


