# Proof Of Reserves
This tutorial introduces the background of BingX Proof-of-Reserves and how to verify individual liabilities in [Merkle Tree](https://en.wikipedia.org/wiki/Merkle_tree). Both Bitcoin and Ethereum use Merkle trees.

## Background
BingX Proof-of-Reserves utilizes the technique of [Merkle Tree](https://en.wikipedia.org/wiki/Merkle_tree), a data structure designed to encrypt blockchain data securely. This technique allows individual users to verify that their funds are included in the attestation. 

## Verification
Merkle root is a straightforward mathematical technique for verifying the data on a Merkle tree. Users can verify the data by calculating their Merkle leafs with Merkle path to get the Merkle root. If the result matches the expected root, you get the proof-of-inclusion.

### Build the Merkle leaf
Users can get the Merkle leaf in BingX proof-of-reserves page, and skip to the [Verification](#Verification).
Users can also calculate their Merkle leaf with the following steps below.

### Hashed User ID
Hash your BingX UID with SHA256. All UID of the individuals will be hashed with SHA256 before generating the Merkle tree or handing it over to the auditor. This will ensure independent auditor only sees the users' hashed UID and never any personally identifiable information. 

### Combine with assets
1. Check your balance in BingX proof-of-reserves page.
2. Combine users' hashed User ID with their assets in the following format. Assets are in the order below.

> {6e2dcfe5474446c744b353fb153f55930914b069c84e70242f989e66d03cfa62},{BTC}:{0},{ETH}:{0},{USDT}:{802.6287571},{USDC}:{0},Total:{802.6287571}

e.g.
> abcdefg,BTC:1.132142,ETH:2.54469871,USDT:20384,USDC:50.3,Total:49875.12599

Use the following number formatting rules to format the balance:
- No Scientific Notation
- Remove trailing zeros: 0.58390000 » 0.5839
- 0 is 0.0:   0.00000000 » 0.0 
- Number must start with 0 if the value is between 0 and 1: .532 » 0.532

3. Hash the output of step 2 with SHA256


## Verification
1. Get your Merkle path from BingX proof-of-reserves page.
2. Get the Merkle root from BingX proof-of-reserves page.
3. Run the Python script with the Merkle path 


## Command line tool to facilitate the verification
### Requirement
Python 3.4 or above


### Examples
- Generate the Hashed UID
> python por.py hash {uid}

- Generate the Merkle leaf
> python por.py hash {asset string}

e.g.
> python por.py hash abcdefg,BTC:1.132142,ETH:2.54469871,USDT:20384,USDC:50.3,Total:49875.12599

- Verify the inclusion of the Merkle leaf, compare the result with the Merkle root
> python por.py verify {Merkle leaf} {Merkle path}
 
