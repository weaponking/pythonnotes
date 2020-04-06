agent功能:

    1.采集机器指标 cpu mem net 设置采集间隔及指标 
    
    2.采集本地mysql指标 慢日志 错误日志 锁等待 等 
    
    3.上报kafka
    
```mermaid
graph LR;
　　Portal-->|发布/更新配置|Apollo配置中心;
　　Apollo配置中心-->|实时推送|App;
　　App-->|实时查询|Apollo配置中心;
```
