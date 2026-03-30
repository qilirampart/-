# 帧析打包说明

## 输出形式

当前采用 `PyInstaller` 的 `onedir` 方案，生成目录为：

`dist/zhenxi`

把整个 `dist/zhenxi` 文件夹压缩成 zip 后，就可以直接发给别人使用。

## 打包命令

在项目根目录执行：

```powershell
.\build_windows.ps1 -Clean
```

## 包内结构

- `zhenxi.exe`
- `runtime/`
- `output/`
- `assets/`
- `docs/`

其中：

- `runtime/` 用于保存 API 配置、下载器配置、腾讯云 ASR 配置
- `runtime/ffmpeg/` 可放置 `ffmpeg.exe` 和 `ffprobe.exe`
- `output/` 用于保存下载结果、截图、音频和转写结果

## 分发建议

- 不要把你自己的 `runtime/*.json` 真实密钥配置打进包里
- 分发前确认 `runtime/` 内只保留 `*.example.json` 或空配置
- 如果对方机器没有系统级 `ffmpeg`，请把 `ffmpeg.exe` 和 `ffprobe.exe` 放进 `runtime/ffmpeg/`
- 轻量分发包默认不内置本地 OCR 运行时；默认推荐 API OCR
- 如果后续确实要打“本地 OCR 完整版”，建议单独出一个大体积版本，不和轻量包混发

## 验证项

发包前至少验证一次：

1. 程序能正常启动
2. 帮助说明能打开
3. 下载结果能写入 `output/`
4. 音频提取能找到 `ffmpeg`
5. API 配置和 ASR 配置能正常保存
