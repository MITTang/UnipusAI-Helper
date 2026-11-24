# -*- coding: utf-8 -*-
"""打包 UnipusAI-Helper 分享包：源码 + whisper 模型 + ffmpeg + 部署说明"""
import os
import zipfile

SRC = r"D:\UnipusAI-Helper-main\UnipusAI-Helper-main"
OUT = r"D:\UnipusAI-Helper-main\UnipusAI-Helper-完整分享包.zip"
ROOT_NAME = "UnipusAI-Helper-main"

EXCLUDE_DIRS = {".venv", "__pycache__", ".git", "node_modules", "logs", "analyze_tools"}
EXCLUDE_FILES = {"config.json", "电信key.txt", "pack_share.py", "_e2e_fill_test.py",
                 "AutoUnipus-for-windows.zip", "Unipus-EXE.rar"}
EXCLUDE_PREFIXES = ("config.json.bak", "_launch_test")  # 含个人 API Key 的配置备份、启动测试日志也不打包

def main():
    if os.path.exists(OUT):
        os.remove(OUT)
    count = 0
    total = 0
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        for root, dirs, files in os.walk(SRC):
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
            for f in files:
                if f in EXCLUDE_FILES or f.startswith(EXCLUDE_PREFIXES):
                    continue
                fp = os.path.join(root, f)
                rel = os.path.relpath(fp, SRC)
                arc = os.path.join(ROOT_NAME, rel)
                zf.write(fp, arc)
                count += 1
                total += os.path.getsize(fp)
    print(f"打包完成: {count} 个文件, 原始大小 {total/1024/1024:.1f} MB")
    print(f"输出: {OUT}")
    print(f"压缩包大小: {os.path.getsize(OUT)/1024/1024:.1f} MB")

if __name__ == "__main__":
    main()
