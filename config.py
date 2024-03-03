cfg = {}

cfg['cls_num'] = 1
cfg['gpu'] = '0,1,2,3' # to use multiple gpu: cfg['gpu'] = '0,1,2,3'
cfg['batch_size'] = 8 # training batch size
cfg['test_batch_size'] = 8 # testing batch size
cfg['lr'] = 0.01 # base learning rate
cfg['model_path'] = 'model' # the path where to save the trained model and evaluation results
cfg['rs_size'] = [160,160,32] # resample size: [x, y, z]
cfg['rs_spacing'] = [0.5,0.5,1.0] # resample spacing: [x, y, z]. non-positive value means adaptive spacing fit the physical size: rs_size * rs_spacing = origin_size * origin_spacing
cfg['rs_intensity'] = [-200.0, 400.0] # rescale intensity from [min, max] to [0, 1].
cfg['cpu_thread'] = 0 # multi-thread for data loading. zero means single thread.
cfg['commu_times'] = 2 # number of communication rounds
cfg['epoch_per_commu'] = 2 # number of local training epochs within one communication round

# map labels of different client datasets to a uniform label map
cfg['label_map'] = {
    'MSD':{1:1, 2:1},
    # 'NCI-ISBI':{1:1, 2:1},
    'PROMISE12':{1:1},
    # 'PROSTATEx':{1:1},
}

# exclude any samples in the form of '[dataset_name, case_name]'
cfg['exclude_case'] = [
]

# data path of each client dataset
cfg['node_list'] = [
    ['Node-1', ['MSD'], ['dataset/MSD-Prostate'], [19,3,10]], # 32 in total
    # ['Node-2', ['NCI-ISBI'], ['dataset/NCI-ISBI-Prostate'], [48,8,24]], # 80 in total
    ['Node-3', ['PROMISE12'], ['dataset/PROMISE12'], [30,5,15]], # 50 in total
    # ['Node-4', ['PROSTATEx'], ['dataset/PROSTATEx'], [122,20,62]], # 204 in total
]