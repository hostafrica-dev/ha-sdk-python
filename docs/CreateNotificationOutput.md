# CreateNotificationOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**NotificationCreateResponseData**](NotificationCreateResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.create_notification_output import CreateNotificationOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNotificationOutput from a JSON string
create_notification_output_instance = CreateNotificationOutput.from_json(json)
# print the JSON string representation of the object
print(CreateNotificationOutput.to_json())

# convert the object into a dict
create_notification_output_dict = create_notification_output_instance.to_dict()
# create an instance of CreateNotificationOutput from a dict
create_notification_output_from_dict = CreateNotificationOutput.from_dict(create_notification_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


