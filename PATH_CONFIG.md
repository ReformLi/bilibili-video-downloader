# 路径配置说明

## 📁 项目目录结构

```
bilibili-downloader/
├── bilibili_downloader/           # Python包
├── config/                       # 配置文件目录
│   └── cookies.txt              # B站Cookie文件
├── bin/                          # 二进制文件目录
│   └── ffmpeg/                   # FFmpeg工具
│       └── bin/
│           ├── ffmpeg.exe       # FFmpeg主程序
│           ├── ffplay.exe       # FFmpeg播放器
│           └── ffprobe.exe      # FFmpeg分析工具
├── downloads/                   # 下载目录（运行时创建）
└── 其他文件...
```

## 🔧 路径配置

### 1. Cookie文件路径

**位置**: `./config/cookies.txt`

**说明**:
- 用于存储B站登录Cookie
- 支持大会员高清视频下载
- 如果文件不存在或无效，将使用游客模式

**获取方法**:
1. 登录B站账号（建议大会员）
2. 按F12打开开发者工具
3. 切换到Network选项卡
4. 刷新页面
5. 在任意请求的请求头中找到Cookie字段
6. 复制Cookie内容到`config/cookies.txt`文件

### 2. FFmpeg路径

**位置**: `./bin/ffmpeg/bin/ffmpeg.exe`

**说明**:
- 用于合并音视频流
- 支持高清视频格式处理
- 如果不存在，程序会尝试使用系统PATH中的ffmpeg

**下载方法**:
- 官方地址: https://ffmpeg.org/download.html
- 推荐下载Windows完整版本
- 解压到`bin/ffmpeg/`目录

### 3. 下载目录

**默认位置**: `./downloads/`

**说明**:
- 视频下载保存目录
- 程序运行时自动创建
- 可以在运行时指定其他目录

## 🛠️ 代码中的路径使用

### BilibiliDownloader类

```python
# Cookie文件路径
cookies_file = "./config/cookies.txt"
downloader = BilibiliDownloader(cookies_file=cookies_file)

# FFmpeg路径（自动检测）
ffmpeg_path = "./bin/ffmpeg/bin/ffmpeg.exe"  # 优先使用
ffmpeg_path = "ffmpeg"  # 回退到系统PATH

# 下载目录
download_dir = "./downloads"  # 默认目录
downloader.download(url, output_dir=download_dir, quality=116)
```

### 命令行使用

```bash
# 使用默认路径
python main.py

# 指定Cookie文件
python main.py
# 输入: ./config/cookies.txt

# 指定下载目录
python main.py
# 输入: /path/to/your/downloads
```

## 🔍 路径验证

运行路径测试脚本验证配置：

```bash
python test_paths.py
```

**预期输出**:
```
BiliDownloader 路径配置测试
==================================================
测试项目路径配置...
========================================
+ config目录存在: ./config
+ cookies.txt存在: ./config/cookies.txt
+ cookies.txt有内容: 1264 字符
+ bin目录存在: ./bin
+ ffmpeg.exe存在: ./bin/ffmpeg/bin/ffmpeg.exe
+ ffmpeg.exe大小: 83.7 MB
========================================
所有路径测试通过

测试ffmpeg功能...
========================================
+ ffmpeg版本: ffmpeg version 2025-03-10-git-...
==================================================
所有测试通过！路径配置正确。
```

## ⚠️ 常见问题

### 问题1: Cookie文件路径错误

**症状**: "Cookie文件不存在"或"Cookie无效"

**解决方法**:
1. 确认`config/cookies.txt`文件存在
2. 检查文件内容是否正确
3. 重新获取Cookie并保存

### 问题2: FFmpeg路径错误

**症状**: "未找到ffmpeg"或"合并失败"

**解决方法**:
1. 确认`bin/ffmpeg/bin/ffmpeg.exe`文件存在
2. 检查文件是否完整（约80MB）
3. 尝试重新下载FFmpeg
4. 或者安装FFmpeg到系统PATH

### 问题3: 下载目录权限问题

**症状**: "无法创建目录"或"写入失败"

**解决方法**:
1. 检查目录权限
2. 使用绝对路径
3. 确保有足够的磁盘空间

## 📝 配置示例

### config.example.json

```json
{
  "default_settings": {
    "cookies_file": "./config/cookies.txt",
    "output_dir": "./downloads",
    "default_quality": 116
  },
  "paths": {
    "config_dir": "./config",
    "bin_dir": "./bin",
    "downloads_dir": "./downloads"
  }
}
```

## 🎯 最佳实践

1. **保持目录结构**: 不要随意移动config和bin目录
2. **备份Cookie**: 定期备份`config/cookies.txt`文件
3. **更新FFmpeg**: 定期检查FFmpeg更新
4. **清理下载**: 定期清理`downloads/`目录
5. **版本控制**: 将config和bin目录添加到.gitignore

---

**最后更新**: 2026/3/15
**版本**: 1.0.0