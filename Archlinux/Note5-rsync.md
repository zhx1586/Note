# 使用rsync来备份Archlinux

## 1 备份

    sudo mkdir /backup
    sudo vim /backup/exclude.list

将内容修改为：

    /proc/*
    /dev/*
    /sys/*
    /tmp/*
    /mnt/*
    /media/*
    /run/*
    /var/lock/*
    /var/run/*
    /var/cache/pacman/pkg/*
    /lost+found
    /backup/*
    /swapfile

使用rsync进行备份
    
    sudo rsync -avXAP --delete --exclude-from=/backup/exclude.list / /backup/backup_root

## 2 还原    

    sudo rsync -avXAP /backup / 

如果分区有变化，需要重新生成fstab

    sudo rm /mnt/etc/fstab
    sudo genfstab -U -p /mnt >> /mnt/etc/fstab


