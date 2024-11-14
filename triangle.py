def area(a, h): 
    '''
    Функция возвращает значение площади треугольника 

            Входные данные:

                    a: основание треугольника
                    b: высота треугольника

            Возвращаемое значение:

                    a*h/2: значение площади треугольника с ооснованием a и высотой h
    Пример:

            input: 3, 6        output: 9
    '''
    return a * h / 2 

def perimetr(a, b, c): 
    '''
    Функция возвращает значение периметра  треугольника 

            Входные данные:

                    a: сторона треугольника
                    b: сторона треугольника
                    с: сторона треугольника

            Возвращаемое значение:

                    a+b+c: значение периметра треугольника со сторонами a, b и c
    Пример:

            input: 2, 7, 3        output: 12
    '''
    return a + b + c 
