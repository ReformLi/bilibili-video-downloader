# 快速开始指南

## 🚀 3分钟快速上手

### 步骤1: 安装依赖

```bash
# 克隆或下载项目到本地
# 打开终端，进入项目目录
cd bilibili-downloader

# 安装依赖
pip install -r requirements.txt
```

### 步骤2: 准备Cookie（可选，但推荐）

1. 登录B站账号（建议使用大会员账号）
2. 按F12打开开发者工具
3. 切换到Network选项卡
4. 刷新页面
5. 在任意请求的请求头中找到Cookie字段
6. 复制Cookie内容，保存到`config/cookies.txt`文件

### 步骤3: 运行程序

```bash
# 交互式运行
python main.py

# 或直接使用示例
python example.py
```

### 步骤4: 输入信息

按照提示输入：
- Cookie文件路径（如果有）
- B站视频链接
- 画质代码（默认116=1080P60）
- 下载目录（默认./downloads）

## 🎯 常用命令

```bash
# 查看帮助
python main.py --help

# 安装为系统命令（需要先运行setup.py）
pip install .

# 使用系统命令
bilibili-downloader
```

## 📋 画质选择建议

- **普通用户**: 64 (720P) 或 32 (480P)
- **大会员**: 116 (1080P60) 或 120 (4K)
- **网络较差**: 16 (360P)

## 🔧 常见问题解决

### 问题1: FFmpeg未找到

**解决方法**:
```bash
# Windows: 下载并安装FFmpeg，添加到系统PATH
# macOS: brew install ffmpeg
# Linux: sudo apt install ffmpeg
```

### 问题2: 下载速度慢

**解决方法**:
- 检查网络连接
- 尝试使用VPN
- 降低画质设置

### 问题3: Cookie无效

**解决方法**:
- 重新获取Cookie
- 确认账号已登录
- 检查Cookie格式是否正确

## 📞 获取帮助

- 查看完整文档: `README.md`
- 查看示例代码: `example.py`
- 提交问题: 在GitHub上创建Issue

---

**🎉 现在你可以开始下载B站视频了！**