# DeleteNotificationResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from ha_sdk_python.models.delete_notification_response_content import DeleteNotificationResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteNotificationResponseContent from a JSON string
delete_notification_response_content_instance = DeleteNotificationResponseContent.from_json(json)
# print the JSON string representation of the object
print(DeleteNotificationResponseContent.to_json())

# convert the object into a dict
delete_notification_response_content_dict = delete_notification_response_content_instance.to_dict()
# create an instance of DeleteNotificationResponseContent from a dict
delete_notification_response_content_from_dict = DeleteNotificationResponseContent.from_dict(delete_notification_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


