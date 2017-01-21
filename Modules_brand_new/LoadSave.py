
def save_data(file, data1):
    with open(file, 'wb') as f:
        dill.dump(len(data1), f)
        dill.dump(data1, f)


# +++++++++++++++++++++++++++++++++ end of function save_data +++++++++++++++++++++++++++++++++++++++++++++++++++++++++



def open_data(file):
    array = []
    with open(file, 'rb') as f:
        length = dill.load(f)
        print("length read: " + str(length))
        array = dill.load(f)

    return array

# +++++++++++++++++++++++++++++++++ end of function open_data ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# noinspection PyShadowingNames
def open_file(file):
    array = [[], [], [], [], [], [], [], []]
    tmp = 0
    with open(file) as openfile:
        for line in openfile:
            for i in range(line.count(",")):
                try:
                    if i is 0:
                        array[i].append(line[tmp:line.find(",", tmp)])
                    else:
                        array[i].append(float(line[tmp:line.find(",", tmp)]))
                except:
                    None
                tmp = line.find(",", tmp) + 1
            tmp = 0
    openfile.close()
    return array


# +++++++++++++++++++++++++++++++++ end of function open_file ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
