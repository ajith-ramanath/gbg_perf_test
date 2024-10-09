from locust import HttpUser, task, between
import calendar, os

class GbgUser(HttpUser):
    wait_time = between(1, 5)
    host = "https://gbg.eu-central-1.aws.api.imply.io/v1/projects/1f975a04-9cef-461f-9864-a706710bb699"

    # Read the api key from the environment variable
    apikey = os.getenv("POLARIS_API_KEY")

    @task()
    def query1(self):
        query1 = """
                    select
                        count(*) as matched,
                        'A0001' as Rule
                    from
                        fake_trust
                    where
                        "Organisation" <> '' 
                        and "Mobile_Phone_Number" = '661-231-9618' 
                        and "Surname" <> '' 
                        and "Home_Postcode" <> '' 
                        and "Home_Address1" <> '' 
                        and "Date_Of_Birth" <> '' 
                        and "First_Name" NOT LIKE '' 
                        and "Application_Type" = 'Credit Card'
                """
        payload = {
            "query" : query1,
            "context" : {
                "queryId": "ajith-gbg-query-1"
            }
        }

        # Set the headers
        self.client.headers = { 'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': f'Basic {self.apikey}'}

        # Send the request
        response = self.client.post("/query/sql", json=payload)

        # print the response only if status code is not 200
        if response.status_code != 200:
            print("Response: " + response.text)

    @task()
    def query2(self):
        query2 = """
                    select
                        count(*) as matched,
                        'C0001' as Rule
                    from
                        fake_trust
                     where
                        "Surname" = ''
                        and "Date_Of_Birth" = '12/31/1982'
                        and "Mobile_Phone_Number" = '500-137-6579'
                        and "Application_Type" = 'Credit Card'
                """
        payload = {
            "query" : query2,
            "context" : {
                "queryId": "ajith-gbg-query-2"
            }
        }

        # Set the headers
        self.client.headers = { 'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': f'Basic {self.apikey}'}

        # Send the request
        response = self.client.post("/query/sql", json=payload)

        # print the response only if status code is not 200
        if response.status_code != 200:
            print("Response: " + response.text)

    @task()
    def query3(self):
        query3 = """
                    select
                        count(*) as matched,
                        'M0001' as Rule
                    from
                        fake_trust
                    where
                        "First_Name" = ''
                        and "Surname" = 'Huttley'
                        and "Date_Of_Birth" = '1/3/1953'
                        and "Application_Type" = 'Burger Time'
                        and "Organisation" <> 'Browsetype'
                        and "Organisation" = 'Bubbletube'
                """
        payload = {
            "query" : query3,
            "context" : {
                "queryId": "ajith-gbg-query-3"
            }
        }

        # Set the headers
        self.client.headers = { 'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': f'Basic {self.apikey}'}

        # Send the request
        response = self.client.post("/query/sql", json=payload)

        # print the response only if status code is not 200
        if response.status_code != 200:
            print("Response: " + response.text)


    @task()
    def query3(self):
        query3 = """
                    select
                        count(*) as matched,
                        'M0001' as Rule
                    from
                        fake_trust
                    where
                        "First_Name" = ''
                        and "Surname" = 'Huttley'
                        and "Date_Of_Birth" = '1/3/1953'
                        and "Application_Type" = 'Burger Time'
                        and "Organisation" <> 'Browsetype'
                        and "Organisation" = 'Bubbletube'
                """
        payload = {
            "query" : query3,
            "context" : {
                "queryId": "ajith-gbg-query-3"
            }
        }

        # Set the headers
        self.client.headers = { 'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': f'Basic {self.apikey}'}

        # Send the request
        response = self.client.post("/query/sql", json=payload)

        # print the response only if status code is not 200
        if response.status_code != 200:
            print("Response: " + response.text)

    @task()
    def query3(self):
        query3 = """
                    select
                        count(*) as matched,
                        'M0001' as Rule
                    from
                        fake_trust
                    where
                        "First_Name" = ''
                        and "Surname" = 'Huttley'
                        and "Date_Of_Birth" = '1/3/1953'
                        and "Application_Type" = 'Burger Time'
                        and "Organisation" <> 'Browsetype'
                        and "Organisation" = 'Bubbletube'
                """
        payload = {
            "query" : query3,
            "context" : {
                "queryId": "ajith-gbg-query-3"
            }
        }

        # Set the headers
        self.client.headers = { 'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': f'Basic {self.apikey}'}

        # Send the request
        response = self.client.post("/query/sql", json=payload)

        # print the response only if status code is not 200
        if response.status_code != 200:
            print("Response: " + response.text)