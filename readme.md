# Course review计划

此翻译项目旨在完成 HuggingFace Course的review，提供出版级别质量的译文。

# 1.项目分析

## 1.1 工程量分析

| title                   | words  | rate     |
| ----------------------- | ------ | -------- |
| 0. 安装                 | 3113   | 1        |
| 1. Transformer 模型     | 34920  | 11.21748 |
| 2. 使用 🤗 Transformers | 45954  | 14.76197 |
| 3. 微调一个预训练模型   | 36018  | 11.57019 |
| 4. 分享你的模型和标记器 | 29496  | 9.475104 |
| 5. 🤗 Datasets库        | 80512  | 25.86315 |
| 6. 🤗 Tokenizers库      | 101183 | 32.50337 |
| 7. 主要的 NLP 任务      | 211903 | 68.07035 |
| 8. 如何寻求帮助         | 52097  | 16.7353  |
| 9. 构建并分享你的模型   | 44034  | 14.1452  |
| 课程活动                | 5464   | 1.75522  |
| 总计                    | 644694 | 207.0973 |

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
