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


''' main '''
global funcotator_bench_f

cerebra_bench_f = 'cerebra_bench/cerebra_giab_all_gencode27_patch_revised.csv'
cwd = os.getcwd()				
cb_df = pd.read_csv(cerebra_bench_f, index_col=0)

# driver loop 
for funco in os.listdir('funco_bench_ensp_tags/final'): # outer loop -- by funco outfile (.vcf)
	curr_sample = funco.split('_')[0] + '_' + funco.split('_')[1]
	funco_path = cwd + '/funco_bench_ensp_tags/final/' + funco

	funco_df = pd.read_csv(funco_path, header=None, names=['col'])
	funco_ids = list(funco_df.col)

	cerebra_line = cb_df.loc[curr_sample] # find the cerebra_bench line that corresponds to this funco outfile
	cerebra_ids = get_trans_ids(cerebra_line)

	inter = len(set(cerebra_ids).intersection(set(funco_ids)))
	funco_u = len(set(funco_ids)) - inter
	cereb_u = len(set(cerebra_ids)) - inter

	c_overlap = inter / len(set(cerebra_ids))
	f_overlap = inter / len(set(funco_ids))

	print(curr_sample)
	print('cerebra overlap: %f' % c_overlap)
	print('funco overlap: %f' % f_overlap)
	print('cerebra total: %f' % len(set(cerebra_ids)))
	print('funco total: %f' % len(set(funco_ids)))
	print(' ')




