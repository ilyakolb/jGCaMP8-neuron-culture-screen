import pandas as pd 

def condition_df(data_in):
	'''
	initial conditioning of pd array imported from csv (e.g. data_all_20210203_GCaMP96uf.csv)
	
	- rename columns with user friendly names
	- drop NaNs
	- drop TEOnly, none, etc
	- replace n AP with n AP
	'''

	data_in = data_in.drop(columns = data_in.columns[data_in.columns.str.contains('Unnamed:')], axis=1) # drop unnamed columns
	data_in.drop(index = ['TEOnly','TE only', 'TE-only', 'none', '376.13'], inplace=True, errors='ignore') # 

	# rename columns to user friendly names
	s = data_in.columns

	for nAP in [1, 3, 10, 160]:
	    # replace nFP with 'n AP'
	    s = s.str.replace(str(nAP) + 'FP', str(nAP) + ' AP')
	
	# replace TimeToPeak with Time to peak
	data_in.columns = s
	data_in.columns = data_in.columns.str.replace('Rise', 'Half-rise time')
	data_in.columns = data_in.columns.str.replace('Decay', 'Half-decay time')
	data_in.columns = data_in.columns.str.replace('TimeToPeak', 'Time to peak')

	# replace 1FP with DF/F (1FP)
	data_in = data_in.rename(columns = {'1 AP': 'DF/F (1 AP)', '3 AP': 'DF/F (3 AP)', '10 AP': 'DF/F (10 AP)', '160 AP': 'DF/F (160 AP)',
										'1 AP(p)': 'DF/F (1 AP)(p)', '3 AP(p)': 'DF/F (3 AP)(p)', '10 AP(p)': 'DF/F (10 AP)(p)', '160 AP(p)': 'DF/F (160 AP)(p)'})

	# remove NaNs
	data_in.dropna(axis = 0, how = 'any')
	return data_in