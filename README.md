# EMTest

## 简介

EMTest（Easy Multi-process Testing Tool）是一款简单的多进程测试管理工具，基于 [VSCode Testing API](https://code.visualstudio.com/api/extension-guides/testing)。

- 最新版本: [Download](https://gitlab.enjoymove.cn/longwei.zhang/emtest/-/releases)
- 项目地址: [GitLab](https://gitlab.enjoymove.cn/longwei.zhang/emtest)
- 问题意见: [Issue](https://gitlab.enjoymove.cn/longwei.zhang/emtest/-/issues)

## 特性

- [x] 无需配置，自动检测工作区内的所有 Gtest 测试程序。
- [x] 能够选取其中的一个或多个测试用例执行。
- [x] 提供更细粒度的高级配置，需要编写配置文件。
- [x] 能够添加不同目录下的多个测试程序，对于每个测试程序指定运行参数。
- [x] 具有程序输出控制台，能够显示日志打印和测试结果。
- [x] 测试用例分组执行，组内并行，组间串行

## 快速开始

目前该扩展并没有上线到 VSCode 扩展商店，所以只能使用打包好的程序，进行离线安装。

安装完毕后，使用 VSCode 打开包含 Gtest 测试程序的文件夹，EMTest 会自动检测该文件夹及其子文件夹下的所有测试程序。

![](https://gitlab.enjoymove.cn/longwei.zhang/emtest/-/raw/master/resources/emtest001.png)



## Documentation

更多使用细节，可以查阅[项目文档](https://gitlab.enjoymove.cn/longwei.zhang/emtest/-/blob/master/docs/index.md)



## Changelog

每个发布版本的细节可以查看更新日志[CHANGELOG](https://gitlab.enjoymove.cn/longwei.zhang/emtest/-/blob/master/CHANGELOG.md)



## Contribution

如果你想为本项目做贡献，请先阅读[Contributing Guide](https://gitlab.enjoymove.cn/longwei.zhang/emtest/-/blob/master/CONTRIBUTING.md)



## License

[MIT](https://gitlab.enjoymove.cn/longwei.zhang/emtest/-/blob/master/LICENSE)
