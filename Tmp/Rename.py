import os

def get_latest_file(extension):
    files = [file for file in os.listdir() if file.endswith(extension)]
    if not files:
        return None
    latest_file = max(files, key=lambda x: os.path.getctime(x))
    return latest_file

# 获取最新创建日期的.lrc文件名
lrc_file = get_latest_file('.lrc')
if not lrc_file:
    print("当前目录下不存在.lrc文件")
    exit()

# 获取最新创建日期的.lrc文件的基本名称（不包含扩展名）
lrc_file_base_name = os.path.splitext(lrc_file)[0]

# 获取最新创建日期的.mp3文件名
mp3_file = get_latest_file('.mp3')
if not mp3_file:
    print("当前目录下不存在.mp3文件")
    exit()

# 获取最新创建日期的.jpg或.png文件名
image_extensions = ('.jpg', '.png')
image_file = None
for ext in image_extensions:
    image_file = get_latest_file(ext)
    if image_file:
        break
if not image_file:
    print("当前目录下不存在.jpg或.png文件")
    exit()

# 生成新的文件名
new_mp3_file = lrc_file_base_name + '.mp3'
new_image_file = lrc_file_base_name + os.path.splitext(image_file)[1]

# 重命名文件
os.rename(mp3_file, new_mp3_file)
os.rename(image_file, new_image_file)

print("重命名成功！")
