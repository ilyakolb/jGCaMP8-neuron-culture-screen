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
