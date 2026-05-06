# Notification

Individual notification item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Notification ID | 
**hosting_id** | **int** | Hosting/service ID | 
**name** | **str** | Notification name/title | 
**condition_key** | **str** | Condition key (cpu_usage, memory_usage, network_traffic, disk_read, disk_write) | 
**threshold** | **int** | Threshold value | 
**period** | **int** | Period in minutes | 
**timeframe** | **int** | Timeframe in minutes | 
**enabled** | **bool** | Whether the notification is enabled | [optional] 
**created_at** | **str** | Creation timestamp | [optional] 
**updated_at** | **str** | Last updated timestamp | [optional] 

## Example

```python
from hostafrica_sdk_python.models.notification import Notification

# TODO update the JSON string below
json = "{}"
# create an instance of Notification from a JSON string
notification_instance = Notification.from_json(json)
# print the JSON string representation of the object
print(Notification.to_json())

# convert the object into a dict
notification_dict = notification_instance.to_dict()
# create an instance of Notification from a dict
notification_from_dict = Notification.from_dict(notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


