# django_login
这是一个django1.11版本的登录系统，主要用于自己学习用的，学习到了二个地方 ：
1》check_password来比较用户输入的密码与数据库中的密码的不是一样
2》在查询数据库数据时，如果用filter，则返回为querySet，取它的值，需要用xx[0].username，如果想用xx.username,需要改为get() 方法
3》退出登录，主要是退过在html中调用url地址，来到url.py路由表中找到对应处理方法，同时logout方法，需要注意与django自带的auth.logout名字最好不要一样，否则会出现递归调用错误


