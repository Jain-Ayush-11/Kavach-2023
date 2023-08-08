import requests

def trace_destination(source_address, api_key):
    current_address = source_address
    while True:
        transaction = find_transaction_by_input(current_address, api_key)
        if transaction is None:
            return current_address
        current_address = transaction['raw_data']['contract'][0]['parameter']['value']['to_address']

def find_transaction_by_input(input_address, api_key):
    url = f'https://api.trongrid.io/v1/accounts/{input_address}/transactions'
    headers = {'TRON-PRO-API-KEY': api_key}
    while url is not None:
        response = requests.get(url, headers=headers)
        data = response.json()
        transactions = data['data']
        retry = 3
        for transaction in transactions:
            if transaction['raw_data']['contract'][0]['parameter']['value']['owner_address'] == input_address:
                return transaction
        url = data['meta']['links'].get('next')
    return None


print(find_transaction_by_input(input_address="TWg9uE1CLRF8BVh94tQUsxbkeiLsgrg7rm", api_key="8b0988e0-5691-42ef-9d56-945c33832a78"))
