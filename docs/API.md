test env: https://datacache.ecalculator.pro/

success response: {'status': 0, 'message': 'Success'}
error response: status !=0 with the error message
{'status': 1, 'message': 'Invalid data'}

# 1. Add wallet

* add an address and with generate tags asynchronous

* Route: /api/wallet/add/
* POST
* Params: address

# 2. User tags
get tag list from an address
* Route: /api/wallet/tag/list/
* GET
* Params: address
https://datacache.ecalculator.pro/api/wallet/tag/list/?address=0x75e89d5979e4f6fba9f97c104c2f0afb3f1dcb88

# 3. Add tag to wallet

* Route: /api/wallet/add/
* POST
* Params: address, tag(id)
* tag can be added in admin

* 4. Tag list 
* Route /api/tag/list/
No Params
Result
{"status": 0, "message": "Success", "list": [{"id": 2, "name": "BigWhale Of ApeCoin"}, {"id": 3, "name": "XMTP"}, {"id": 4, "name": "ERC6551 Supporter"}]}

* 5. Search Wallet Addresses by tags
* Route /api/wallet/tag/search/
* Params: tags(id), use , to split. 2,4 means Tag(2) and Tag(4)
*         condition(Optional, default or), or|and, search users by tags
* /api/wallet/tag/search/?tags=2,4&condition=and