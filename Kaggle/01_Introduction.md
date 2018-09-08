# 01 Kaggle 基础概述

##  1 任务种类

- 分类
- 回归
- 推荐
- 排序

## 2 大致流程

### 2.1 Data Exploration 

- 目的： 对数据进行探索性分析。
- 常用库：`pandas`，`matplotlib`，`seaborn`。

### 2.2 Data Preprocessing

- 目的：对数据进行预处理。

### 2.3 Feature Enginnering

- 目的：构造有用的特征（重要步骤，效果取决于对数据的了解程度）。

### 2.4 Model Selection

- 目的：选择适合数据的模型。
- 基于树的模型：
  - Gradient Boosting Decision Tree
  - Random Forest
  - Extra Randomized Trees
- 其他常用模型：
  - SVM
  - Linear Regression
  - Logistic Regression
  - Neural Network （CV）

### 2.5 Ensemble Generation

- 目的：将多个模型融合来获得更好的表现。

## 3 高效的Pipeline 

### 3.1 模块化的 Feature Transform

- 含义：使用很少的代码即可将新的 Feature 更新到训练集中。

### 3.2 自动化的 Grid Search

- 含义：只要预先设定好使用的模型和参数的候选就能自动搜索并记录最佳模型。

### 3.3 自动化的 Ensemble Generation

- 含义：每隔一段时间将现有最好的 $k$ 个模型拿来做模型融合。

## 4 学习计划

- 学习常用模型和 python 库。
- 参加入门级比赛，掌握大致流程。
- 参加正式比赛。

