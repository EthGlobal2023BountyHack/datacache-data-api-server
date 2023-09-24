from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import os

def search_thegraph(url, query):
  transport = RequestsHTTPTransport(
      url=url.replace("[api-key]", os.getenv("THE_GRAPH_API_KEY")),
      use_json=True,
  )
  client = Client(
      transport=transport,
      fetch_schema_from_transport=True,
  )
  query = gql(query)
  return client.execute(query)

