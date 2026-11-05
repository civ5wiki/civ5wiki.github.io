# 大富翁4 · 角色语音素材包

从你本机的正版 Steam 版《大富翁4》导出。12 个角色、**1140 条发言**，每条都带音频、台词（金贝贝为图标）；其中 1116 条还带该条发言在原版中使用的情绪头像（24 条原版未使用的卡 7 台词没有对应情绪）。

## 一眼看数量

| 项目 | 数量 |
| --- | --- |
| 角色 | 12 |
| 发言条目 | 1140（其中原版实际会触发 1116，未使用 24） |
| 每个角色 | 95 条（27 事件 + 52 卡片 + 16 道具） |
| 情绪头像 | 48 种；1x 保留原版，8x/16x 为透明背景 AI 重绘版 |
| 金贝贝图标 | 21 个 |
| 音频总时长 | 约 29 分 06 秒（处理后） |
| 试听音频 | 16.63 MB（Ogg Opus / 单声道 / 48 kHz / 64 kbps VBR） |
| 无损剪辑母版归档 | 85.04 MB（可逐字节恢复全部 WAV） |

## 目录

```text
rich4-speech-pack/
├─ index.html                 ← 双击打开：搜索、试听、看头像（离线可用）
├─ index.csv                  ← Excel 可直接打开的主索引（1140 行）
├─ index.json                 ← 程序用索引（含全部字段）
├─ audio-processing.csv       ← 转码前 WAV 母版的处理结果（1140 行）
├─ characters.csv             ← 12 角色一览（含 4 张头像路径）
├─ events.csv / cards.csv / tools.csv   ← 事件槽 / 卡牌 / 道具的含义表
├─ pictograms.csv             ← 金贝贝 21 个图标的说明
├─ audio/
│   ├─ event/00_約翰喬/1050_別忌妒我！.opus
│   ├─ card/00_約翰喬/0426_有錢大家花！.opus
│   └─ tool/00_約翰喬/0236_替我除掉障礙物！.opus
├─ portrait/00_約翰喬/
│   ├─ mood0_平静.webp  … mood3_开心.webp   （发言气泡用的头像，1x）
│   ├─ mood0_平静_8x.webp …                （由 AI 重绘 16x 版缩小一半）
│   ├─ mood0_平静_16x.webp …               （AI 重绘，尺寸为原图 16 倍）
│   ├─ face_large.webp                     （原版右侧资金/状态栏的大头像）
│   └─ face_72.webp                        （选人/资料面板的 72×72 头像）
├─ pictogram/p01_爱心.webp … p21_小熊.webp   （金贝贝专用，1x + 8x + 16x）
├─ contact-sheet-moods.webp     ← 原版 12 角色 × 4 情绪速查图
├─ contact-sheet-pictograms.webp ← 原版图标速查图
└─ backups/                   ← 无损音频母版、原图备份、生图原件与转换记录
```

## 怎么用

1. **先打开 `index.html`**：顶部 12 个角色头像点一下即可筛选；也可按类别、情绪筛选，搜索台词，点行看大图并试听。
2. 在剪辑软件里按场景找素材：在 `index.csv` 搜台词或「场景」列，拿到 `audio` / `portrait` 路径。
3. `audio/` 是轻量 Opus 试听版；剪辑时使用无损母版归档恢复出的 16-bit / 48 kHz 单声道 WAV，恢复步骤见「音频规格」。
4. 情绪头像 WebP 带透明通道；`mood*_16x.webp` 为 AI 重绘版；页面详情使用缩小后的 `_8x` 版本。`mood*.webp` 原图仍保留，`mood*_8x.webp` 由对应 16x 版等比缩小一半。金贝贝图标的 `_8x` 版也由 `_16x` 高清重绘版缩小生成。

## 字段说明（index.csv）

| 字段 | 含义 |
| --- | --- |
| `id` | 1–1140 的顺序号 |
| `category` | `event` 事件 / `card` 卡片 / `tool` 道具 |
| `character` / `character_index` | 角色名 / 0–11 的顺序号 |
| `voice` | 原版 Speaking.mkf 条目号，也是音频文件名前缀 |
| `mood` / `mood_name` | 0 平静 / 1 生气 / 2 难过 / 3 开心；空 = 原版未使用 |
| `text` | 台词原文（保留原版换行） |
| `text_inline` | 把换行换成「／」的单行版，便于搜索 |
| `pictogram` / `pictogram_name` | 金贝贝的图标编号 1–21 / 描述名 |
| `pictogram_file` | 图标 WebP 路径 |
| `portrait` | 该条发言使用的情绪头像路径 |
| `audio` | 该条发言的 Opus 试听文件路径 |
| `context` | 场景：事件槽含义 / 卡名+使用方式 / 道具名 |
| `card_id` / `card_name` / `card_row` | 卡片编号、卡名、0 使用者 / 1 对自己 / 2 被针对 |
| `tool_id` / `tool_name` | 道具编号与名称（被路障/地雷/炸弹时为空的特殊行） |
| `used` | 原版是否真的会说出这句：`yes` / `no`（卡 7 的两行不会被使用） |

## 情绪头像怎么对应

原版《大富翁4》的发言气泡里，角色头像是 `map.mkf` 里的 7 帧小图：第 0 帧是大头像，第 1–4 帧就是 4 种情绪，第 5–6 帧是小图标。Steam 版的索引是 **15 + 角色号**（光盘版文档写的是 27 + 角色号，Steam 重打包后整体前移了 12 项）。

`portrait/角色/face_large.webp` 就是原版右侧资金/状态栏里的大头像（第 0 帧），`index.html` 顶部每个角色用的也是它；`face_72.webp` 是选人/资料面板的 72×72 版本；`mood0`–`mood3` 才是发言气泡里随台词变化的小头像。

| mood | 头像帧 | 文件名 | 典型场景 |
| --- | --- | --- | --- |
| 0 | frame 1 | `mood0_平静.webp` | 普通发言、买地、升级、自豪 |
| 1 | frame 2 | `mood1_生气.webp` | 复仇、被陷害、被路障/地雷挡住 |
| 2 | frame 3 | `mood2_难过.webp` | 倒霉、付钱、坐牢、住院、破产 |
| 3 | frame 4 | `mood3_开心.webp` | 进账、赢、免付、幸运转盘 |

事件发言的 mood 由事件槽固定（原版 `_rich4_player_say` 的第二个参数）；卡片/道具的 mood 由原版各卡片的调用点决定。同一句台词不会因为上下文换头像。

## 16 倍情绪头像重绘与备份

48 张 `portrait/角色/mood*_16x.webp` 使用内置 `image_gen` 生图功能重新绘制：以各角色的 `face_large.webp` 固定长相、服饰和配色，以对应 mood 小图确定表情。同一角色的平静重绘图还作为其他表情的画风参考。新文件带透明背景，尺寸保持为原 mood 小图宽高的 16 倍；生图原件分辨率更高，缩小到目标尺寸保存。

这些头像是 AI 演绎的高清版本，不是原版隐藏的高清素材；原始 1x 头像与 `face_large.webp` 均保留；8x 头像已替换为 16x 重绘版的缩小版本。原版速查图 `contact-sheet-moods.webp` 保留；重绘版可在 `index.html` 查看。`index.csv`、`index.json` 的 `portrait` 字段仍指向原图；对应的高清文件在同目录，文件名加 `_16x`。

- 修改前备份：`backups/mood-before-ai-20261104-102346.zip`，包含原头像、原速查图、索引与说明，包内有 SHA-256 校验清单。
- 最终高分辨率生图原件、逐张提示词与校验记录：`backups/redraw-sources-20261105.zip`。解压到单独目录后，头像原件在 `artifacts/mood-redraw-20261104/generated/`；归档根目录的 `manifest.json` 记录转换前 16x PNG 的尺寸、SHA-256 和 RGBA 像素校验值。
- 恢复旧头像：先将备份解压到单独目录，取其中的 48 张 `mood*_16x.png`，转换为无损 WebP 后覆盖当前对应 `.webp` 文件。

## 金贝贝

金贝贝（角色号 11）没有文字台词，原版把 `#NNNN@MM` 里的 `@MM` 画成 `Data.mkf` 的图标。Steam 版这组图标在 **Data.mkf 条目 478**，共 21 帧；`@01`–`@21` 对应第 0–20 帧，已导出为 `pictogram/p01…p21`。她的 95 条发言全部有音频，索引里 `pictogram` 列就是图标号。

## 16 倍 pictogram 重绘与备份

21 个 `pictogram/pNN_*_16x.webp` 使用内置 `image_gen` 按原图重新绘制，保留图形含义、配色、表情和符号数量。项目中的正式文件为透明 WebP，宽高保持为原图的 16 倍；先裁去生图画布的透明留白，再等比缩小到目标画布，不拉伸图形。原始 1x 文件与原版速查图均保留；8x 图标已由对应 16x 重绘版缩小生成。

页面表格和详情使用由 16x 重绘版缩小生成的 8x 图标，详情中会放大显示。`index.json` 的 `pictograms` 项提供 `file_16x` 和 `size_16x`；发言记录中的 `pictogram_file` 仍指向原图，`pictograms.csv` 的 `file_16x` 列可直接找到高清文件。

原图的省略号为五个点，脏话符号顺序为 `O × # △ @`，睡觉图标为逐渐变大的 `z · Z · Z`。`p16_兔子` 实际绘制金色 V 字手势，本次按手势重绘，并保留旧文件名和索引名称以兼容现有路径。

- 修改前备份：`backups/pictogram-before-ai-20261104-191242.zip`，包含全部原图标、索引和说明，并附 SHA-256 清单。
- 最终生图原件、提示词与校验记录：`backups/redraw-sources-20261105.zip`。解压后，图标原件在 `artifacts/pictogram-redraw-20261104/generated/`；归档根目录 `manifest.json` 是转换前的 16x PNG 文件清单。
- 恢复旧版：先将备份解压到单独目录，取其中的 21 张 `_16x.png`，转换为无损 WebP 后覆盖当前对应图标。

## 8 倍图片版本与页面引用

48 张 `portrait/角色/mood*_8x.webp` 和 21 张 `pictogram/pNN_*_8x.webp` 均由当前对应的 16x 重绘版按宽高各 50% 缩小，采用 Lanczos 重采样，保留透明通道。尺寸仍为原始小图的 8 倍。12 张 `face_large_8x.webp` 没有对应 16x 文件，保持原版。

替换前的 8x PNG 已逐文件核对，分别完整保存在 `backups/mood-before-ai-20261104-102346.zip` 和 `backups/pictogram-before-ai-20261104-191242.zip`。恢复时先解压到单独目录，再将所需 `_8x.png` 转为无损 WebP 后取用。

| 页面位置 | 实际引用 |
| --- | --- |
| 顶部角色筛选头像 | 原版 `face_large.webp` |
| 表格里的小情绪头像 | 原版 `mood*.webp`（1x） |
| 发言详情的情绪头像 | AI 重绘缩小版 `mood*_8x.webp` |
| 表格及详情的金贝贝情绪符号 | AI 重绘缩小版 `pNN_*_8x.webp` |

页面原先引用 16x 的情绪头像和 pictogram 现均使用 8x 版本，减少图片加载体积。

## 图片压缩与清理

转为 WebP 前，69 张正式 16x PNG 已做无损压缩，从 17.37 MB 减至 17.05 MB（减少 1.86%）。逐张解码核对尺寸和 RGBA 像素，并保留全部 PNG 非图像数据块，包括原有色彩元数据；69/69 一致。没有减色或更改透明度。

新增的两张重绘速查图、失败生图、重复修订图片及四份中间修订备份已清理。最终采用的 69 张高分辨率生图原件、提示词和历史 JSON 记录合并为 `backups/redraw-sources-20261105.zip`；两份重绘前原版素材备份继续单独保留。归档内的历史 JSON 是清理前快照，其中旧修订图片及旧备份路径仅作为历史记录；该归档的文件校验值为 WebP 转换前的 PNG 快照；当前 WebP 校验值见下方转换记录。

## WebP 无损转换

项目中的 305 张 PNG 已全部转换为无损 WebP，图片合计从 23.32 MB 减至 16.29 MB（减少 30.15%）。逐张解码比对尺寸及 RGBA 字节，305/305 完全一致，包括完全透明区域内的 RGB 值；没有调整尺寸、减色或有损压缩。

页面、`index.json` 和三个含图片路径的 CSV 已同步改为 `.webp`。页面详情头像及 pictogram 继续使用 8x 版本，表格小头像及顶部角色头像的版本不变。WebP 使用与原图相同的 sRGB 色彩；原 PNG 元数据保存在转换记录中。

已有两份重绘前 PNG 备份与最终生图 PNG 原件归档继续保留。本次转换记录及转换前的页面、索引和说明保存在 `backups/webp-conversion-20261105.zip`，无需重复存放全套 PNG。需要当前图片的 PNG 版时，解压记录包，在安装 Pillow 的 Python 环境中运行包内 `restore-png.py`：

```sh
python3 restore-png.py --manifest manifest.json --webp-root /path/to/rich4-speech-pack --output /path/to/export-png
```

导出目录须独立于项目。导出会恢复完全相同的像素与原 PNG 元数据，PNG 压缩字节可能不同。历史 ZIP 内保留原 PNG 文件名；当前 WebP 的尺寸、SHA-256 与像素校验值以转换记录中的 `manifest.json` 为准。

## 数据来源与校验

- 游戏目录：`E:\SteamLibrary\steamapps\common\rich4\Game`
- 台词：直接从 `rich4.exe` 的 `#NNNN` 字符串表读取，并与本仓库移植表逐条比对：**1140/1140 完全一致**。
- 语音来源：从 `Speaking.mkf` 提取对应条目，先做 Broadcast+EQ 生成 WAV 母版，再编码为 `audio/` 中的 Opus 试听版；处理步骤与输出规格见下方「音频规格」。
- 头像：`map.mkf` 15–26 号条目，每角色 7 帧；金贝贝图标：`Data.mkf` 478 号。
- 检查过：1140 条 Opus 均可完整解码，采样率、声道和有效样本数与 WAV 母版一致；1140 条无损母版均可逐字节恢复为原 WAV。1116 条有情绪头像，95 条金贝贝发言有图标；24 条卡 7 未使用行没有头像。

源文件 SHA-256：

- `rich4.exe`：`110b29f9d2fadcff3836eb69ec380aa264951859c90955da6e11158d2f956a13`
- `Speaking.mkf`：`0f43530b45a3286d1681f7a676c440864bc2f5734ab41c2f3763b4e3f8bbfb19`
- `map.mkf`：`717aaa1c1becf277064d29772500027427d39488bad64a7ee42875975c0e7106`
- `Data.mkf`：`c63023e815b1ad4bef172b6415d128c7f041f12b71b5d80dc3ff29240a0a1988`

## 音频规格

- 原始：8-bit 单声道，22050 Hz（950 条）或 44100 Hz（190 条）；本包未附原始 WAV。
- 剪辑母版：统一做 **Broadcast + EQ** 处理，输出 16-bit PCM / 48 kHz / 单声道 WAV：
  - FFT 降噪 10 dB、高通 75 Hz、低通 10/16 kHz；
  - 掐头去尾、6 ms 淡入淡出；
  - 检测到削波的 127 条做 de-clip；
  - 300 Hz / Q0.8 / -1.5 dB 宽峰衰减（覆盖 250–400 Hz，去闷）；
  - 2.5:1 轻压缩、目标 -16 LUFS、限幅 -1.5 dBTP。
- WAV 母版实测：中位 -16.0 LUFS，真峰值最高 -1.6 dBTP；61 条 <0.4 秒的短句积分响度不适用，39 条峰值受限/语气偏轻的句子低于 -16 LUFS，逐条见 `audio-processing.csv`。
- 原始 8-bit 音源的上限仍在，处理不是“还原”。


- 试听版：由 WAV 母版编码为 **Ogg Opus（`.opus`）、目标 64 kbps、48 kHz 单声道、VBR**，采用 libopus 1.5.2、20 ms 帧、复杂度 10。未再次归一化或裁剪音频。1140 条共 16.63 MB，比原 WAV 的 167.69 MB 减少 90.09%。Opus 是有损试听版。
- 校验：逐页检查 Ogg 校验和、序号和结束位置；用独立的 libsndfile 解码，1140/1140 的采样率、声道及有效样本数与母版一致，编码延迟和尾部填充通过 Opus pre-skip 与最终 granule 正确裁去。
- 无损母版：`backups/audio-wav-masters-20261105.zip`（85.04 MB）。内含全部母版的 FLAC 无损压缩文件及原 WAV 元数据；已全部导回 WAV，1140/1140 的整文件 SHA-256 与转换前一致。归档中的 `manifest.json` 同时记录 WAV、FLAC 和 Opus 校验值。
- `audio-processing.csv` 保持原始处理记录，`audio` 列为归档内母版恢复后的 WAV 路径；其中字节数、LUFS、峰值等数据适用于 WAV 母版。当前试听路径以 `index.csv` / `index.json` 的 `audio` 字段为准。

恢复剪辑用 WAV：先把母版 ZIP 解压到单独目录，准备好 `flac` 命令行工具，在解压目录执行：

```sh
python3 restore-wav.py --output /path/to/wav-export
```

脚本会恢复原有 `audio/` 目录和 `.wav` 文件名，逐条核对 SHA-256，并拒绝覆盖已有文件。使用独立导出目录即可保留轻量试听包。页面播放需要支持 Ogg Opus 的浏览器；Safari 需 18.4 或更新版本。

## 已知限制

- 音频已按 Broadcast+EQ 处理；短句和峰值受限的个别句子会有响度偏差，逐条标注在 `audio-processing.csv`，需要更严格一致时可再做角色级增益。
- 游戏原始 8-bit 音频备份与校验清单未随包提供；这与本次完整保存的处理后 WAV 母版不同。旧导出记录中的文件名为 `rich4-speech-pack-original-20261104-2250.zip` 和 `audio-original-manifest.csv`；`index.json` 及页面内嵌索引的 `meta.audio.backup`、`meta.audio.backup_manifest` 均为 `null`。需要原始音频时，须先取得原始备份，或从正版游戏文件重新提取；无法从本包已处理的音频还原原始音源。
- 卡片 7（改建卡）的「对自己」「被针对」两行在原版里没有任何调用点（本仓库审计结论），12 角色共 24 条；这些行已保留但标为 `used=no`，mood 与 portrait 为空。
- 情绪名「平静/生气/难过/开心」和图标名（爱心、气球、奶瓶……）都是按画面写的描述性命名，不是官方文案。
- Steam 版与 2000 年代光盘版的 MKF 打包顺序不同：光盘版文档里的 `map 27–38`、`Data 519` 在 Steam 版分别是 `map 15–26`、`Data 478`。本包按你的 Steam 文件实际定位。
- 台词保留了原版的异体字、全角标点和「～」；没有转成简体。
- 未包含商店店员、银行、新闻播报、命运等非角色语音；那部分在 `Speaking.mkf` 0–233。

## 重新生成

当前目录是导出的素材包，未包含原始提取与 Broadcast+EQ 处理脚本；本次 Opus 编码器源文件保存在音频母版归档的 `encoder/` 中。此前使用的脚本为 `artifacts/pack_common.py`、`artifacts/build_pack.py` 和 `artifacts/process_pack_audio.py`（Broadcast+EQ）。

重新导出前，需补齐上述脚本及正版 Steam 游戏源文件，再按实际游戏目录调整 `pack_common.py` 中的 `STEAM` 路径。游戏源文件的校验值见「数据来源与校验」；仅凭当前目录无法重现原始提取和音频处理过程。

---

《大富翁4》© 1998–2022 SOFTSTAR ENTERTAINMENT INC. 本项目与官方无关。
