# Course review计划

此翻译项目旨在完成 HuggingFace Course的review，提供出版级别质量的译文。

# 1.项目分析

## 1.1 工程量分析

| title                   | words  | rate     | 工期    |
| ----------------------- | ------ | -------- | ------- |
| 0. 安装                 | 3113   | 1        |         |
| 1. Transformer 模型     | 34920  | 11.21748 |         |
| 2. 使用 🤗 Transformers | 45954  | 14.76197 |         |
| 3. 微调一个预训练模型   | 36018  | 11.57019 |         |
| 4. 分享你的模型和标记器 | 29496  | 9.475104 | 6月7日  |
| 5. 🤗 Datasets库        | 80512  | 25.86315 |         |
| 6. 🤗 Tokenizers库      | 101183 | 32.50337 | 6月14日 |
| 7. 主要的 NLP 任务      | 211903 | 68.07035 | 6月21日 |
| 8. 如何寻求帮助         | 52097  | 16.7353  |         |
| 9. 构建并分享你的模型   | 44034  | 14.1452  |         |
| 课程活动                | 5464   | 1.75522  | 6月30日 |
| 总计                    | 644694 | 207.0973 |         |

# 2. 项目实施方案

## 2.1 人员招募与组织

1. 译者：寻找具备 NLP、深度学习或相关领域背景的译者，确保他们能理解专业术语并准确翻译。(同学,志愿者)
2. 校对者：对译文进行审查，确保质量。
3. 管理者：负责项目的整体进度和质量把控。
4. 特邀审稿人：邀请NLP专业领域的人和面向的入门读者进行阅读，给出建议。

#### 2.2 时间规划

1. 招募阶段：2 周
2. 翻译阶段：10 周（预计每周翻译约 6.4 万字）
3. 审稿阶段：2 周
4. 修改与整理阶段：1 周

Project: [Translate project (github.com)](https://github.com/orgs/huggingface-cn/projects/7/views/1)

## 2.3 工作协作

其中，⼤分⽀可分为：master(主分⽀)、review(校审分⽀)、translate1(翻译分⽀)以及最后的hotfix(热修复分⽀)

| 分⽀      | 作⽤                                                                                                        |
| --------- | ----------------------------------------------------------------------------------------------------------- |
| master    | 作为最终的代码存放分⽀，⼀切bug处理后且运⾏达到预期效果才可通过提交PR的⽅式推送到该分⽀                     |
| review    | 作为校审分⽀，最后测试⽆误且稳定达到预期效果后推到master分⽀                                                |
| translate | 初次翻译分支，需要修改的工作量最大，翻译和自查之后推到review分⽀                                            |
| hotfix    | 热修复分⽀，⼀旦master分⽀出现bug，必须⻢上合并(merge)到该分⽀进⾏修复，修复完毕后再合并(merge)到master分⽀ |

## 2.4 工作流程

### 2.4.1 初始化任务

1. 找负责人1375626371@qq.com登记翻译人信息，以及每周可以参与翻译的大概时间，拉入群。
2. Fork Brach
3. 学习翻译规范
4. 安装准备对应的环境，软件

### 2.4.2 每周的工作

1. 认领project（微信）
2. Git Fetch
3. 翻译
   术语提示检查

   - 将 `utils/glossary_hint.py` 中的文件名改为自己翻译的文件名，然后运行得到代码参考。

   翻译

   - 将文件后缀由mdx改为md，就可以使用Office Viewer(Markdown Editor)编辑了
   - 翻译的过程要遵循术语规范、语言规范和排版规范

   格式检查

   - 将 `utils/format_tools.py` 中的文件路径改为自己翻译文件的路径，运行并选择对应的格式化过程
   - 审核在翻译文件路径生成的对应的fix文件，确认无误之后替换原文件
4. 质量检查
5. Push and PR

# 3.翻译规范

## 3.1 术语规范规范

### 3.1.1 规范流程

术语提出—>方案征集—>投票表决—>术语归档

* 术语提出：由译者在 Github 上提出 Issues。
* 方案征集：所有的译者要及时给出自己的建议翻译和理由（包括不译）。
* 投票表决：2天之后由管理者发起投票，确定最后的翻译。
* 术语归档：由管理者根据得票最多的翻译，进行归档到 glossary.md

### 3.1.2 可能出现的术语

Course中出现的术语大概可以分为以下及各类别：

1. 基础概念与技术：这类术语涉及自然语言处理的基本理论、方法和技术，例如分词（Tokenization）、词性标注（Part-of-Speech Tagging）、命名实体识别（Named Entity Recognition）等。
2. 机器学习与深度学习：这类术语与机器学习、深度学习算法和模型相关，例如神经网络（Neural Networks）、循环神经网络（Recurrent Neural Networks, RNN）、卷积神经网络（Convolutional Neural Networks, CNN）等。
3. NLP 模型与架构：这类术语与自然语言处理领域的经典模型和架构有关，例如 Seq2Seq（Sequence-to-Sequence）、Transformer、BERT（Bidirectional Encoder Representations from Transformers）等。
4. 评价指标：这类术语与自然语言处理任务的评价方法和指标相关，例如准确率（Accuracy）、召回率（Recall）、F1 分数（F1 Score）、BLEU 分数（Bilingual Evaluation Understudy）等。
5. 任务与数据集：这类术语与自然语言处理的具体任务和常用数据集相关，例如机器翻译（Machine Translation）、文本分类（Text Classification）、情感分析（Sentiment Analysis）、问答系统（Question Answering）等。
6. 工具与框架：这类术语与自然语言处理领域的软件工具和开发框架有关，例如 NLTK（Natural Language Toolkit）、HuggingFace Transformers 等。

### 3.1.3术语翻译参考

1. [jiqizhixin/Artificial-Intelligence-Terminology-Database: A comprehensive mapping database of English to Chinese technical vocabulary in the artificial intelligence domain (github.com)](https://github.com/jiqizhixin/Artificial-Intelligence-Terminology-Database)
2. [数据科学术语表 | NVIDIA](https://www.nvidia.cn/glossary/data-science/)

TODO：整理已有的术语参考到文件glossary.md中

## 3.2语言理解规范

1. 易于理解的翻译：针对初学者，译者需要使用简单易懂的语言，避免过于复杂的表述。同时，需要在适当的地方添加解释性说明，以帮助初学者更好地理解概念和技术。
2. 文化敏感性：译者需要了解目标语言和文化的特点，在翻译过程中避免使用可能引起误解或不适的表述。同时，要注意对比原文和译文中的文化差异，尽可能保持原文的意义和风格。
3. 举例与案例的本地化：为了更好地体现语境，可以考虑将原文中的例子和案例替换为目标语言和文化背景下的具体实例。这有助于初学者更容易地理解概念，并提高学习兴趣。
4. 专业术语的处理：对于初学者而言，过多的专业术语可能会增加理解难度。在翻译过程中，译者需要充分考虑目标受众的背景，对于一些常用术语，可以保留英文原文，并在第一次出现时提供中文解释。对于不太常见的术语，可以直接翻译成中文，并在适当的地方添加解释。
5. 注重语言的逻辑性和连贯性：在翻译过程中，要注意保持译文的逻辑性和连贯性，以便初学者更容易地理解和掌握知识点。译者需要关注句子和段落之间的衔接，确保译文的通顺性。

## 3.3排版规范

可以参考[yaoqih/hint: 重构到 ---&gt; https://github.com/hustcc/lint-md](https://github.com/yaoqih/hint)

TODO：尝试搭建Github的Bot自动化处理

# 4. 可能存在的问题

1. 推荐使用的软件：
   提交：GitHub Desktop
   编辑软件：VsCode+Extension：Office Viewer(Markdown Editor)或Typora
2. utils代码说明
   - format_check：format_tool.py的代码实现
   - auto_fill_project：自动填写GitHub的Project
   - format_tools：翻译后的部分格式检查和自动修改（翻译用）
   - glossary_hint： 翻译前的专有名称提示（翻译用）
   - mask_translate：将mdx转换为基础的markdown以便部分编辑器打开
   - summery：用于统计工作量
3. 协同工作与沟通：在合作翻译过程中，译者之间需要有效地沟通和协作。解决这个问题需要建立有效的沟通机制，如定期召开会议、使用协作工具等。
4. 时间管理与进度把控：合作翻译项目可能涉及多个参与者和阶段，需要有效地管理时间和进度。项目经理需要密切关注项目进度，并在必要时进行调整。
5. 质量控制与审稿：在翻译过程中，可能出现翻译质量不高、审稿不严等问题。为确保译文质量，需要建立严格的审稿机制，对译文进行多轮审查和修改。

# 5. 发布的处理

## 5.1格式处理

1. 处理链接：直接将链接放到标记之后，并添加脚注
2. 处理Tip: 自写HTML标签规则
3. CourseFloatingBanner标签：移除
4. YouTube标签：移除
5. 标题后的[[[*]]：移除
6. 章节测试的处理
7. Torch和TensorFlow的区别处理

## 5.2内容处理

1. 点击交互的内容
2. 图片的翻译

## 5.3 prompt

希望你能担任英语翻译、拼写校对和修辞改进的角色。我是一个自然语言相关技术的初学者，我会给你一个课程的英文版本，请将其翻译并用更为优美和精炼的中文回答我。请将我简单的词汇和句子替换成更为优美和高雅的表达方式，确保意思不变，但使其更具文学性而且容易理解。请仅回答更正和改进的部分，不要写解释。我需要翻译的内容如下:

希望你能担任英语翻译、拼写校对和修辞改进的角色。我是一个自然语言相关技术的初学者，我会给你一个课程的英文版本，请将其翻译并用更为优美和精炼的中文回答我。请用通俗易懂的语言风格来编写翻译，同时确保意思不变，内容准确。请仅回答更正和改进的部分，不要写解释。我需要翻译的内容如下:

# 翻译

## 1. 初审

初审的目标是提供一个互联网发布版，会在原本的HF Course 发布。

流程

1. 打开zh_CN的文件对照修改
2. 打开typora检查格式和内容
3. 使用formt_tool格式化（格式化之前要提交commit）
4. typora最终检查

### 负责的内容

* 文字：确保描述准确，通顺，术语统一
* 格式：确保符合markdown语法，通过format_tool的格式检查，最后在markdown编辑器中查看和核对。

#### 文字细则：

1. 如果里面出现新的术语，比如token，前三个用中英双语表示将最终采用的放在括号外，另一个放在括号里。比如：词元（token）
2. 文字的您统一用你

#### 格式细则：

1. 要符合markdown语法，不要有过多的空行，链接使用规范，关键的名词使用 "``"
2. 在typora中查看没有异常的情况，对异常的情况进行修改

## 2. 二审

二审的目标是提供一个可以出版的版本

代码：划分TensorFlow和 Pytorch，处理python out

斜体：取消正文斜体改为双引号

图片：更改链接（更改space），下载，翻译，题注

章节层级：根据readme更改

双版本代码的不同：处理相同的描述只是专有名词不同

QA：尝试自动化处理

章节的描述：更改章节链接

代词：更换为具体的名词

指代性描述：标注具体位置

标点：半角全角符号规范统一

chapter7，QA：logist统一

token :统一

图片：转png插入文稿

属于规范：笔记本：Notebook token


流程：

1. 使用public_export_format将文本导出到publish

2. 检查排版和文字

3. 切换描述主体，并处理 HF 的TensorFlow 和Torhch 的 if /else

4. 处理QA（处理之前要提交commit）

5. 下载图片（下载之前要提交commit），翻译图片以及解释

6. 重构章节

7. 导出word并处理其他的信息

   | title                   | words  | 交稿日期 |
   | ----------------------- | ------ | -------- |
   | 0. 安装                 | 3113   |          |
   | 1. Transformer 模型     | 34920  | 7月28日  |
   | 2. 使用 🤗 Transformers  | 45954  |          |
   | 3. 微调一个预训练模型   | 36018  | 7月30日  |
   | 4. 分享你的模型和标记器 | 29496  |          |
   | 5. 🤗 Datasets库         | 80512  | 8月1日   |
   | 6. 🤗 Tokenizers库       | 101183 |          |
   | 7. 主要的 NLP 任务      | 211903 | 8月7日   |
   | 8. 如何寻求帮助         | 52097  |          |
   | 9. 构建并分享你的模型   | 44034  | 8月9日   |
   | 总计                    | 644694 |          |

   

### 负责的内容

* 文字：确保描述准确，通顺，术语统一，描述视角转化为书籍
* 格式：确保符合markdown语法，通过public_export_format的格式检查，最后在markdown编辑器中查看和核对。
* 图片：将图片替换为本地的中文图片

#### 文字细则：

1. 将描述的主体由课程切换到书籍
2. 再次审核一下描述，通读一遍
3. 处理HF的 TensorFlow和Torch 的if 和else

#### 格式细则：

1. 要符合markdown语法，不要有过多的空行，链接使用规范，关键的名词使用 "``"
2. 在typora中查看没有异常的情况，对异常的情况进行修改
3. 使用qa_translate.py将问答转化为书籍的格式

#### 图片细则：

1. 使用download_img,将所有的图片离线下来。
2. 使用Windows画图编辑png，使用word或者illstrator或者Inkscape修改svg
3. 将markdown中的图片描述翻译为中文

## 章节信息

第一部分：基础篇

1. 环境配置与介绍（c0s1）
2. Transformer模型（c1s1）

   - 自然语言处理概述(c1s2)
   - Transformer可以做什么（c1s3）
   - Transformer的工作原理(c1s4)
   - 常见的三种Transform模型的结构(c1s5,c1s6,c1s7)
   - 模型的偏见和局限性(c1s8)
   - 章末总结及测试（c1s9,c1s10）
3. 使用🤗Transformers（c2s1）

   - Pipeline 的内部（c2s2）
   - 模型与词元分析器的使用(c2s3,c2s4)
   - 多序列处理(c2s5,c2s6)
   - 章末总结及测试（c2s7,c2s8）
4. 微调预训练模型(c3s1)

   - 数据处理(c3s2)
   - 使用Trainer
     API进行模型训练（c3s3）
   - 使用Keras进行模型训练(c3s3_tf)
   - 一个完整的训练(c3s4)
   - 章末总结及测试（c3s5,c3s6）
5. 使用 Hugging Face Hub(c4s1)

   - 预训练模型的共享与使用(c4s2,c4s3)
   - 构建模型卡片(c4s4)
   - 章末总结及测试（c4s5,c4s6）

第二部分：进阶篇

6. 🤗 Datasets库(c5s1)

   - 数据集的获取与处理(c5s2,c5s3)
   - 大数据处理(c5s4)
   - 创建自定义数据集(c5s5)
   - 语义搜索与FAISS(c5s6)
   - 章末总结及测试（c5s7,c5s8）
7. 🤗 Tokenizers库(c6s1)

   - 新旧分词器的训练(c6s2)
   - 快速分词器的特性(c6s3,c6s3b)
   - 标准化与预分词(c6s4)
   - 各种分词算法的应用(c6s5,c6s6,c6s7)
   - 模块化构建词元分析器(c6s8)
   - 章末总结及测试（c6s9,c6s10）
8. 主要NLP任务(c7s1)

   - Token分类(c7s2)
   - 微调遮罩语言模型(s7s3)
   - 翻译(c7s4)
   - 摘要(c7s5)
   - 从头开始训练因果语言模型(c7s6)
   - 问答任务(c7s7)
   - 章末总结及测试（c7s8,c7s9）
9. 如何寻求帮助(c8s1)

   - 解决错误及提问的方法(c8s2,c8s3,c8s5)
   - 训练过程中的调试技巧(c8s4)
   - 章末总结及测试（c8s6,c8s7）

第三部分：拓展篇

10. 构建与分享演示(c9s1)

    - 使用Gradio构建演示(c9s2)
    - 掌握Interface类并与他人分享演示(c9s3,c9s4)
    - 与HuggingFace Hub的集成(c9s5)
    - 高级Interface功能及Blocks介绍(c9s6,c9s7)
    - 章末总结及测试（c9s8,c9s9）
