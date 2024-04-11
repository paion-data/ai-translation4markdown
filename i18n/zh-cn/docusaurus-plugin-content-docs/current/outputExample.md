---
sidebar_position: 4
标题: 配置

---

[//]: # (版权所有 Paion Data)

[//]: # (根据 Apache License, Version 2.0 的规定获得许可；)
[//]: # (除非符合相关法律法规或书面协议，否则您不得使用此文件。)
[//]: # (您可以通过以下方式获取许可证的副本：)

[//]: # (    http://www.apache.org/licenses/LICENSE-2.0)

[//]: # (未经适用法律要求或书面同意，根据本许可分发的软件)
[//]: # (按“原样”基础提供，不附带任何形式的明示或暗示担保。)
[//]: # (请参阅许可证以了解特定于语言的权限和)
[//]: # (限制。)

页面中的配置可以按照以下顺序从多个来源设置：

1. 操作系统的环境变量；例如，可以使用 `export DB_URL="jdbc:mysql://db/elide?serverTimezone=UTC"` 设置环境变量
2. Java 系统属性；例如，可以使用 `System.setProperty("DB_URL", "jdbc:mysql://db/elide?serverTimezone=UTC")` 设置 Java 系统属性
3. 放置于 CLASSPATH 下的 **.properties** 文件。此文件可置于 `src/main/resources` 源目录中，内容如下：`DB_URL=jdbc:mysql://db/elide?serverTimezone=UTC`

核心属性
--------

:::note

以下配置可放置在名为 **application.properties** 的属性文件中

:::

- **MODEL_PACKAGE_NAME**: 包含一组 Elide JPA 模型的完全限定包名

(Elide) JPA 数据存储
--------------------

:::note

以下配置可放置在名为 **jpadatastore.properties** 的属性文件中

:::

- **DB_USER**: 持久化数据库用户名（需要具有读写权限）。
- **DB_PASSWORD**: 持久化数据库用户密码。
- **DB_URL**: 持久化数据库 URL，如 "jdbc:mysql://localhost/elide?serverTimezone=UTC"。
- **DB_DRIVER**: SQL 数据库驱动类名，如 "com.mysql.jdbc.Driver"。
- **DB_DIALECT**: SQL 数据库方言名，如 "org.hibernate.dialect.MySQLDialect"。
- **HIBERNATE_HBM2DDL_AUTO**: 当 Web 服务启动时，对现有 JPA 数据库执行的操作；可取以下 4 个值之一：

  1. _validate_：验证模式匹配，不对数据库模式做任何更改。_这是 **HIBERNATE_HBM2DDL_AUTO** 的默认值_
  2. _update_：更新模式以反映要持久化的实体
  3. _create_：为您的实体创建所需的模式，销毁任何先前数据。
  4. _create-drop_：如上所述创建模式，但在会话结束时也删除该模式。这对于开发或测试非常有用。

  :::note

  此属性与 [Hibernate `hibernate.hbm2ddl.auto` 属性] 完全相同。

  :::

[Hibernate `hibernate.hbm2ddl.auto` 属性]: https://stackoverflow.com/questions/18077327/hibernate-hbm2ddl-auto-possible-values-and-what-they-do

[Java 系统属性]: https://docs.oracle.com/javase/tutorial/essential/environment/sysprop.html

[操作系统的环境变量]: https://docs.oracle.com/javase/tutorial/essential/environment/env.html