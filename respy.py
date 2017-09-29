
import os


# the default resources dir
RESOURCES_DIR = "C:\\respy_resources\\"


def init_dir(resources_dir=RESOURCES_DIR):
    """ Make sure RESOURCES_DIR and resources.py exist """
    if not os.path.exists(resources_dir):
        os.makedirs(resources_dir)


def init_resources():
    open("resources.py", "a")
    if not open("resources.py").read():
        open("resources.py", "w").write("res_dict={}")


def set(resorce_file, target_name=None):
    """
    set the resource file into resources.py
    the resorce_file should be a absolute path or a relative path
    """
    if not os.path.exists(resorce_file):
        print(resorce_file + ' not found!')
        return
    if not target_name:
        target_name = os.path.split(resorce_file)[-1]
    init_resources()
    bin_str = open(resorce_file, "rb").read()
    read_str = open("resources.py").read()
    out_str = read_str[:-1] + repr(target_name) + ":" + repr(bin_str) + ",\n}"
    open("resources.py", "w").write(out_str)


def release(resources_dir=RESOURCES_DIR):
    """ release the files in resources.py to resources dir (C:\respy_resources\) """
    try:
        from resources import res_dict
    except ImportError as e:
        print('resources module not found!')
        res_dict = {}

    init_dir(resources_dir)
    for target_name, bin_str in res_dict.iteritems():
        open(get(target_name, resources_dir, False), "wb").write(bin_str)

    
def get(target_name, resources_dir=RESOURCES_DIR, flag=True):
    """ get target file path in resources dir (C:\respy_resources\) """
    if flag:
        release(resources_dir)
    path = os.path.join(resources_dir, target_name)
    if not os.path.exists(path) and flag:
        return '<not_exists>'
    return path



