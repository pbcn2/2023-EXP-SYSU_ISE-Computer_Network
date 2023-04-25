# 网络抓包与协议分析

***

## **Commend**:

### 显示过滤器指令

显示arp协议报文（TCP/UDP/ICMP 同理）
```
arp    
```
显示源地址为a.b.c.d的icmp报文（ping的时候用的就是icmp报文）
```
ip.src == a.b.c.d && icmp
```

### 终端指令
```
arp -d  删除所有的ip地址项
    -s InetAddr EtherADDR [IfaceAddr]
    在ARP缓存中添加对应InetAddr地址的EtherAddr地址静态项
```

***

<br>

## 实验1.1 Wireshark软件使用与ARP协议分析

### 实验1.1.1 观察MAC地址
在显示捕捉器中中输入`ip.src == a.b.c.d && icmp`（将a.b.c.d）替换成目标服务器的IP地址，仅仅捕捉目标服务器的ping数据包

启动终端，输入`ping a.b.c.d`即可在Wireshark界面中看到icmp报文，双击打开，展开以太网Ⅱ

### 实验1.1.2 ARP协议分析
ARP是地址解析协议，主要作用是 **将IP地址解析成MAC地址** ，因为在数据链路层封装的时候必须有 IP地址和目标主机或下一跳服务器的MAC地址。

发送端主机自己惠维护一个ARP表，会首先查看自己的ARP表，如果表中有IP-MAC对，则不会发送ARP报文。因此，要观察到ARP报文首先应当打开终端输入
`arp -d`清空ARP表。

然后在显示过滤器中输入`arp`捕捉ARP报文

***请求报文***<br>
可以观察到一个Broadcast类型报文 INFO栏内容为  

    Who has a.b.c.d? Tell a'.b'.c'.d'
展开可以看到以太网Ⅱ端口的MAC地址栏为`ff:ff:ff:ff:ff:ff`表示不清楚目的端口，询问<br>

***回传报文***<br>
随后目标主机收到了广播，自己发送回传报文，Info为
``` 
a.b.c.d is at xxx:xxx(MAC)
```
展开以太网Ⅱ发现MAC位置已经用MAC地址替代了fff

<br><br>
## 实验1.2 IP与ICMP分析
