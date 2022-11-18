# Proof Of Reserves
This tutorial introduces the background of BingX's Proof-of-Reserves and how to verify individual customer's liabilities in [Merkle Tree](https://en.wikipedia.org/wiki/Merkle_tree). Merkle trees are used by both Bitcoin and Ethereum.

## Background
BingX's Proof-of-Reserves utilizes the technique of [Merkle Tree](https://en.wikipedia.org/wiki/Merkle_tree), a data structure designed to encrypt blockchain data securely. This technique makes it possible for individual users to verify that their funds are included in the attestation. 

## Verification
A straightforward mathematical technique for verifying Merkle tree data is Merkle root. Customer can verify the data themselve by calculating their merkle leafs with merkle path to get the Merkle root. If the result matches the expected root, you get the proof-of-inclusion.

### Build the Merkle leaf
Customers can get the Merkle leaf in BingX's proof-of-reserves page, and skip to the [Verification](#Verification).
Customers also can recalculate their Merkle leaf the Merkle leaf with steps below.

### Hashed User ID
Hash your your BingX's UID with SHA256. Each individual's user ID will be hashed with SHA256 before generating the Merkle tree or handing over to auditor. This will ensure independent auditors only see the customer’s hashed user ID, never any personally identifiable information. 

### Combine with assets
1. Check your balance in BingX's proof-of-reserves page.
2. Combine customer's hashed User ID with customer's assets with the following format. Assets are in ascending order (A-Z) by the name.

> {Hashed UID},{Asset1}:{Balance1},{Asset2}:{Asset2},Total:{TotalValueInUsd}

e.g.
> abcdefg,BTC:1.132142,ETH:2.54469871,USDT:20384,Total:49875.12599

Use the following number formating rules to format the balance:
- No Scientific Notation
- Remove trailing zeros: 0.58390000 » 0.5839
- 0 is 0.0:   0.00000000 » 0.0 
- Number must start with 0 if value between 0 and 1: .532 » 0.532

3. Hash the output of step 2 with SHA256


## Verification
1. Get your Merkle path from BingX's proof-of-reserves page.
2. Get the Merkle root from BingX's proof-of-reserves page.
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
> python por.py hash abcdefg,BTC:1.132142,ETH:2.54469871,USDT:20384,Total:49875.12599

- Verify the inclusion of the Merkle leaf, compare the result with the Merkle root
> python por.py verify {Merkle leaf} {Merkle path}
 
