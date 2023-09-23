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
