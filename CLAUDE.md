# 项目说明

静态个人学术主页,通过 GitHub Pages 部署。无构建步骤,HTML/CSS 原样发布。

## CSS 缓存穿透规则(重要)

每次修改 `stylesheet.css` 后,必须递增 `index.html` 中样式表链接的版本号:

```html
<link rel="stylesheet" type="text/css" href="stylesheet.css?v=2">
```

当前版本:`?v=2`

- 原因:论文缩略图的 `<img>` 标签没有 `width` 属性,尺寸完全依赖 CSS 控制。如果访客浏览器缓存了旧版 CSS 而加载了新版 HTML,图片会按原始尺寸(700~1900px 宽)渲染,撑破版面。
- 操作方法:每次改动 `stylesheet.css` 时,在同一次提交中把 `?v=N` 递增为 `?v=N+1`,并同步更新上面的"当前版本"。
