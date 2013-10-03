import os

# the default resources dir
RESOURCES_DIR = "C:\\respy_resources\\"


def init():
    """ Make sure RESOURCES_DIR and resources.py exist """
    if not os.path.exists(RESOURCES_DIR):
        os.makedirs(RESOURCES_DIR)
    open("resources.py", "a")
    if not open("resources.py").read():
        cls_res()

def make_res(resorce_file):
    """
    make the resource file into resources.py
    the resorce_file should be a absolute path or a relative path
    """
    init()
    filename = resorce_file.split("\\")[-1]
    bin_str = open(resorce_file, "rb").read()
    read_str = open("resources.py").read()
    out_str = read_str[:-1] + repr(filename) + ":" + repr(bin_str) + ",\n}"
    open("resources.py", "w").write(out_str)


def release_res():
    """ release the files in resources.py to resources dir (C:\respy_resources\) """
    init()
    from resources import res_dict
    for filename, bin_str in res_dict.iteritems():
        open(get_res(filename), "wb").write(bin_str)

    
def get_res(filename):
    """ get resource file path in resources dir (C:\respy_resources\) """
    return RESOURCES_DIR + filename


def cls_res():
    """ init the resources.py """
    open("resources.py", "w").write("res_dict={}")

init()
