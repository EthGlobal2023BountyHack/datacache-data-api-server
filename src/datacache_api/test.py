import json
from jsonpath_ng import jsonpath, parse

ex = "$.Ethereum.TokenBalance[*].owner.identity"
data = {"Ethereum":{"TokenBalance":[{"owner":{"identity":"0x0d6754e153231cd05062b5cebbe2bd397e7edeb9"},"amount":"200000000000000000000","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0x4e8ca5cb9fca486d09ee7c8dbbfe99ac96ec1982"},"amount":"681265000000000000000000","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0x787b8840100d9baadd7463f4a73b5ba73b00c6ca"},"amount":"2238574856172723497804","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0x28c6c06298d514db089934071355e5743bf21d60"},"amount":"4437419969030208035467312","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0x7b0380f4066e27030b8cc15d84d10fdf644f8d38"},"amount":"254270282833586359610","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0xfb19ffd1ff9316b7f5bba076ef4b78e4bbedf4e1"},"amount":"532204000589348296918","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0x5e4bb4c092e2441b6aecb4db4e73c47086a19478"},"amount":"1782053368733269517312","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0x2cccd9fedeabbf6c5112658a0855ba77b864f2db"},"amount":"178925000000000000000","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0xef8801eaf234ff82801821ffe2d78d60a0237f97"},"amount":"148961345116431882076247","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0x389505f098a29a994a3ed0e674f07cd451dde42c"},"amount":"3839527782111934510528","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0x87286ca4d761f4ac52039a8f5be9dd636c27dccf"},"amount":"107215956141441782160","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43"},"amount":"2043020675774865931184071","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0x0ab0b70f1ba55343c3412f60d6b7626642cf0911"},"amount":"750682468181028490067","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0xfdbda90772d62b652cfe0a96e3192e8062e1b0ef"},"amount":"874517760970000000000","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0x6cc5f688a315f3dc28a7781717a9a798a59fda7b"},"amount":"3891176646828630755930629","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0xdfd5293d8e347dfe59e90efd55b2956a1343963d"},"amount":"871703404498550000000000","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0x21a31ee1afc51d94c2efccaa2092ad1028285549"},"amount":"706910510240520000000000","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0x8ef5359bcf3c9b990e122be31613572b1fa8b6bd"},"amount":"722446489400381954048","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0x130f4322e5838463ee460d5854f5d472cfc8f253"},"amount":"2394127336921725572006","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0x5954ab967bc958940b7eb73ee84797dc8a2afbb9"},"amount":"169796706484280229325362965","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0xf52459e8bc708d55400c167e0d77ed49641226d3"},"amount":"11392610648027615094472","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0x51c72848c68a965f66fa7a88855f9f7784502a7f"},"amount":"180530156427919047024","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0xac4b3dacb91461209ae9d41ec517c2b9cb1b7daf"},"amount":"785097287286985615157049","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0x5bdf85216ec1e38d6458c870992a69e38e03f7ef"},"amount":"389499799730741431000000","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0xa69babef1ca67a37ffaf7a485dfff3382056e78c"},"amount":"4968192442056910720123","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0xe75ef1ec029c71c9db0f968e389331609312aa22"},"amount":"41805000000000000000000","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0xa486a982fa71b46bd4d7c36058827bcae90787cc"},"amount":"13497167227125400248568","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0x0cfb5d82be2b949e8fa73a656df91821e2ad99fd"},"amount":"14360000000000000000000","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0x153321cff12c46a8b94b916ff33ddc684182583c"},"amount":"550861993239322395514","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0xb1e66855fd67f6e85f0f0fa38cd6fbabdf00923c"},"amount":"3845999242706780516939","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0xbe4d91dcf2cbfc4628eac91a6f3e32e6197542fc"},"amount":"1026040000000000000000","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0xe3fbac9456bde90d3990fbd14e796a4ef4468a71"},"amount":"945945945945945800000","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0xf1f7648f81f5219c36d75d24d33811f16b426dbe"},"amount":"2258929283229960551305967","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0x2d3a91b6a3dc90a7fbd0c449d0851f677964a094"},"amount":"555000000000000000000","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0xbb289bc97591f70d8216462df40ed713011b968a"},"amount":"19782413838866684927843","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0x6a04ddf3de778de8d9fc64fcf6fb826b03570738"},"amount":"2713362756485868411233","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0xb011eeaab8bf0c6de75510128da95498e4b7e67f"},"amount":"29239651689757209279438","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0xb3c839dbde6b96d37c56ee4f9dad3390d49310aa"},"amount":"19818894085209627367461","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0x6b75d8af000000e20b7a7ddf000ba900b4009a80"},"amount":"4186754174417480526765","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0x84fdaf5487ee50b81de4af4667e6258d7b5ddeaf"},"amount":"973684534029758652416","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0x74dec05e5b894b0efec69cdf6316971802a2f9a1"},"amount":"9806487271493741625517","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0x72e364f2abdc788b7e918bc238b21f109cd634d7"},"amount":"216029159977814287541306","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0x89f2ab029dcd11bd5a00ed6a77ccbe46315212e8"},"amount":"39955700000000000000000","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0x5d6aa3c283fc6a8af42a5a5494cfe744e7d503c2"},"amount":"197960000000000000000","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0xf60c2ea62edbfe808163751dd0d8693dcb30019c"},"amount":"295038515870622420586038","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0x48111e5b7d64615dbb8db8b2183d625f71ed99e3"},"amount":"224800809790000000000","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0xbb0cacfdcd4394a419b48eec4c57e2a89afa2015"},"amount":"219976854229941488878","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0x29488e5fd6bf9b3cc98a9d06a25204947cccbe4d"},"amount":"121113304316866756377","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0x974caa59e49682cda0ad2bbe82983419a2ecc400"},"amount":"19551673605344791180766","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"},{"owner":{"identity":"0xdb5485c85bd95f38f9def0ca85499ef67dc581c0"},"amount":"5992000000000000000000","tokenAddress":"0x4d224452801aced8b2f0aebe155379bb5d594381","tokenId":"","tokenType":"ERC20"}],"pageInfo":{"nextCursor":"eyJMYXN0VmFsdWVzTWFwIjp7Il9pZCI6eyJWYWx1ZSI6IjEweDRkMjI0NDUyODAxYWNlZDhiMmYwYWViZTE1NTM3OWJiNWQ1OTQzODEweGRiNTQ4NWM4NWJkOTVmMzhmOWRlZjBjYTg1NDk5ZWY2N2RjNTgxYzAiLCJEYXRhVHlwZSI6InN0cmluZyJ9LCJsYXN0VXBkYXRlZFRpbWVzdGFtcCI6eyJWYWx1ZSI6IjE2OTU0ODQ5MDciLCJEYXRhVHlwZSI6IkRhdGVUaW1lIn19LCJQYWdpbmF0aW9uRGlyZWN0aW9uIjoiTkVYVCJ9","prevCursor":""}}}
expression = parse(ex)

for match in expression.find(data):
    print(match.value)