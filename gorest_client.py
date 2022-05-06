import requests


class Client:
    def __init__(self, token):
        self.token = token
        self.base_url = "https://gorest.co.in/public/v2/users/"

    def get_users(self):
        response = requests.get(f"{self.base_url}")
        return response.content

    def get_user(self, idn):
        response = requests.get(f"{self.base_url}{idn}")
        return response.content

    def create_user(self, name, email, gender, status):
        response = requests.post(
            f"{self.base_url}",
            data={
                "name": name,
                "email": email,
                "gender": gender,
                "status": status,
            },
            headers={"Authorization": f"Bearer {self.token}"},
        )
        if response.status_code == 201:
            return response.json()

        print(f"Error, {response.status_code}, \n{response.content} ")
        return False

    def update_user(self, idn, newname, newemail, newgender, newstatus):
        response = requests.put(
            f"{self.base_url}{idn}",
            data={
                "name": newname,
                "email": newemail,
                "gender": newgender,
                "status": newstatus,
            },
            headers={"Authorization": f"Bearer {self.token}"},
        )
        if response.status_code == 200:
            return response.json()

        print(f"Error, {response.status_code}, \n{response.content} ")
        return False

    def delete_user(self, idn):
        response = requests.delete(
            f"{self.base_url}{idn}",
            headers={"Authorization": f"Bearer {self.token}"},
        )
        if response.status_code == 204:
            return True

        print(f"Error, {response.status_code}, \n{response.content}")
        return False


gorest_client = Client(
    "38c5b28f734d47d620cde565d41d79680c0171df817454a3ebf6722dfc882d66"
)
