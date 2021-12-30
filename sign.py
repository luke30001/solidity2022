from eth_account.messages import encode_defunct
from web3.auto import w3
message = encode_defunct(text="hello")
print(w3.eth.account.sign_message(message, private_key="0x8aaa00acd15b9909228dc088a8a0a772e371c1b5da2a720367f2f5dd87ed0f2a"))
