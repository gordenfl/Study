# 02 General Estimate

## Map of Count to Size:

| Count      | Size   |
|------------|--------|
|1           | 1 KB   |
|1 Thousand  | 1 MB   |
|1 Million   | 1GB    |
|1 Billion   | 1TB    |


## Latency statistics:

| Operation name      | Time                                 |
|---------------------|--------------------------------------|
| L1 cache            | 0.5 ns                               |
| L2 cache            | 5 ns                                 |
| Mutex lock/unlock   | 7 ns                                 |
| Memory reference    | 10 ns                                |
| Zip 1K Byte         | 10,000 ns = 10μs                     |
| 2K network          | 20,000 ns = 20μs                     |
| Read 1M from Memory | 250,000 ns = 250μs                   |
| Read 1M from network| 10,000,000 ns = 10ms                 |
| Read 1M from disk   | 30,000,000 ns = 10ms                 |


## Assessment the Twitter Query Times and Storage requirement

Support:
    * 300 Million active user
    * 50% user use Twitter every day
    * 2 Twits every user on average
    * 10% Twits will include media
    * Data will storage 5 years

Assessment: 
* QPS
    300 Million * 50% = 150 Million active users
    Twits QPS = 150 M * 2 / 24/ 3600 = 3500 QPS
    Peek is QPS * 2 = 7000

* Storage
    * average data size
        average each twits ID are 128 bytes
        average each twits text are 250 bytes
        media 1Mb
    * Media Storage : 150M * 2 * 1M * 10% = 30 Tb
    * 5 years data : 30Tb * 365 * 5 = 55Pb