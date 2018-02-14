
# Archlinux安装配置

## 1. 安装基本系统

- 1 分区和挂载

	`mkfs.ext4 /dev/sda1`

	`mount /dev/sda1 /mnt`

	`mkdir -p /mnt/boot/efi`

	`mount /dev/sda2 /mnt/boot/efi`

- 2 安装系统

	配置软件源

	`grep -A 1 China mirrorlist > tmp`

	`mv mirrorlist mirrorlist.bak`

	`mv tmp mirrorlist`

	安装系统

	`pacstrap -i /mnt base base-devel`

	生成fstab

	`genfstab -U -p /mnt >> /mnt/etc/fstab`

	`cat /mnt/etc/fstab`

	进入新系统

	`arch-chroot /mnt`

- 3 新系统基本配置
	
	配置时区

	`ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime`

	`hwclock --systohc`

	配置编码

	`vim /etc/locale.gen`

	`locale-gen`

	配置主机名

	`echo Lenovo-Y430P > /etc/localhost`

	配置root密码

	`passwd root`

	安装GRUB(启动时需要使用UEFI方式启动安装U盘)

	`pacman -S grub efibootmgr`

	`grub-install --target=x86_64-efi --efi-directory=/boot/efi --recheck`

	`grub-mkconfig -o /boot/grub/grub.cfg`

- 4 返回重启
	
	`exit`

	`umount -R /mnt`

	`reboot`

## 2 安装无线网卡驱动

- 1 新建普通用户
	
	`useradd -m -G wheel -s /bin/bash zhang`

	`passwd zhang`

- 2 配置sudo

	`pacman -S sudo`

	`vim /etc/sudoers`

- 3 配置archlinuxcn源

	`[archlinuxcn]`

	`SigLevel = Never`
	
	`Server = http://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch`

- 4 安装yaourt
	
	`pacman -S yaourt`

- 5 安装无线网卡驱动 
	
	`sudo pacman -S dialog net-tools wpa_supplicant wireless_tools`

	`yaourt -S broadcom-wl`

	`sudo reboot`

## 3 安装桌面环境

- 1 安装显卡驱动

	`yaourt -S bumblebee xf86-video-intel nvidia`

	`sudo gpasswd -a zhang bumblebee`

	`sudo systemctl enable bumblebeed.service`

- 2 安装xorg

	`sudo pacman -S xorg-server`

- 3 安装gnome

	`sudo pacman -S gnome gdm gnome-tweak-tools`

	`sudo systemctl enable gdm NetworkManager`

- 4 配置中文输入	
	
	`sudo pacman -S wqy-zenhei wqy-microhei`

	`sudo pacman -S fcitx-im fcitx-configtool`

	`yaourt -S fcitx-sogoupinyin`

	修改～/.xprofile 文件

	`## ~/.xprofile`

	`export GTK_IM_MODULE=fcitx`
	
	`export QT_IM_MODULE=fcitx`
	
	`export XMODIFIERS='@im=fcitx'`

	解决快捷键切换问题

	`gsettings set org.gnome.settings-daemon.plugins.xsettings overrides "{'GtkIMModule':<'fcitx'>}"`

## 4 美化Gnome桌面

- 1 安装桌面配置软件

	`sudo pacman -S gnome-tweak-tool`

- 2 配置下拉式终端

	`sudo pacman -S gnome-shell-extension-drop-down-terminal`

- 3 更换图标

	`yaourt -S numix-circle-icon-theme-git`

- 4 更换主题

	`yaourt -S gtk-theme-arc-git`

- 5 配置dock 

	`yaourt -S gnome-shell-extension-dash-to-dock`

## 5 其他常用软件

- 1 网易云音乐

    `sudo pacman -S netease-cloud-music`

- 2 Zsh

    `sudo pacman -S zsh`

    `sudo pacman -S git`
    
    `wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh`
    
    `chmod +x install.sh`

    `./install.sh`

- 3 Sublime Text 3

	`sudo pacman -S sublime-text`

	授权码

	```
	—– BEGIN LICENSE —–
	MinBan
	Single User License
	EA7E-806395
	318133A3 8F202A61 B0DBB8EB 21E17D2E
	97D540E6 34079344 54620650 71E47589
	9EF87857 345F5042 0D728DD1 8D8C979D
	6A4F4DD2 67BB0345 746CA297 515BDA91
	6CEAB381 4DB56700 D77DCD14 977BD326
	1AC309ED 0EB414B8 4730DA10 99DBD291
	FC88E0EF DCC7E3A9 56E4FFED 7629746B
	E529AECA 92A96B60 72AE8928 8A240AAC
	—— END LICENSE ——
	```

## 6 安装Deepin桌面

- 1 安装Deepin

    `sudo pacman -S deepin` 

- 2 配置lightdm

    `sudo vim /etc/lightdm/lightdm.conf`

    ```
    [Seat:*] 
    greeter-session=lightdm-deepin-greeter
    ```
    
       


	


