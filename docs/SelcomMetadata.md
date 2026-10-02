# SelcomMetadata

Selcom alt-gateway payment details included on an invoice when configured

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Due amount formatted for display (e.g. \&quot;TZS 29,000.00\&quot;). Non-TZS amounts are converted using the WHMCS currency rate. | 
**pesa_account** | **str** | Selcom Pesa account: 5-digit padded client id plus 6-digit padded invoice id | 
**mobile_reference** | **str** | Mobile payment reference: 61107370 plus the same padded client and invoice ids | 
**ussd_code** | **str** | USSD shortcode for Selcom (always *150*50*1#) | 
**instructions** | **str** | WHMCS Selcom alt-gateway instructions HTML with placeholders filled | 

## Example

```python
from ha_sdk_python.models.selcom_metadata import SelcomMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SelcomMetadata from a JSON string
selcom_metadata_instance = SelcomMetadata.from_json(json)
# print the JSON string representation of the object
print(SelcomMetadata.to_json())

# convert the object into a dict
selcom_metadata_dict = selcom_metadata_instance.to_dict()
# create an instance of SelcomMetadata from a dict
selcom_metadata_from_dict = SelcomMetadata.from_dict(selcom_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


