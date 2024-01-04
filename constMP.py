#To Do: Replace all this with a naming service

# With local addresses (within the same cloud region)
#PEERS = ['172.31.78.41','172.31.65.227','172.31.74.212','172.31.75.17','172.31.72.48','172.31.75.162']

# With public addresses (in the same region of the cloud)
# The last one is not fixed and must be changed each time the lab is restarted.
PEERS_SAME_REGION = ['54.167.24.39','54.145.199.22','3.89.161.213','35.172.225.184','54.80.183.57','54.82.237.3']

# With public addresses (in two separate regions - last two servers in Oregon)
PEERS_TWO_REGIONS = ['54.167.24.39','54.145.199.22','3.89.161.213','35.172.225.184','44.239.194.163','52.88.79.71']


PEER_UDP_PORT = 4567
PEER_TCP_PORT = 5679
N = 6   # Number of peers
SERVER_ADDR ='54.221.20.159'
SERVER_PORT = 5678

