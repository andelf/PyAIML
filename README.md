# PyAIML -- The Python AIML Interpreter

## PyAIML 中文支持

中文支持维护(current maintainer): andelf (andelf AT gmail.com)

<img src="https://raw.github.com/andelf/PyAIML/master/screenshot.jpg" />

NOTE:

- 目前可以支持中文规则
- 规则库目测翻译量巨大
- 规则中请使用半角标点
- 暂时对 CJK 中的 JK 无支持
- 修正了 match() 函数的一个严重 BUG, 会导致 * 错误匹配
- 可以完美保存会话进度

Changelog:

- 2013/03/09
  - 初步中文支持完成
- 2013/03/10
  - 修复 match() BUG
  - 添加 example1 example2 两个例子
- 2013/03/12
  - 为 Kernel() 添加 session 参数
  - 添加 example3
- 2013/03/14
  - 添加 dumps(), loads() 保存 PatterMgr()

## 以下为原 README

author: Cort Stratton (cort@users.sourceforge.net)
web: http://pyaiml.sourceforge.net/

PyAIML is an interpreter for AIML (the Artificial Intelligence Markup
Language), implemented entirely in standard Python.  It strives for
simple, austere, 100% compliance with the AIML 1.0.1 standard, no less
and no more.

This is currently pre-alpha software.  Use at your
own risk!

For information on what's new in this version, see the
CHANGES.txt file.

For information on the state of development, including
the current level of AIML 1.0.1 compliance, see the
SUPPORTED_TAGS.txt file.

Quick & dirty example (assuming you've downloaded the
"standard" AIML set):

```python
import aiml

# The Kernel object is the public interface to
# the AIML interpreter.
k = aiml.Kernel()

# Use the 'learn' method to load the contents
# of an AIML file into the Kernel.
k.learn("std-startup.xml")

# Use the 'respond' method to compute the response
# to a user's input string.  respond() returns
# the interpreter's response, which in this case
# we ignore.
k.respond("load aiml b")

# Loop forever, reading user input from the command
# line and printing responses.
while True: print k.respond(raw_input("> "))
```
