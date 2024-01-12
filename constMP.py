#To Do: Replace all this with a naming service

# With local addresses (within the same cloud region)
#PEERS = ['172.31.78.41','172.31.65.227','172.31.74.212','172.31.75.17','172.31.72.48','172.31.75.162']

# With public addresses (in the same region of the cloud)
# The last one is not fixed and must be changed each time the lab is restarted.
PEERS_SAME_REGION = ['54.144.183.145','3.91.176.209','52.91.81.9','54.145.116.43','54.152.213.178','3.92.217.120']

# With public addresses (in two separate regions - last two servers in Oregon)
PEERS_TWO_REGIONS = ['54.144.183.145','3.91.176.209','52.91.81.9','54.145.116.43','34.219.162.159','35.88.151.74']


PEER_UDP_PORT = 4567
PEER_TCP_PORT = 5679
N = 6   # Number of peers
SERVER_ADDR ='54.221.20.159'
SERVER_PORT = 5678


# Account Balance
balance = 0
# List of operations
operationList = ['deposit', 'fee', 'withdraw']
# Deposit gap
depositRange = [1,100]
feeRange = [1,3]