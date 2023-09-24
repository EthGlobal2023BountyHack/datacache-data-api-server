from django.core.management.base import BaseCommand
import os
from web3 import Web3
from datacache.web3inbox import boardcast
import time 
import json

class Command(BaseCommand):
    help = 'Listen to marketplace event and send boardcast'

    def handle(self, *args, **kwargs):
        w3 = Web3(Web3.HTTPProvider(os.getenv("QUICKNODE_URL")))
        contract_address = '0xeb825C7276255471be49551F3136b7095E45BCFf'
        contract_abi = [{"inputs":[{"internalType":"address","name":"_trustedForwarder","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"addr","type":"address"},{"indexed":False,"internalType":"uint256","name":"bountyId","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"},{"indexed":False,"internalType":"bytes32","name":"rewardType","type":"bytes32"},{"indexed":False,"internalType":"address","name":"tokenAddress","type":"address"}],"name":"ClaimedBounty","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"ownerOf","type":"address"},{"indexed":False,"internalType":"uint256","name":"bountyId","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"reward","type":"uint256"},{"indexed":False,"internalType":"bytes32","name":"rewardType","type":"bytes32"},{"indexed":False,"internalType":"address","name":"rewardAddress","type":"address"}],"name":"CreatedBounty","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"userAddress","type":"address"},{"indexed":False,"internalType":"address payable","name":"relayerAddress","type":"address"},{"indexed":False,"internalType":"bytes","name":"functionSignature","type":"bytes"}],"name":"MetaTransactionExecuted","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint64","name":"requestId","type":"uint64"},{"indexed":False,"internalType":"contract ICircuitValidator","name":"validator","type":"address"},{"indexed":False,"internalType":"uint256","name":"schema","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"claimPathKey","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"operator","type":"uint256"},{"indexed":False,"internalType":"uint256[]","name":"value","type":"uint256[]"}],"name":"NewBountyRequestSet","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":True,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":True,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":True,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":True,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":True,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"stateMutability":"payable","type":"fallback"},{"inputs":[],"name":"BOUNTY_MANAGER","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"ERC1155_REWARD","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"ERC20_REWARD","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"ERC712_VERSION","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"ERC721_REWARD","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"OWNER_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"VERIFY_REQUEST_ID","outputs":[{"internalType":"uint64","name":"","type":"uint64"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"bountyId","type":"uint256"},{"internalType":"uint256","name":"totalRewards","type":"uint256"},{"internalType":"address","name":"tokenAddress","type":"address"}],"name":"addBountyBalance","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"addressToId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"bounties","outputs":[{"internalType":"uint256","name":"bountyId","type":"uint256"},{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"description","type":"string"},{"internalType":"string","name":"imageUrl","type":"string"},{"internalType":"bytes32","name":"rewardType","type":"bytes32"},{"internalType":"uint256","name":"reward","type":"uint256"},{"internalType":"address","name":"rewardAddress","type":"address"},{"internalType":"address","name":"payoutFrom","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"bountyBalance","outputs":[{"internalType":"address","name":"ownerOf","type":"address"},{"internalType":"uint256","name":"balance","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"bountyIds","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"description","type":"string"},{"internalType":"string","name":"imageUrl","type":"string"}],"internalType":"struct IBounty.BountyInfo","name":"info","type":"tuple"},{"internalType":"string","name":"rewardType","type":"string"},{"internalType":"uint256","name":"reward","type":"uint256"},{"internalType":"uint256","name":"totalRewards","type":"uint256"},{"internalType":"address","name":"tokenAddress","type":"address"},{"components":[{"internalType":"uint64","name":"requestId","type":"uint64"},{"internalType":"contract ICircuitValidator","name":"validator","type":"address"},{"internalType":"uint256","name":"schema","type":"uint256"},{"internalType":"uint256","name":"claimPathKey","type":"uint256"},{"internalType":"uint256","name":"operator","type":"uint256"},{"internalType":"uint256[]","name":"value","type":"uint256[]"}],"internalType":"struct IBounty.ZKPBountyRequest","name":"request","type":"tuple"}],"name":"createBounty","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"emergencyWithdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"contractAddress","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"emergencyWithdrawERC20","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"userAddress","type":"address"},{"internalType":"bytes","name":"functionSignature","type":"bytes"},{"internalType":"bytes32","name":"sigR","type":"bytes32"},{"internalType":"bytes32","name":"sigS","type":"bytes32"},{"internalType":"uint8","name":"sigV","type":"uint8"}],"name":"executeMetaTransaction","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"getAllBounties","outputs":[{"internalType":"bytes[]","name":"","type":"bytes[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"bountyId","type":"uint256"}],"name":"getBountyOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getChainId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getDomainSeperator","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"getNonce","outputs":[{"internalType":"uint256","name":"nonce","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"bountyId","type":"uint256"}],"name":"getRemainingBounty","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getSupportedRequests","outputs":[{"internalType":"uint64[]","name":"arr","type":"uint64[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint64","name":"requestId","type":"uint64"}],"name":"getZKPRequest","outputs":[{"components":[{"internalType":"uint256","name":"schema","type":"uint256"},{"internalType":"uint256","name":"claimPathKey","type":"uint256"},{"internalType":"uint256","name":"operator","type":"uint256"},{"internalType":"uint256[]","name":"value","type":"uint256[]"},{"internalType":"uint256","name":"queryHash","type":"uint256"},{"internalType":"string","name":"circuitId","type":"string"}],"internalType":"struct ICircuitValidator.CircuitQuery","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"idToAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"forwarder","type":"address"}],"name":"isTrustedForwarder","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"pendingBountyProofs","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint64","name":"","type":"uint64"}],"name":"proofs","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint64","name":"","type":"uint64"}],"name":"requestQueries","outputs":[{"internalType":"uint256","name":"schema","type":"uint256"},{"internalType":"uint256","name":"claimPathKey","type":"uint256"},{"internalType":"uint256","name":"operator","type":"uint256"},{"internalType":"uint256","name":"queryHash","type":"uint256"},{"internalType":"string","name":"circuitId","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint64","name":"","type":"uint64"}],"name":"requestValidators","outputs":[{"internalType":"contract ICircuitValidator","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"bountyId","type":"uint256"}],"name":"revokeBounty","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_treasury","type":"address"}],"name":"setTreasury","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint64","name":"requestId","type":"uint64"},{"internalType":"contract ICircuitValidator","name":"validator","type":"address"},{"internalType":"uint256","name":"schema","type":"uint256"},{"internalType":"uint256","name":"claimPathKey","type":"uint256"},{"internalType":"uint256","name":"operator","type":"uint256"},{"internalType":"uint256[]","name":"value","type":"uint256[]"}],"name":"setZKPRequest","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint64","name":"requestId","type":"uint64"},{"internalType":"contract ICircuitValidator","name":"validator","type":"address"},{"internalType":"uint256","name":"schema","type":"uint256"},{"internalType":"uint256","name":"claimPathKey","type":"uint256"},{"internalType":"uint256","name":"operator","type":"uint256"},{"internalType":"uint256[]","name":"value","type":"uint256[]"},{"internalType":"uint256","name":"queryHash","type":"uint256"}],"name":"setZKPRequestRaw","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"components":[{"internalType":"uint64","name":"requestId","type":"uint64"},{"internalType":"uint256","name":"bountyId","type":"uint256"}],"internalType":"struct IZKPVerifier.SubmitResponse","name":"request","type":"tuple"},{"internalType":"uint256[]","name":"inputs","type":"uint256[]"},{"internalType":"uint256[2]","name":"a","type":"uint256[2]"},{"internalType":"uint256[2][2]","name":"b","type":"uint256[2][2]"},{"internalType":"uint256[2]","name":"c","type":"uint256[2]"}],"name":"submitZKPResponse","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_bountyId","type":"uint256"}],"name":"testFulfillBounty","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"treasury","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"stateMutability":"payable","type":"receive"}]
        contract = w3.eth.contract(address=contract_address, abi=contract_abi)
        event_name = 'CreatedBounty'
        def event_callback(event):
            print(f'Event：{event.event} - Params{event.args}')
            bounty_id = event.args['bountyId']
            boardcast(title="Announcement", 
                body=json.dumps({"timestamp": int(time.time()), "bountyId": int(bounty_id)})
            )            
        # event_filter = contract.events[event_name].createFilter(fromBlock='latest')
        event_filter = contract.events.CreatedBounty.create_filter(fromBlock='latest')

        event_logs = event_filter.get_all_entries()
        while True:
            print("work")
            for event in event_filter.get_new_entries():
                event_callback(event)
        print("end")