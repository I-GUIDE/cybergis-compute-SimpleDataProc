#!/bin/env python3

import yaml
import os


processor_dict ={'$1': {'SimpleDataProc':{'input_dir':os.environ['param_input_dir'], 'start_year': os.environ['param_start_year'],'end_year': os.environ['param_end_year']}}}

with open('/job/executable/data_process.yml','w') as demfile:
    yaml.dump(processor_dict,demfile)


