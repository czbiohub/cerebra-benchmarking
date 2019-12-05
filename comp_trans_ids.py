''' want to compare the results i get with cerebra to 
	the results obtained with GATK Funcotator, specicially
	with respect to Ensemble translation IDs '''

import pandas as pd
import os

def get_trans_ids(curr_line_):
	''' return all translation ids for a given sample in cerebra benchmarking df '''
	trans_ids = []

	for gene_str in curr_line_:
	    for t_id in gene_str.split(','):
	        tid_strip = t_id.split('.')[0]
	        tid_strip = tid_strip.strip("[")
	        tid_strip = tid_strip.strip("]")
	        
	        try:
	            tid_strip = tid_strip.split("'")[1]
	        except IndexError:
	            continue
	       
	        trans_ids.append(tid_strip)

	return(trans_ids)



def grep_trans_id(curr_ids_, funco_file_):
	''' greps funco file for translation ids of interest'''
	num_found = 0
	num_not_found = 0

	for tid in curr_ids_:
		cmd = 'grep ' + tid + ' ' + funco_file_ + ' > grep_out.csv'
		os.system(cmd)

		if os.path.getsize('grep_out.csv') > 0:
			num_found += 1
		else:
			num_not_found += 1


	print(num_found)
	print(num_not_found)
	print(' ')
	ret_tup = [num_found, num_not_found]


''' main '''
global funcotator_bench_f

cerebra_bench_f = 'cerebra_bench/cerebra_giab_all_benchmarking.csv'
#funcotator_bench_f = 'funco_bench/ash_father_benchmark.vcf' # for testing purposes
cwd = os.getcwd()				
cb_df = pd.read_csv(cerebra_bench_f, index_col=0)

# driver loop 
for f in os.listdir('funco_bench'): 		# outer loop -- by funco outfile (.vcf)
	curr_sample = f.strip('_benchmarking.vcf')
	f_path = cwd + '/funco_bench/' + f

	curr_line = cb_df.loc[curr_sample] # find the cerebra_bench line that corresponds to this funco outfile
	curr_ids = get_trans_ids(curr_line)
	curr_outcome = grep_trans_id(curr_ids, f_path)

	print("%s:   %d %d" % curr_sample, curr_outcome[0], curr_outcome[1])




