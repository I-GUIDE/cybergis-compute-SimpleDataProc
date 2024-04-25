#!/bin/env python3

import yaml
import os

#input_dir = '/compute_scratch/%s' % os.environ['param_input_dir']
#processor_dict ={'$1': {'SimpleDataProc':{'input_dir':input_dir, 'start_year': os.environ['param_start_year'],'end_year': os.environ['param_end_year']}}}
processor_dict ={'$1': {'SimpleDataProc':{'start_year': os.environ['param_start_year'],'end_year': os.environ['param_end_year']}}}

#create folders for each year in /job/result
start_year = int(os.environ['param_start_year'])
end_year = int(os.environ['param_end_year'])
for year in range(start_year,end_year+1):
    os.mkdir('/job/result/%d' % year)

#create the /job/result/outputs folder
os.mkdir('/job/result/outputs')

with open('/job/executable/data_process.yml','w') as dataprocfile:
    yaml.dump(processor_dict,dataprocfile)
