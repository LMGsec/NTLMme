#!/usr/bin/python
###########################################################
###########################################################
#  _   _ _____ _     __  __                               #
# | \ | |_   _| |   |  \/  |_ __ ___   ___   _ __  _   _  #
# |  \| | | | | |   | |\/| | '_ ` _ \ / _ \ | '_ \| | | | #
# | |\  | | | | |___| |  | | | | | | |  __/_| |_) | |_| | #
# |_| \_| |_| |_____|_|  |_|_| |_| |_|\___(_) .__/ \__, | #
#                                           |_|    |___/  #
###########################################################
###########################################################
# @DFeat406 @LMGsecurity - 3/31/21

"""
Copyright 2021, LMG Security
Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT 
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT 
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT 
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON 
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE
"""

import hashlib
import fileinput
import random
import sys
import argparse
import binascii

#Defining command line args

parser = argparse.ArgumentParser(description='NTLM Hash Generator and String Converter.')
parser.add_argument('-i', '--inputfile', help='File to read strings from.')
parser.add_argument('-o', '--outputfile', help='File to write hashes to.')
parser.add_argument('-r', '--randomhashes', type=int, help='Create specified number of random NTLM hashes.')
parser.add_argument('-s', '--single', type=str, help='Hashes individual strings.')

args = parser.parse_args()

# Help if nothing is specified
if len(sys.argv)==1:
	parser.print_help()
	sys.exit(1)

#main
def main():

	if args.inputfile is not None:
		with open(args.inputfile) as file:
				for line in file:
					line = line.strip()
					hash = hashlib.new('md4', line.encode('utf-16le')).digest()
					if args.outputfile is not None:
						with open(args.outputfile, 'a+') as output_file:
							output_file.write(binascii.hexlify(hash) + ":" +line)
					else:
						print binascii.hexlify(hash) +':'+line
	elif args.randomhashes is not None:
		for x in range(args.randomhashes):
			lst = [random.choice('0123456789abcdef') for i in range(32)]
			str = ''.join(lst)
			if args.outputfile is not None:
				with open(args.outputfile, 'a+') as output_file:
					output_file.write(str + '\n')
			else:
				print (str)
	elif args.single is not None:
		hash = args.single
		hash = hashlib.new('md4', hash.encode('utf-16le')).digest()
		if args.outputfile is not None:
			with open(args.outputfile, 'a+') as output_file:
				output_file.write(binascii.hexlify(hash) + '\n')
		else:
			print binascii.hexlify(hash)

if __name__ == "__main__":
    main()
