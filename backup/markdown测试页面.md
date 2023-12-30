![](https://img.shields.io/badge/Markdown-8A2BE2) ![](https://img.shields.io/badge/Static_Badge-blue)  

这是一个markdown格式的测试页面，也是个人经常会使用的格式记录。

## Static Badge
```markdown
![](https://img.shields.io/badge/参考页面-orange)
```
![](https://img.shields.io/badge/参考页面-orange)

## 标题
```markdown
# H1
## H2
### H3
#### H4
```

## 强调
```markdown
今天的天气真好啊，可以吃**冰激凌**吗？
```
今天的天气真好啊，可以吃**冰激凌**吗？

## 删除横线
```markdown
今天的天气真好啊，可以吃~~冰激凌~~吗？
```
今天的天气真好啊，可以吃~~冰激凌~~吗？

## 列表
```markdown
1. 看电视
2. 吃饭
3. 睡觉

- 乒乓球
- 篮球
- 羽毛球
```
1. 看电视
2. 吃饭
3. 睡觉

- 乒乓球
- 篮球
- 羽毛球

## 代码高亮 
\`\`\`python  
import request  
import time  
  
time.sleep_ms(1000)  
print("Hello World")  
\`\`\`   
  
```python
import request
import time

time.sleep_ms(1000)
print("Hello World")
```

## 链接
```markdown
[我的博客](https://meekdai.github.io)
```
[我的博客](https://meekdai.github.io)

## 图片
```markdown
![这是我的头像](https://meekdai.com/avatar.svg)
```
![这是我的头像](https://meekdai.com/avatar.svg)

## 表格
```markdown
| Table Heading 1 | Table Heading 2 | Center align    | Right align     | Table Heading 5 |
| :-------------- | :-------------- | :-------------: | --------------: | :-------------- |
| Item 1          | Item 2          | Item 3          | Item 4          | Item 5          |
| Item 1          | Item 2          | Item 3          | Item 4          | Item 5          |
| Item 1          | Item 2          | Item 3          | Item 4          | Item 5          |
```

| Table Heading 1 | Table Heading 2 | Center align    | Right align     | Table Heading 5 |
| :-------------- | :-------------- | :-------------: | --------------: | :-------------- |
| Item 1          | Item 2          | Item 3          | Item 4          | Item 5          |
| Item 1          | Item 2          | Item 3          | Item 4          | Item 5          |
| Item 1          | Item 2          | Item 3          | Item 4          | Item 5          |

## 水平线
```markdown
---
我在2个水平线中间
***
```
---
我在2个水平线中间
***

## 引用
```markdown
> 落霞与孤鹜齐飞，秋水共长天一色。《滕王阁序》--王勃 
```
> 落霞与孤鹜齐飞，秋水共长天一色。《滕王阁序》--王勃 

## 对比
```diff
+ this text is highlighted in green
- this text is highlighted in red
```

<pre>
```diff
+ this text is highlighted in green
- this text is highlighted in red
```
</pre>

## 字体颜色
```CSS
Some text in green! 123
```

<pre>
```CSS
Some text in green! 123
```
</pre>

```P4
Some text in blue! 123
```

```Mint
Some text in blue with additional keyword highlighting! 123
```

<pre>
```P4
Some text in blue! 123
```

```Mint
Some text in blue with additional keyword highlighting! 123
```
</pre>

```JSON
Some text highlighted in red! 123
```

<pre>
```JSON
Some text highlighted in red! 123
```
</pre>

## HTML tricks

<samp>Monospaced text</samp>

```
<samp>Monospaced text</samp>
```

---

<ins>Underlined text</ins>

```
<ins>Underlined text</ins>
```

---

<table><tr><td>Boxed text</td></tr></table>

```
<table><tr><td>Boxed text</td></tr></table>
```

---

<details>
<summary>Item summary with dropdown</summary>

Dropdown content (supports **markdown** ~~yay!~~)

```json
{
  awesome: "true"
}
```
</details>

<pre>
&lt;details>
&lt;summary>Item summary with dropdown&lt;/summary>

Dropdown content (supports **markdown** ~~yay!~~)

```json
{
  awesome: "true"
}
```
&lt;/details>
</pre>

---

__*Italic-bold*__

```
__*Italic-bold*__
```

---

Superscript<sup>TM</sup>

```
Superscript<sup>TM</sup>
```

---

Superscript-italic<sup>*tm*</sup>

```
Superscript-italic<sup>*tm*</sup>
```

---

Subscript<sub>x</sub>

```
Subscript<sub>x</sub>
```

---

Subscript-bold<sub>**min**</sub>

```
Subscript-bold<sub>**min**</sub>
```

---

~~__*Italic-bold-strikethrough*__~~

```
~~__*Italic-bold-strikethrough*__~~
```

## 参考
> 更多GitHub Markdown 语法参考：https://github.com/Olwiba/Kickass-markdown/
