import shutil, os

with open('sid.txt', 'r') as input_f:
    sids = input_f.readlines()
sids = [i.strip() for i in sids]

dst = 'asg2-clean'
src = 'asg'
filepaths = []
for root, dirs, files in os.walk(src):
    for f in files:
        path = os.path.join(root, f)
        filepaths.append(path)

for i, sid in enumerate(sids):
    dirpath = os.path.join(dst, str(i+ 1))
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    for f in filepaths:
        if sid in f:
            shutil.move(f, os.path.join(dirpath, ''))

