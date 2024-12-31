def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()
# inner_function()
'''
inner_function() -  вызывая функцию inner_function в глобальном пространстве имен, которая является локальной функцией объемлющей
функции test_function(), мы получаем ошибку "name 'inner_function' is not defined. Did you mean: 'test_function'?", так как 
локальные переменные, определённые внутри функции, становятся недоступными после выхода из неё

но вызывая функцию inner_function() в объемлющей функции, данные из функции не показываются, так как локальная пременная (данные print)
находится только в в локальной области видимости функции inner_function
'''
# test_function ()