# UpdateNotificationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**notification_id** | **int** | Notification ID to update | 
**name** | **str** | Name/title for the notification | [optional] 
**status** | [**NotificationStatus**](NotificationStatus.md) |  | [optional] 
**notification_interval** | **int** | Notification interval in minutes (must be &gt; 0) | [optional] 
**data_timeframe** | **int** | Data timeframe in minutes (must be &gt; 0) | [optional] 
**exceed_all** | **bool** | Whether all thresholds must be exceeded (true) or any one (false) | [optional] 
**email_address** | **List[str]** | Email addresses for notifications (comma-separated string or array) | [optional] 
**cpu_usage** | **int** | CPU usage threshold percentage (0-100) | [optional] 
**memory_usage** | **int** | Memory usage threshold percentage (0-100) | [optional] 
**network_traffic** | **int** | Network traffic threshold percentage (0-100) | [optional] 
**disk_read** | **int** | Disk read threshold percentage (0-100) | [optional] 
**disk_write** | **int** | Disk write threshold percentage (0-100) | [optional] 

## Example

```python
from hostafrica_sdk_python.models.update_notification_input import UpdateNotificationInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateNotificationInput from a JSON string
update_notification_input_instance = UpdateNotificationInput.from_json(json)
# print the JSON string representation of the object
print(UpdateNotificationInput.to_json())

# convert the object into a dict
update_notification_input_dict = update_notification_input_instance.to_dict()
# create an instance of UpdateNotificationInput from a dict
update_notification_input_from_dict = UpdateNotificationInput.from_dict(update_notification_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


