# 1000 Genomes Directory path
# Defaults to 1000 Genomes FTP.  Replace with path to local directory 
# containing the 1000 Genomes vcfs.
CHROMOSOME_VCF_FILE = "{path}/ALL.chr{chromosome}.phase3_shapeit2_mvncall_integrated_v5.20130502.genotypes.vcf.gz"
PANEL_FILE = "{path}/integrated_call_samples_v3.20130502.ALL.panel"

CHROMOSOME_BED_FILE_FEW_SNPS = "/home/endrebak/playground/freewas/data/{chromosome}_1kg_few_snps.bed"
BRAINY_VCF_FILE = "/home/endrebak/genomes/highiq/{brainiac}.vcf"
BRAINY_BED_FILE = "/home/endrebak/playground/freewas/data/{brainiac}.bed"
BRAINY_BIM_FILE_NEW_SNP_NAMES = "/home/endrebak/playground/freewas/data/{brainiac}_snp_names_improved.bim"

WHOLE_GENOME_BED_ONEKG = "/home/endrebak/playground/freewas/data/1kg_genome_whole.bed"
WHOLE_GENOME_BED_ONEKG_WITHOUT_LD = "/home/endrebak/playground/freewas/data/1kg_genome_whole_without_ld.bed"
CHROMOSOME_FILE_LIST = "/home/endrebak/playground/freewas/data/chromosomes_to_merge.txt"

LIST_OF_RANGES_TO_EXCLUDE_DUE_TO_LD = "/home/endrebak/playground/freewas/data/ld_ranges"
FAM_FILE_WITH_RACE = "/home/endrebak/playground/freewas/data/fam_file_with_race.fam"
RACE_SNP_FREQUENCY_FILE = "/home/endrebak/playground/freewas/data/race_snp_frequency_file.frq.strat"
RACE_SNP_FREQUENCY_CSV = "/home/endrebak/playground/freewas/data/race_snp_frequency_file.csv"
RACE_SPECIFIC_FREQUENCY_FILE = "/home/endrebak/playground/freewas/data/{population}_specific_freq_file"
ONEKG_BIM_FILE_WITH_SNP_NAMES = "/home/endrebak/playground/freewas/data/snp_file_with_names.bim"
BENEFICIAL_ALLELES = "/home/endrebak/playground/freewas/data/beneficial_alleles_{r2_level}.pickle"

RACE_SNP_R2_FILE = "/home/endrebak/playground/freewas/data/population_r2_{r2_level}_score"
BRAINY_SNP_COUNT_FILE_R2 = "/home/endrebak/playground/freewas/data/{brainiac}_{r2_level}_r2_count.frq.count"
RACE_SNP_COUNT_FILE_R2 = "/home/endrebak/playground/freewas/data/{population}_{r2_level}_r2_count.frq.strat"
SNPS_IN_ALL_BRAINIACS = "/home/endrebak/playground/freewas/data/snps_to_extract"

BRAINIAC_FISHERS_EXACT_DATA = "/home/endrebak/playground/freewas/data/{brainiac}_{r2_level}.fe"
POPULATION_FISHERS_EXACT_DATA = "/home/endrebak/playground/freewas/data/{population}_{r2_level}.fe"
