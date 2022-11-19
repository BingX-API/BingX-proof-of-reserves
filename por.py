# -*- coding: utf-8 -*-

import argparse
from hashlib import sha256


# initialize the input parameters
parser = argparse.ArgumentParser(description="BingX's Proof of Reserves Verification Script")
subparsers = parser.add_subparsers(title='commands', help='all valid commands', dest='command')

hash_parser = subparsers.add_parser('hash', help='Calculate hash for your input string.')
hash_parser.add_argument('raw_input_string', help='The raw input string.')

verify_parser = subparsers.add_parser('verify', help='Verify the inclusion of the Merkle leaf, compare the result with the Merkle root')
verify_parser.add_argument('merkle_leaf', help='Hash of your record in the MerkleTree.')
verify_parser.add_argument('merkle_path', help='The hash path of your identifier in Merkle Tree with the format: "{hash1},{hash2}..."')

args = parser.parse_args()


# put raw input string to hash string
def hash(raw_input_string):
    hash_result = sha256(raw_input_string.encode()).hexdigest().upper()
    return hash_result


# use to generate merkle tree's root hash.
# This function will merge each of the path hash, and come out a final hash
# you can compare the final hash to the root hash that BingX has provided
def generate_root(merkle_leaf, path):
    path_list = list(path.split(','))
    root_hash = merkle_leaf
    for index in range(len(path_list)):
        root_hash = sha256(root_hash.join(path_list[index]).encode()).hexdigest().upper()
    return root_hash


def main():
    # calculate hash for the raw input string
    # format: hash {rawInputString}
    if args.command == "hash":
        raw_input_string = args.raw_input_string
        hash_result = hash(raw_input_string)
        print("hash: ", hash_result)
    # calc the root hash for the provided merkle leaf and merkle path
    elif args.command == "verify":
        path = args.merkle_path
        merkle_leaf = args.merkle_leaf
        root_hash = generate_root(merkle_leaf, path)
        print('root hash: ', root_hash)
    else:
        print('command error, please check your command')


# start execution
if __name__ == '__main__':
    main()
