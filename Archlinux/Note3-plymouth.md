# 为Archlinux添加开机Logo

## 1 安装Plymouth

    yaourt -S gdm-plymouth

## 2 配置Plymouth HOOK

    sudo vim /etc/mkinitcpio.conf

修改内容为：

    HOOKS="base udev plymouth [...] "

## 3 修改内核参数

    sudo vim /etc/default/grub 

修改内容为：

    GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"

重新生成内核镜像：

    sudo mkinitcpio -p linux

重新生成GRUB配置文件：

    sudo grub-mkconfig -o /boot/grub/grub.cfg

## 4 将gdm替换为gdm-plymouth

    sudo systemctl disable gdm.service
    sudo systemctl enable gdm-plymouth.service

## 5 配置Plymouth

    plymouth-set-default-theme -R spinfinity

