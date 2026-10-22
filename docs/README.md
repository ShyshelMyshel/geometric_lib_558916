# Geometric Lib

## Общее описание
Библиотека на Python для вычисления площади и периметра геометрических фигур: круга, квадрата, прямоугольника и треугольника.

## Навигация

- [Общее описание](#общее-описание)
- [Функции](#функции)
  - [Круг](#circlearear)
    - [circle.area(r)](#circlearear)
    - [circle.perimeter(r)](#circleperimeterr)
  - [Квадрат](#squareareaa)
    - [square.area(a)](#squareareaa)
    - [square.perimeter(a)](#squareperimetera)
  - [Прямоугольник](#rectangleareaa-b)
    - [rectangle.area(a, b)](#rectangleareaa-b)
    - [rectangle.perimeter(a, b)](#rectangleperimetera-b)
  - [Треугольник](#triangleareaa-h)
    - [triangle.area(a, h)](#triangleareaa-h)
    - [triangle.perimeter(a, b, c)](#triangleperimetera-b-c)
- [История изменений](#история-изменений)



---

## Функции


### circle.area(r)
Принимает радиус `r`, возвращает площадь круга радиуса `r`.
Пример вызова: `area(1)`

### circle.perimeter(r)
Принимает радиус `r`, возвращает длину окружности.
Пример вызова: `perimeter(2)`

### square.area(a)
Принимает число `a` (сторону квадрата), возвращает его площадь.
Пример вызова: `area(3)`

### square.perimeter(a)
Принимает число `a` (сторону квадрата), возвращает его периметр.
Пример вызова: `perimeter(4)`

### rectangle.area(a, b)
Принимает две соседние стороны a и b, возвращает площадь прямоугольника.
Пример вызова: area(3, 5)

### rectangle.perimeter(a, b)
Принимает две соседние стороны a и b, возвращает периметр прямоугольника.
Пример вызова: perimeter(3, 5)

### triangle.area(a, h)
Принимает число `a` и `h` (сторону и высоту треугольника), возвращает его площадь.
Пример вызова: `area(5, 12)`

### triangle.perimeter(a, b, c)
Принимает три стороны треугольника, возвращает его периметр.
Пример вызова: `perimeter(5, 12, 13)`

## История изменений
- `0504138` Добавила в функциях блоки комментариев с описаниями самих функций и примерами их  вызова
- `d078c8d` L-03: Docs added
- `8ba9aeb` L-03: Circle and square added