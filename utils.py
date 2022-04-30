import pandas as pd 

def abbreviate_construct(construct_id):
    '''
    abbreviate_construct: for brevity in plotting, abbreviate construct.
    all GCaMPxx and jGCaMPxx to xx
    all jGCaMPx.yyy to yyy
    all XCaMP stays the same
    '''
    if construct_id.startswith('GCa') or construct_id.startswith('jGCa'):
        if '.' not in construct_id:
            return construct_id[-2:]
        else:
            return construct_id
    else:
        return construct_id

def filter_construct_range(construct_id, prefix, low, high):
    '''
    return whether construct_id starts with prefix and is between high and low values
    e.g. filter_construct_range('500.123', '500', 1, 200) -> True
    '''
    if construct_id.startswith(prefix):
        suffix = construct_id[construct_id.index('.')+1:]
        return (int(suffix) > low and int(suffix) <= high)
    return False

def condition_df(data_in):
	'''
	initial conditioning of pd array imported from csv (e.g. data_all_20210203_GCaMP96uf.csv)
	
	- rename columns with user friendly names
	- drop NaNs
	- drop TEOnly, none, etc
	- replace n AP with n AP
	'''

	data_in = data_in.drop(columns = data_in.columns[data_in.columns.str.contains('Unnamed:')], axis=1) # drop unnamed columns
	data_in = data_in.drop(index = ['TEOnly','TE only', 'TE-only', 'none', '376.13', '514.4409', '514.1', '514.1722', '514.4445', '497.32', '497.440', '515.4', '515.3', '515.2']) # 

	# rename columns to user friendly names
	s = data_in.columns

	for nAP in [1, 3, 10, 160]:
	    # replace nFP with 'n AP'
	    s = s.str.replace('_' + str(nAP) + '_fp', ' ({} AP)'.format(nAP))
	
	# replace TimeToPeak with Time to peak
	data_in.columns = s
	data_in.columns = data_in.columns.str.replace('rise', 'Half-rise time')
	data_in.columns = data_in.columns.str.replace('decay', 'Half-decay time')
	data_in.columns = data_in.columns.str.replace('timetopeak', 'Time to peak')
	data_in.columns = data_in.columns.str.replace('snr', 'SNR')
	data_in.columns = data_in.columns.str.replace('norm_f0', 'Norm. F0')
    
    
	# replace 1FP with DF/F (1FP)
	data_in = data_in.rename(columns = {'1_fp': 'DF/F (1 AP)', '3_fp': 'DF/F (3 AP)', '10_fp': 'DF/F (10 AP)', '160_fp': 'DF/F (160 AP)',
										'1_fp_p': 'DF/F (1 AP)_p', '3_fp_p': 'DF/F (3 AP)_p', '10_fp_p': 'DF/F (10 AP_p', '160_fp_p': 'DF/F (160 AP)_p'})
    

	# remove NaNs
	data_in.dropna(axis = 0, how = 'any')
	return data_in
