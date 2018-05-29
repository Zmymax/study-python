# Happyday

启动python有两种方式：python manage.py shell和python。

这两个命令 都会启动交互解释器，但是manage.py shell命令有一个重要的不同： 在启动解释器之前，它告诉Django使用 哪个设置文件。 Django框架的大部分子系统，包括模板系统，都依赖于配置文件；如果Django不知道使用哪 个配置文件，这些系统将不能工作。
