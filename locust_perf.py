# Create a locust performance test script
#
# Usage: locust -f perf_test.py --processes <N>

from locust import HttpUser, task, between
import os, json

class GbgUser(HttpUser):

    # Wait time between requests
    wait_time = between(1, 5)

    # Host
    host = "https://gbg.eu-central-1.aws.api.imply.io/v1/projects/1f975a04-9cef-461f-9864-a706710bb699"

    # API key
    apikey = os.getenv("POLARIS_API_KEY")

    # Create a function to check the number of queries in the queries.json file
    def on_start(self):
            with open("./queries.json") as f:
                queries = json.load(f)
                return len(queries["queries"])

    # Create a function to read from the queries.json file
    def query(self, query_id):
        with open("./queries.json") as f:
            queries = json.load(f)
        return queries["queries"][query_id]

    # Create tasks
    @task
    def query1(self):

        # Check the number of queries in the queries.json file
        num_queries = self.on_start()

        # Loop through the queries in the queries.json file
        for query_id in range(0, num_queries):
            query = self.query(query_id)
            payload = {
                "query" : query,
                "context" : {
                    "queryId": f"ajith-gbg-query-{query_id}"
                }
            }

            # Set the headers
            self.client.headers = { 'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': f'Basic {self.apikey}'}

            # Send the request
            response = self.client.post("/query/sql", json=payload)

            # print the response only if status code is not 200
            if response.status_code != 200:
                print("Response: " + response.text)