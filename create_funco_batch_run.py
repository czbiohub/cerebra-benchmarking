''' what does it do? '''

import pandas as pd  
import os

#vcf_path = '/Users/lincoln.harris/code/cerebra-benchmarking/new_vcf/'
vcf_path = './new_vcf/'
vcf_files = os.listdir(vcf_path)

for f in vcf_files:
	curr_path = vcf_path + f
	curr_id = f.strip('.vcf')
	cmd = 'gatk Funcotator -R ref/hg38-plus.fa -V ' + curr_path + ' -O laud_run_out/' + curr_id + '_funco_benchmark.vcf --data-sources-path funcotator_dataSources_orig --ref-version hg38 -output-file-format VCF'
	print(cmd)

