import os
from tqdm import tqdm

folder_path = '..\SelfMusics'  # 替换为实际的文件夹路径

# 清空name.txt文件内容
with open('README.md', 'w') as output_file:
    pass

# 获取目录下所有文件夹的名字
folder_names = [name for name in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, name))]
folder_names.remove('.git')
folder_names.remove('AIMP')
folder_names.remove('Tmp')

mp3_files = []

output_file = open('README.md', 'a',encoding='utf-8')

# 遍历每个文件夹，获取子目录中后缀为.mp3的文件名
for folder_name in tqdm(folder_names, desc='读取文件夹'):
    output_file.write('\n' + '---' + '\n' + folder_name + '\n --- \n' + '---' + '\n')
    subfolder_path = os.path.join(folder_path, folder_name)
    for root, dirs, files in os.walk(subfolder_path):
        for file in tqdm(files,desc='开始写入目录'+folder_name+'中的文件'):
            if file.endswith('.mp3'):
                mp3_files.append(file)
                filename = file.strip('.mp3')
                output_file.write('- ' + filename + '\n')

print("文件名已写入name.txt。")

output_file.close();


