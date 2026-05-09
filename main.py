import functools

def my_decorator(func):
    def wrapper():
        print("Chetdan kelgan funksiya ishlayapti.")
        func()
    return wrapper

@functools.wraps(my_decorator)
def decorated_function():
    print("Bu funksiya dekori qilingan.")

print(decorated_function.__name__)
print(decorated_function.__doc__)
```

Kodni ishlatib ko'rish uchun quyidagilarni amalga oshiring:

1. `functools.wraps` funksiyasini import qiling.
2. Dekorator funksiyasini yozing (masalan, `my_decorator`).
3. Dekorator funksiyasiga `@functools.wraps(my_decorator)` ni qo'shing.
4. Dekorator funksiyasini ishlatib, unga `__name__` va `__doc__` atributlarini chiqaring.
