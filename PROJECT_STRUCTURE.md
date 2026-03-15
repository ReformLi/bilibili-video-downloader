# 项目结构说明

## 📁 项目结构

```
bilibili-downloader/
├── bilibili_downloader/           # 核心包目录
│   ├── __init__.py               # 包初始化文件
│   └── downloader.py             # 核心下载模块
├── config/                       # 配置文件目录
│   └── cookies.txt              # Cookie文件
├── bin/                          # 二进制文件目录
│   └── ffmpeg/                   # FFmpeg工具
│       └── bin/
│           └── ffmpeg.exe       # FFmpeg可执行文件
├── main.py                       # 程序入口点
├── example.py                    # 使用示例
├── test_project.py              # 项目测试脚本
├── README.md                    # 项目说明文档
├── QUICKSTART.md               # 快速开始指南
├── PROJECT_STRUCTURE.md         # 项目结构说明（本文件）
├── requirements.txt            # 依赖文件
├── setup.py                    # 安装脚本
├── .gitignore                  # Git忽略文件
├── config.example.json         # 配置文件示例
└── downloads/                  # 默认下载目录（运行时创建）
```

## 📄 文件说明

### 核心文件

- **`bilibili_downloader/__init__.py`**: 包初始化文件，定义版本和作者信息
- **`bilibili_downloader/downloader.py`**: 核心下载模块，包含BilibiliDownloader类
- **`main.py`**: 命令行入口点，提供交互式用户界面

### 文档文件

- **`README.md`**: 完整的项目说明文档
- **`QUICKSTART.md`**: 快速开始指南
- **`PROJECT_STRUCTURE.md`**: 项目结构说明（本文件）

### 示例和测试

- **`example.py`**: 使用示例代码
- **`test_project.py`**: 项目结构和功能测试

### 配置和依赖

- **`requirements.txt`**: Python依赖包列表
- **`setup.py`**: Python包安装脚本
- **`config.example.json`**: 配置文件示例
- **`.gitignore`**: Git版本控制忽略文件

## 🚀 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行程序

```bash
# 交互式模式
python main.py

# 查看示例
python example.py

# 运行测试
python test_project.py
```

### 安装为系统包

```bash
# 安装到系统
pip install .

# 使用系统命令
bilibili-downloader
```

## 🔧 核心类说明

### BilibiliDownloader类

主要方法：

- `__init__(cookies_file=None)`: 初始化下载器
- `download(url, output_dir='./downloads', quality=116)`: 下载视频
- `get_cid(url)`: 获取视频CID
- `get_play_url(bvid, cid, quality=116)`: 获取播放地址
- `get_available_quality(bvid, cid)`: 获取可用画质列表

## 📊 项目特点

### ✅ 功能特性

- 支持多种画质选择
- 自动检测可用画质
- 支持大会员高清视频
- 自动合并音视频流
- 下载进度显示
- 错误处理和重试机制

### 🛡️ 代码质量

- 完整的文档字符串
- 类型提示（可选）
- 异常处理
- 模块化设计
- 可测试性

### 📝 项目规范

- 遵循PEP 8代码风格
- 使用UTF-8编码
- 包含完整的文档
- 提供示例和测试
- 支持Python 3.7+

## 🎯 使用场景

- 个人学习和研究
- 离线观看B站视频
- 视频内容备份
- 教育用途

## ⚠️ 注意事项

- 请遵守B站的使用条款
- 仅用于个人学习和研究
- 请勿用于商业用途
- 注意版权保护

## 📞 获取帮助

1. 查看 `README.md` 获取完整文档
2. 查看 `QUICKSTART.md` 快速上手
3. 运行 `python test_project.py` 测试项目
4. 查看 `example.py` 学习使用方法

---

**项目版本**: 1.0.0
**最后更新**: 2026/3/14
**作者**: reformLi