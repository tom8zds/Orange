![unittest](https://github.com/tom8zds/Orange/actions/workflows/unittest.yml/badge.svg)

# Orange
一体化追番服务, 集成订阅下载链接刮削

支持linux, docker

# 自动化流程
1. 用户使用数据源获取番剧信息
2. 选择番剧进行订阅, 订阅时进行番剧刮削, 加入订阅库
3. 定时刷新订阅, 订阅结果进行刮削后加入下载队列
4. 定时监控下载队列中的任务
5. 任务完成时, 使用链接器进行硬链接,送入刮削器刮削信息,重命名并按照路径放置,将库中剧集加入白名单
