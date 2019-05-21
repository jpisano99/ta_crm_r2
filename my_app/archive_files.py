import os
import json
import datetime
from shutil import copyfile
from my_app.settings import app_cfg


def phase_4(run_dir=app_cfg['UPDATES_DIR']):
    home = app_cfg['HOME']
    working_dir = app_cfg['WORKING_DIR']
    archives_dir = app_cfg['ARCHIVES_DIR']
    update_dir = app_cfg['UPDATES_DIR']

    path_to_run_dir = (os.path.join(home, working_dir, run_dir))
    path_to_main_dir = (os.path.join(home, working_dir))
    path_to_archives = (os.path.join(home, working_dir, archives_dir))
    path_to_updates = (os.path.join(home, working_dir, update_dir))

    # bookings_path = os.path.join(path_to_run_dir, app_cfg['XLS_BOOKINGS'])
    # renewals_path = os.path.join(path_to_run_dir, app_cfg['XLS_RENEWALS'])

    # Read the config_dict.json file
    with open(os.path.join(path_to_run_dir, app_cfg['META_DATA_FILE'])) as json_input:
        config_dict = json.load(json_input)
    data_time_stamp = datetime.datetime.strptime(config_dict['data_time_stamp'], '%m-%d-%y')
    last_run_dir = config_dict['last_run_dir']

    str_data_time_stamp = datetime.datetime.strftime(data_time_stamp, '%m-%d-%y')

    # Make an archive directory where we need to place these update files
    path_to_archive_fldr = os.path.join(path_to_archives, str_data_time_stamp + " Updates")
    if os.path.exists(path_to_archive_fldr):
        print (path_to_archive_fldr, ' already exists')
        exit()
    else:
        os.mkdir(os.path.join(path_to_archives, str_data_time_stamp + " Updates"))

    # Move a copy of all new files to the archive directory also
    main_files = os.listdir(path_to_run_dir)
    for file in main_files:
        os.rename(os.path.join(path_to_run_dir, file), os.path.join(path_to_archive_fldr, file))

    print(path_to_run_dir)
    print(path_to_main_dir)
    print(path_to_archives)
    print(path_to_updates)
    print(path_to_archive_fldr)
    exit()

    return

phase_4()