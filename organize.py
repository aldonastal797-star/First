import os
import shutil

# 1. 定义我们要整理的文件夹路径
# '.' 表示当前目录，这一行意思是找到当前目录下的 test_files 文件夹
target_folder = './test_files'

# 2. 检查文件夹是否存在，防止报错
if not os.path.exists(target_folder):
    print("找不到目标文件夹！请先创建 test_files 文件夹")
    exit()

# 3. 遍历文件夹里的所有文件
# os.listdir() 会列出文件夹里所有的名字
for filename in os.listdir(target_folder):
    
    # 拼接文件的完整路径
    file_path = os.path.join(target_folder, filename)
    
    # 如果是文件夹，就跳过（我们只处理文件）
    if os.path.isdir(file_path):
        continue

    # 4. 获取文件的后缀名 (比如 .jpg, .docx)
    # os.path.splitext 会把 'a.jpg' 切分成 ('a', '.jpg')
    file_extension = os.path.splitext(filename)[1].lower()

    # 5. 定义分类规则：根据后缀名决定去哪个房间
    new_folder = None
    
    if file_extension in ['.jpg', '.png', '.gif', '.jpeg']:
        new_folder = '图片'
    elif file_extension in ['.doc', '.docx', '.pdf', '.txt', '.xlsx']:
        new_folder = '文档'
    elif file_extension in ['.zip', '.rar', '.7z']:
        new_folder = '压缩包'
    else:
        new_folder = '其他'

    # 6. 开始移动！
    if new_folder:
        # 目标文件夹的完整路径，比如 ./test_files/图片
        destination_path = os.path.join(target_folder, new_folder)
        
        # 如果这个分类文件夹不存在，就自动创建一个
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)
            print(f"创建了新文件夹: {new_folder}")

        # 移动文件
        # 把 file_path 移动到 destination_path 里面
        shutil.move(file_path, os.path.join(destination_path, filename))
        print(f"已移动: {filename} -> {new_folder}")

print("自动化整理完成！")