# django_login
这是一个django1.11版本的登录系统，主要用于自己学习用的，学习到了二个地方 ：
1》check_password来比较用户输入的密码与数据库中的密码的不是一样
2》在查询数据库数据时，如果用filter，则返回为querySet，取它的值，需要用xx[0].username，如果想用xx.username,需要改为get() 方法
3》退出登录，主要是退过在html中调用url地址，来到url.py路由表中找到对应处理方法，同时logout方法，需要注意与django自带的auth.logout名字最好不要一样，否则会出现递归调用错误
4>这里用到了captcha，它是用来做验证码的，对于验证码大小，内容,这些需要在setting.py中设置，主要参考：http://django-simple-captcha.readthedocs.io/en/latest/usage.html
5》在html中如果要使用uf.as_p，它的作用是将继承自forms.form表格转换为<p>的格式，每一个字段一个<p>,它主要是通过url.py中路由调用view.py(也可以不写到view.py)中的调用，在其中函数中调用对应的form(如loginuserform ,它继承于forms.form, uf=loginuserform(),return render(request, "*.html", {'uf':uf},)
6><form method="POST" enctype="multipart/form-data">: 表单特定的格式，注意上传数据的时候把enctype明确就可以
7>{% csrf_token %}: 跨域请求，我们需要在表单标签的内部加上这个模板标签，而且要在views.py中配合render而不是render_to_response来实现


