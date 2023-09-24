from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

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


@app.route('/gql', methods=['POST'])
def process_json():
    data = request.get_json()
    url = data['url']
    query = data['query']
    res = search_thegraph(url, query)
    return jsonify(res), 200

if __name__ == '__main__':
    app.run(debug=True, port=1234)




