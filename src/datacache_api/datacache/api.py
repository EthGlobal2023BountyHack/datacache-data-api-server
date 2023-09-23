import os
import traceback
import asyncio
import json

from airstack.execute_query import AirstackClient

airstack_client = AirstackClient(api_key=os.getenv("AIRSTACK_APIKEY"))

async def airstack_query(query, variables, limit):
    res = list()
    execute_query_client = airstack_client.create_execute_query_object(query=query, variables=variables)
    query_response = await execute_query_client.execute_paginated_query()
    res.append(query_response.data)
    page = 1
    while query_response.has_next_page and page < limit:
        page += 1
        query_response = await query_response.get_next_page
        res.append(query_response.data)
    return res

async def test_airstack():
    try:
        query = """
        query MyQuery {
            Ethereum: NFTSaleTransactions(
                input: {filter: {nfts: {tokenAddress: {_eq: "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D"}}}, blockchain: ethereum, limit: 50}
            ) {
                NFTSaleTransaction {
                to {
                    identity
                    socials {
                    profileName
                    dappName
                    }
                }
                paymentAmountInUSDC
                }
                pageInfo {
                nextCursor
                prevCursor
                }
            }
            }
        """
        variables = dict()
        execute_query_client = airstack_client.create_execute_query_object(query=query, variables=variables)
        query_response = await execute_query_client.execute_paginated_query()
        print("error", query_response.error)
        print("data ", json.dumps(query_response.data))
        if query_response.has_next_page: 
            query_response = await query_response.get_next_page
            print("page 2 data ", json.dumps(query_response.data))
    except:
        print(traceback.format_exc())

if __name__ == "__main__":
    asyncio.run(test_airstack())
