import shutil, os

with open('sid.txt', 'r') as input_f:
    sids = input_f.readlines()
sids = [i.strip() for i in sids]

dst = 'asg2-moss'
src = 'asg2'
filepaths = []
for root, dirs, files in os.walk(src):
    for f in files:
        path = os.path.join(root, f)
        filepaths.append(path)

if not os.path.exists(dst):
    os.mkdir(dst)

for i, sid in enumerate(sids):
    dirpath = os.path.join(dst, sid)
    for f in filepaths:
        if sid in f and not f.endswith('.txt'):
            if not os.path.exists(dirpath):
                os.mkdir(dirpath)
            if not (f.endswith('.zip') or f.endswith('.rar') or f.endswith('.7z')):
                print(sid)
            shutil.copy(f, os.path.join(dirpath, ''))
