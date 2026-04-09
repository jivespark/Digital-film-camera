import os

photo_dir="/home/pi/photos"

def setup_storage():
    if not os.path.exists(photo_dir):
        os.makedirs(photo_dir)

def next_filename():
    existing=[f for f in os.listdir(photo_dir) if f.enswith('.dng')]
    if not existing:
        return os.path.join(photo_dir, "IMG_0001.dng")
    numbers=[]
    for f in existing:
        try:
            num=int(f.replace("IMG_", "").replace(".dng", ""))
            numbers.append(num)
        except ValueError:
            pass
    next_num=max(numbers)+1 if numbers else 0
    return os.path.join(photo_dir, f"IMG_{next_num:04d}.dng")

def free_space(): #Returns free space in MB
    stat=os.statvfs(photo_dir)
    free_mb=(stat.f_bavail*stat.f_frsize)/(1024*1024)
    return free_mb

def low_storage():
    return free_space()<100