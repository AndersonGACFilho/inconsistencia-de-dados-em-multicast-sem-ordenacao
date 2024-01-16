#To Do: Replace all this with a naming service

# With local addresses (within the same cloud region)
#PEERS = ['172.31.78.41','172.31.65.227','172.31.74.212','172.31.75.17','172.31.72.48','172.31.75.162']

# With public addresses (in the same region of the cloud)
# The last one is not fixed and must be changed each time the lab is restarted.
PEERS_SAME_REGION = ['54.234.228.207','3.91.79.14','54.81.25.40','44.222.206.14','54.82.28.46','52.90.154.92']

# With public addresses (in two separate regions - last two servers in Oregon)
PEERS_TWO_REGIONS = ['54.234.228.207','3.91.79.14','54.81.25.40','44.222.206.14', '34.212.17.139','35.91.64.97']


PEER_UDP_PORT = 4567
PEER_TCP_PORT = 5679
N = 6   # Number of peers
SERVER_ADDR ='54.198.32.149'
SERVER_PORT = 5678
