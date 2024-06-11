'''
因为我不想直接用.txt文件安装导致我的老包被覆盖掉，所以我就把没安装的包（不考虑版本号，有就算安装）打印出来，再安装
新的文件为requirements_1.txt
'''

# 假设 requirements.txt 是你的依赖文件
import subprocess

not_installed = []

with open('./requirements_1.txt') as f:
    lines = f.readlines()

for line in lines:
    # 去除每行的前后空白字符，包括换行符
    line = line.strip()
    # 跳过空行和注释行
    if not line or line.startswith('#'):
        continue

    # 分离包名和版本号
    if '==' in line:
        package_name, version = line.split('==', 1)
    elif '>' in line or '<' in line:
        package_name, version = line.split('>', 1)[0], None  # 对于大于或小于的比较，不记录版本号
    else:
        package_name, version = line, None

    # 使用 subprocess 调用 pip show 命令检查包是否安装
    process = subprocess.run(["pip", "show", package_name], capture_output=True, text=True)

    # 检查命令是否执行成功
    if process.returncode != 0:
        # 如果包未安装，只记录包的声明（包括版本号）
        not_installed.append(line)

# 最后打印未安装的包及其版本号
if not_installed:
    print("\nPackages not installed:")
    for package in not_installed:
        print(package)
else:
    print("\nAll packages are installed.")