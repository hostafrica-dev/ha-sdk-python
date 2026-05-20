# ListOrdersResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**ListOrdersResponseData**](ListOrdersResponseData.md) |  | 

## Example

```python
from ha_sdk_python.models.list_orders_response_content import ListOrdersResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of ListOrdersResponseContent from a JSON string
list_orders_response_content_instance = ListOrdersResponseContent.from_json(json)
# print the JSON string representation of the object
print(ListOrdersResponseContent.to_json())

# convert the object into a dict
list_orders_response_content_dict = list_orders_response_content_instance.to_dict()
# create an instance of ListOrdersResponseContent from a dict
list_orders_response_content_from_dict = ListOrdersResponseContent.from_dict(list_orders_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


