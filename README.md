# Parallel-Processing-Final-Project


# اتصال پروژه به GitHub

این راهنما مراحل اتصال یک پروژه محلی به ریپازیتوری GitHub را نشان می‌دهد.  
فرض بر این است که Git روی سیستم نصب شده باشد.

### 1. ساخت ریپازیتوری در GitHub

1. وارد حساب GitHub شوید.
2. روی دکمه **New Repository** کلیک کنید.
3. یک نام انتخاب کنید و ریپازیتوری را **Public** یا **Private** بسازید.
4. آدرس (URL) ریپازیتوری را کپی کنید (HTTPS یا SSH).


### 2. آماده‌سازی پروژه روی سیستم

داخل پوشه پروژه در ترمینال:

```bash
git init
git add .
git commit -m "Initial commit"

```



### 3. اتصال به ریپازیتوری GitHub
```bash
git remote add origin <URL>
```
مثال :
git remote add origin https://github.com/username/repo-name.git

### 4. ارسال کد به GitHub

```bash
git branch -M main
git push -u origin main
```

نمونه اجرای دستورات :
![Github connection](images/github1.png)
![Github connection](images/github2.png)
---


# داکرایز کردن پروژه








