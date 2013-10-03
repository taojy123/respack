
# Init
if not os.path.exists("C:\\respy_resource"):
    os.makedirs("C:\\respy_resource")

open("resorces.py", "a")



def make_res(resorce_file):
    bin_str = open(resorce_file, "rb").read()
    read_str = open("resorces.py").read()
    if read_str:
        out_str = read_str[:-1] + ", '" + str(bin_str) + "']"
    else:
        out_str = "res = ['" + str(bin_str) + "']"
    open("resorces.py", "w").write(out_str)


def get_res(filename):
    return "C:\\respy_resource\\" + filename



def cteate_res():
    import resorces
    




