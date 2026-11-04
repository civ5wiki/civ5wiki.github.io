#!/usr/bin/env python3
"""为 docs/ 下的每个条目页生成旧地址跳转页（X.php.htm -> X.htm）。

GitHub Pages 不能配置服务端重定向，因此在旧地址上放置一个极小的 HTML
跳转页：<meta http-equiv="refresh"> 与 location.replace() 双保险，
响应码仍为 200，老链接与书签可以继续使用。

用法：
    python3 tools/gen_redirects.py
"""
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs"

STUB = """<!DOCTYPE html>
<html lang="zh-cn">
<head>
<meta charset="utf-8">
<title>页面地址已更新</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="{target}">
<meta http-equiv="refresh" content="0; url={target}">
<script>location.replace("{target}");</script>
</head>
<body style="background:#000;color:#ffffc8;font:13px Verdana,Arial,sans-serif">
<p>此页面地址已更新，正在跳转到 <a href="{target}" style="color:#ffffc8">{target}</a>。</p>
</body>
</html>
"""


def main() -> None:
    pages = sorted(p for p in DOCS.glob("*.htm") if not p.name.endswith(".php.htm"))
    if not pages:
        sys.exit(f"未在 {DOCS} 找到条目页")

    created = updated = 0
    for page in pages:
        stub = DOCS / f"{page.stem}.php.htm"
        body = STUB.format(target=page.name)
        if stub.exists():
            if stub.read_text(encoding="utf-8") != body:
                stub.write_text(body, encoding="utf-8")
                updated += 1
        else:
            stub.write_text(body, encoding="utf-8")
            created += 1

    # 指向已删除条目的旧跳转页：只提示，不自动删除，避免误删
    stale = [
        p.name
        for p in DOCS.glob("*.php.htm")
        if not (DOCS / (p.name[: -len(".php.htm")] + ".htm")).exists()
    ]
    print(f"条目页 {len(pages)} 个，新建跳转页 {created} 个，更新 {updated} 个")
    if stale:
        print("以下跳转页的目标已不存在：")
        for name in stale:
            print("  ", name)


if __name__ == "__main__":
    main()
