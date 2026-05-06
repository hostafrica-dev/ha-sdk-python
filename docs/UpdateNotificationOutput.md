# UpdateNotificationOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**NotificationCreateResponseData**](NotificationCreateResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.update_notification_output import UpdateNotificationOutput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateNotificationOutput from a JSON string
update_notification_output_instance = UpdateNotificationOutput.from_json(json)
# print the JSON string representation of the object
print(UpdateNotificationOutput.to_json())

# convert the object into a dict
update_notification_output_dict = update_notification_output_instance.to_dict()
# create an instance of UpdateNotificationOutput from a dict
update_notification_output_from_dict = UpdateNotificationOutput.from_dict(update_notification_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


