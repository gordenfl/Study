#!/bin/bash
# 游戏服务器 TCP 优化脚本（适用于 TCP 长连接场景）
# 请使用 root 权限执行

echo "✅ 开始优化 Linux 系统以支持高并发 TCP 长连接"

echo "👉 设置文件描述符上限..."
ulimit -n 1048576
echo "* soft nofile 1048576
* hard nofile 1048576" >> /etc/security/limits.conf

# 适用于 Ubuntu/Debian 的 PAM 设置
if grep -q "pam_limits.so" /etc/pam.d/common-session; then
    echo "pam_limits.so 已配置"
else
    echo "session required pam_limits.so" >> /etc/pam.d/common-session
fi

# 适用于 CentOS/RHEL
if [ -f /etc/pam.d/login ]; then
    echo "session required pam_limits.so" >> /etc/pam.d/login
fi

echo "👉 修改 sysctl.conf 内核参数..."
cat <<EOF >> /etc/sysctl.conf

# === TCP 长连接优化 for Game Server ===
fs.file-max = 2097152

# 本地端口范围扩大（支持更多客户端连接）
net.ipv4.ip_local_port_range = 1024 65535

# 提高 TCP 队列长度
net.core.somaxconn = 65535
net.core.netdev_max_backlog = 250000
net.ipv4.tcp_max_syn_backlog = 65535

# TIME_WAIT 优化（适用于长连接场景）
net.ipv4.tcp_fin_timeout = 15
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_tw_recycle = 0

# 防止 TIME_WAIT 占满连接池
net.ipv4.tcp_max_tw_buckets = 500000

# 禁用连接 Keepalive（由应用层控制更灵活）
net.ipv4.tcp_keepalive_time = 600

# 启用 TCP 快速打开（视客户端支持而定）
net.ipv4.tcp_fastopen = 3

# 禁用 SYN Cookies（除非你有 SYN flood 风险）
net.ipv4.tcp_syncookies = 0
EOF

echo "✅ 应用 sysctl 参数..."
sysctl -p

echo "🧹 清理旧连接状态建议："
echo "可以使用 netstat -ant 或 ss -ant 状态分析连接状态"

echo "✅ 优化完成，请重启系统以确保全部设置生效。"
