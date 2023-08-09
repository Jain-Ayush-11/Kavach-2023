# Import requests library to make API calls
import requests

# Define a function to get the destination addresses from a bitcoin transaction or the outputs of a wallet address
def get_destinations(address_or_tx):

    if is_valid_address(address_or_tx) or is_valid_tx_hash(address_or_tx):
        url = f"https://api.blockcypher.com/v1/btc/main/{'addrs' if is_valid_address(address_or_tx) else 'txs'}/{address_or_tx}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            destinations = []
            if is_valid_address(address_or_tx):
                for tx in data["txs"]:
                    for output in tx["outputs"]:
                        if "spent_by" not in output:
                            destination = output["addresses"]
                            if destination is not None:
                                destination = destination[0]
                                if destination not in destinations:
                                    destinations.append(destination)
            else:
                for output in data["outputs"]:

                    destination = output["addresses"]
                    # Check if the destination address is not None
                    if destination is not None:
                        # Get the first element of the destination address list
                        destination = destination[0]
                        # Append it to the destinations list if not already present
                        if destination not in destinations:
                            destinations.append(destination)
            # Return the destinations list
            return destinations
        else:
            # Return an empty list if the response is invalid
            return []
    else:
        # Return an empty list if the input is invalid
        return []

# Define a helper function to check if a string is a valid bitcoin address
def is_valid_address(address):
    # Check if the address length is between 26 and 35 characters
    if len(address) < 26 or len(address) > 35:
        return False
    # Check if the address starts with 1, 3, or bc1 (for legacy, segwit, and bech32 formats respectively)
    if not (address.startswith("1") or address.startswith("3") or address.startswith("bc1")):
        return False
    # Check if the address contains only alphanumeric characters (excluding uppercase O, uppercase I, lowercase l, and number 0)
    valid_chars = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    for char in address:
        if char not in valid_chars:
            return False
    # TODO: Add more validation rules such as checksum and version byte checks (optional)
    return True

# Define a helper function to check if a string is a valid transaction hash
def is_valid_tx_hash(tx_hash):
    # Check if the transaction hash length is 64 characters (32 bytes)
    if len(tx_hash) != 64:
        return False
    # Check if the transaction hash contains only hexadecimal characters (0-9 and a-f)
    hex_chars = "0123456789abcdef"
    for char in tx_hash:
        if char not in hex_chars:
            return False
    return True

# Test the function with an example transaction hash
tx_hash = "4cdb5e7315287062f3e90c9c78ec5d9c7711d6544a41ef5dfd964935e24360af"
print(f"The destination addresses for transaction {tx_hash} are:")
print(get_destinations(tx_hash))

# Test the function with an example wallet address
address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
print(f"The destination addresses for wallet address {address} are:")
print(get_destinations(address))