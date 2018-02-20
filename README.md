Задача:
Программа должна эмулировать гонку трёх автомобилей. В каждый момент времени машина либо двигается вперёд, либо нет. Каждый раз программа выводит пройденный автомобилями путь. Через пять промежутков времени гонка заканчивается.

Примеры вывода:
```
 -
 - -
 - -

 - -
 - -
 - - -

 - - -
 - -
 - - -

 - - - -
 - - -
 - - - -

 - - - -
 - - - -
 - - - - -
```


# Дополнительные задачи

Дан код в императивном стиле, переписать его в функциональный.

reduce:
```python
sentences = ['капитан джек воробей',
             'капитан дальнего плавания',
             'ваша лодка готова, капитан']

cap_count = 0
for sentence in sentences:
    cap_count += sentence.count('капитан')

print cap_count
```

map:
```python
names = ['Маша', 'Петя', 'Вася']

for i in range(len(names)):
    names[i] = hash(names[i])

print names
```


Решение должно быть в функциональном стиле.

- Чистые функции
- Неизменяемые значения
