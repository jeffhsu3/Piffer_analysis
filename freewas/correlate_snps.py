"""
"""
import numpy as np
import pandas as pd
import gzip

from scipy.stats import pearsonr
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('../config.cfg')


def get_nlines(fh):
    counter = 0
    for line in fh:
        if line[0:2] == '##':
            counter +=1
        else:
            break
    return(counter)



def get_pairwise_ld(chrom):
    """ Calculate population based ld of SNPs
    """
    global one_geno_string  
    snps =\
            pd.read_csv('../data/IQ_snps/chr{chrom!s}_IQPC_snps.txt'.
                    format(chrom=chrom), sep=",",
                    index_col=0, header=None)
    one_geno_string =(
    '../../1KG_proj/ALL.chr{chrom!s}.'
    'phase3_shapeit2_mvncall_integrated_'
    'v5.20130502.genotypes.vcf.gz'
    )
    filename = one_geno_string.format(chrom=chrom)
    f = gzip.open(filename, 'rb')
    nlines = get_nlines(f)
    cols_use = [0,1,2,3,4]
    cols_use.extend(range(9, 2513))
    geno = pd.read_csv(filename, compression='gzip', 
            sep="\t", skiprows=nlines,
            chunksize=5000, header=0, usecols=cols_use)
    concat_list = []
    debug = 0
    for i in geno:
        noid = i['ID'] == '.'
        noid = noid.values
        nix = i['#CHROM'][noid].map(str) + "_" +\
                i['POS'][noid].map(str) + "_" + i["ALT"][noid].map(str)
        common = nix.isin(snps.index).values
        concat_list.append(i.ix[common,:])
        debug += 1
        if debug >= 3:
            break
        else: pass
    full_geno = pd.concat(concat_list)
    print(full_geno.shape)


if __name__ == '__main__':
    pca4 = pd.read_csv('../data/4SNP_4PCA_pops.txt', sep="\t", header=0,
            index_col=0)
    get_pairwise_ld(22)

