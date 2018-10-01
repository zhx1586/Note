# Git 相关配置

## 1初始化用户名和邮箱

```shell
git config --global user.name "zhx1586"
git config --global user.email "zhx1586@126.com"
```

## 2 配置远程仓库

- 创建 SSH 秘钥

  ```shell
  ssh-keygen -t rsa -C "zhx1586@126.com"
  ```

- 将公钥 `id_rsa.pub` 加入GitHub 网站

- 将本地仓库与远程仓库相关联

  ```shell
  git remote add origin git@github.com:zhx1586/learngit.git
  ```

- 首次提交

  ```shell
  git push -u origin master
  ```

- 日常提交

  ```shell
  git push origin master
  ```

- 从远程仓库克隆

  ```shell
  git clone git@github.com:zhx1586/learngit.git
  ```


