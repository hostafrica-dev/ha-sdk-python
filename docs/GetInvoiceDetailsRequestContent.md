# GetInvoiceDetailsRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** | Invoice ID - must be sent as a string | 

## Example

```python
from ha_sdk_python.models.get_invoice_details_request_content import GetInvoiceDetailsRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of GetInvoiceDetailsRequestContent from a JSON string
get_invoice_details_request_content_instance = GetInvoiceDetailsRequestContent.from_json(json)
# print the JSON string representation of the object
print(GetInvoiceDetailsRequestContent.to_json())

# convert the object into a dict
get_invoice_details_request_content_dict = get_invoice_details_request_content_instance.to_dict()
# create an instance of GetInvoiceDetailsRequestContent from a dict
get_invoice_details_request_content_from_dict = GetInvoiceDetailsRequestContent.from_dict(get_invoice_details_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


