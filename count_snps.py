import sys, gzip
import pandas as pd

def nlines_header(f):
    counter = 0
    for line in f:
        if line[0:2] == '##':
            counter += 1
        else: break
    return(counter)

def main():
    f = sys.argv[1]
    fh = gzip.open(f, 'rb')
    nlines = nlines_header(fh)
    cksize = 8000
    gen = pd.read_csv(f, sep="\t", chunksize=cksize, 
            compression='gzip', skiprows=nlines, header=None)
    # Index Gen
    for nl, i in enumerate(gen):
        if i.ix[0,0] == 1:
            print(i.head())
            print(i.ix[0,8])
            break
        else: pass
    print(nlines)
    thesnps = './data/IQ_snps/chr{chrom!s}_IQPC_snps.txt'
    #genotypes = '../data


    # Count @ 1000 genomes populations 

    for i in range(21, 22):
        gi = pd.read_csv(thesnps.format(chrom=i), sep=",", header=None)
        print(gi.head())
        print(gi.shape)
        print(i)


if __name__ == '__main__':
    main()
