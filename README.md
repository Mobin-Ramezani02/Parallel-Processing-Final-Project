# Parallel-Processing-Final-Project


# اتصال پروژه به GitHub

این راهنما مراحل اتصال یک پروژه محلی به ریپازیتوری GitHub را نشان می‌دهد.  
فرض بر این است که Git روی سیستم نصب شده باشد.

---

## ۱. ساخت ریپازیتوری در GitHub

1. وارد حساب GitHub شوید.
2. روی دکمه **New Repository** کلیک کنید.
3. یک نام انتخاب کنید و ریپازیتوری را **Public** یا **Private** بسازید.
4. آدرس (URL) ریپازیتوری را کپی کنید (HTTPS یا SSH).

---

## ۲. آماده‌سازی پروژه روی سیستم

داخل پوشه پروژه در ترمینال:

```bash
git init
git add .
git commit -m "Initial commit"
