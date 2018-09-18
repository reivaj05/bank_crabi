import requests

base_url = 'http://localhost:8000/'
login_endpoint = '{}rest-auth/login/'.format(base_url)
accounts_endpoint = '{}api/v0.1/bank/accounts/'.format(base_url)
transfers_endpoint = '{}api/v0.1/bank/transfers/'.format(base_url)
authorizations_endpoint = '{}api/v0.1/bank/authorizations/'.format(base_url)


class UserExample():
    data = None
    token = None
    account = None
    headers = None

    def __init__(self, data):
        self.data = data
        self.__login()

    def __login(self):
        response = requests.post(login_endpoint, json=self.data)
        response.raise_for_status()
        self.token = response.json()['key']
        self.headers = {'Authorization': 'Token {}'.format(self.token)}

    def create_account(self, initial_money):
        data = {'balance': initial_money, 'user': self.data['username']}
        response = requests.post(accounts_endpoint, json=data, headers=self.headers)
        response.raise_for_status()
        self.account = response.json()

    def transfer(self, target, total):
        data = {'sender': self.account['eid'], 'receiver': target, 'total': total}
        response = requests.post(transfers_endpoint, json=data, headers=self.headers)
        response.raise_for_status()
        return response

    def authorize(self, total):
        data = {'account': self.account['eid'], 'total': total}
        response = requests.post(authorizations_endpoint, json=data, headers=self.headers)
        response.raise_for_status()
        return response


class Example():
    user_1 = None
    user_2 = None

    def __init__(self):
        self.user_1 = UserExample({'email': 'admin@crabi.com', 'username': 'admin@crabi.com', 'password': 'password'})
        self.user_2 = UserExample({'email': 'admin2@crabi.com', 'username': 'admin2@crabi.com', 'password': 'password'})
        self.steps = self.__init_steps()

    def __init_steps(self):
        return [
            self.__step_1, self.__step_2, self.__step_3, self.__step_4,
            self.__step_5, self.__step_6, self.__step_7, self.__step_8,
        ]

    def __step_1(self):
        print('Creating account with $1000')
        self.user_1.create_account(1000)
        print('Account created {}'.format(accounts_endpoint + self.user_1.account['eid'] + '/'))

    def __step_2(self):
        print('Creating account with $360')
        self.user_2.create_account(360)
        print('Account created {}'.format(accounts_endpoint + self.user_2.account['eid'] + '/'))

    def __step_3(self):
        print('Sending 500 from account1 to account2')
        response = self.user_1.transfer(self.user_2.account['eid'], 500)
        print('Success: {}'.format(response.ok))

    def __step_4(self):
        print('Sending 200 from account2 to account1')
        response = self.user_2.transfer(self.user_1.account['eid'], 200)
        print('Success: {}'.format(response.ok))

    def __step_5(self):
        print('Authorizing 200 from account2')
        response = self.user_2.authorize(200)
        print('Success: {}'.format(response.ok))

    def __step_6(self):
        print('Authorizing 300 from account1')
        response = self.user_1.authorize(300)
        print('Success: {}'.format(response.ok))

    def __step_7(self):
        print('Sending 500 from account2 to account1')
        try:
            response = self.user_2.transfer(self.user_1.account['eid'], 500)
            print('Success: {}'.format(response.ok))
        except:
            print('Cant transfer')

    def __step_8(self):
        print('Sending 400 from account1 to account2')
        response = self.user_1.transfer(self.user_2.account['eid'], 400)
        print('Success: {}'.format(response.ok))

    def run(self):
        for step in self.steps:
            step()


if __name__ == '__main__':
    Example().run()
