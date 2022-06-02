#!/usr/bin/python

######################################################
# fasta2dict.py
# author: Mitchell O'Brien 
# documentation
# version 1
######################################################

def fasta2dict(reffasta):
    """
    Read a fasta file and create dictionary(name,value)
    where name will be the unique chrom/scaff identifier in header
    and the value is the corresponding sequence
    """
    fastdic = {}
    chr_seq=[]
    fasta=open(reffasta)
    for line in fasta:
        if line.startswith(">"):
            chr_id = line.split(' ')[0].replace('>','')
            chr_seq=""
        else:
            chr_seq+=line.rstrip()
            fastdic[chr_id] = ''.join(chr_seq)
    return fastdic
