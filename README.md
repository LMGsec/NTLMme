# NTLMme.py
NTLM Hash Generator

## Description
NTLMme.py is an NTLM hash generator written in python3.

## Usage
usage: NTLMme.py [-h] [-i INPUTFILE] [-o OUTPUTFILE] [-r RANDOMHASHES]
                 [-s SINGLE]

NTLM Hash Generator and String Converter.

optional arguments:
  -h, --help            show this help message and exit
  
  -i INPUTFILE, --inputfile INPUTFILE
                        File to read strings from.
                        
  -o OUTPUTFILE, --outputfile OUTPUTFILE
                        File to write hashes to.
                        
  -r RANDOMHASHES, --randomhashes RANDOMHASHES
                        Create specified number of random NTLM hashes.
                        
  -s SINGLE, --single SINGLE
                        Hashes individual strings.
