# 文明5在线百科

《文明5》中文百科的静态镜像站：<https://civ5wiki.github.io/>

本站存档「文明5在线百科」汉化版，内容对应「新奇世界（Brave New World）」资料片
v1.0.3.276，汉化数据更新于 2014-12-25。共 1562 个条目页，涵盖游戏概念、科技、
单位、晋升、建筑、奇观、社会政策、伟人、文明与领袖、城邦、地形、资源、地域设施、
宗教、世界议会等 15 个栏目。

## 目录结构

```
docs/                    # GitHub Pages 站点根目录（提交即发布）
├── index.html           # 首页
├── *.htm                # 条目页，如 TECH_SAILING.htm
├── *.php.htm            # 旧地址跳转页（自动生成，勿手工编辑）
├── images/              # 图片资源（WebP）
├── styles.css           # 样式
├── skinnytip.js         # 悬停提示脚本
└── .nojekyll            # 关闭 GitHub Pages 的 Jekyll 处理
tools/gen_redirects.py   # 重新生成旧地址跳转页
```

## URL 约定

- 条目页：`/TECH_SAILING.htm`（相对链接，无前导斜杠，可直接托管在任意子路径下）
- 旧地址：`/TECH_SAILING.php.htm` 保留为跳转页，用 `<meta http-equiv="refresh">`
  与 `location.replace()` 跳到新地址，响应码仍为 200，老链接和书签不会失效。

GitHub Pages 不支持服务端重定向，因此跳转页是随站点一起提交的静态文件。新增或删除
条目页后运行：

```bash
python3 tools/gen_redirects.py
```

## 本地预览

```bash
python3 -m http.server 8000 --directory docs
# 打开 http://localhost:8000/
```

## 资源与体积

`docs/images/` 已从 PNG 统一转为 WebP（质量 85，透明通道无损），图片体积由
55.4MB 降至 9.7MB，页面引用全部指向 `.webp`。原始 PNG 仍保存在 git 历史中，
需要时可从历史版本取回。

站点同时清理了 Teleport Ultra 抓取残留（`tppabs` 属性、`/*tpa=*/` 注释、损坏的
`javascript:if(confirm(...))` 跳转脚本），HTML 体积减少约 25MB。

## 维护说明

- 无构建步骤：修改 `docs/` 后直接提交，GitHub Pages 会发布该目录；`.nojekyll`
  让 Pages 跳过 Jekyll 处理，加快发布并避免误处理大量静态文件。
- 条目页的 `<title>` 目前仍是栏目名（如「文明5在线百科: 科技」），具体条目名在页面
  内的 `.title` 元素中；这是抓取时的历史遗留。
- 站点为 1024px 固定宽度布局，面向桌面浏览器。

## 内容来源与版权

- 游戏素材、界面设计与文本版权归 Firaxis Games / 2K 所有；本站仅作非商业性的
  资料存档与检索用途，不含游戏本体。
- 中文内容基于[塞爱维·文明联盟](https://tieba.baidu.com/f?kw=%E6%96%87%E6%98%8E%E8%81%94%E7%9B%9F)
  与[游翔·天邈](http://www.591danji.com/)联合制作的文明5汉化包。
- 页面由 [dndjunkie.com](http://www.dndjunkie.com/civilopedia/) 的 Nebular 程序
  生成（Civilopedia）。
- 如版权方认为本站内容不妥，请提交 issue，我们会配合处理。
