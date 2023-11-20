'''
Создайте программу на Python или Java, которая принимает два списка чисел и
выполняет следующие действия:
a. Рассчитывает среднее значение каждого списка.
b. Сравнивает эти средние значения и выводит соответствующее сообщение:
- ""Первый список имеет большее среднее значение"", если среднее значение первого списка больше.
- ""Второй список имеет большее среднее значение"", если среднее значение второго списка больше.
- ""Средние значения равны"", если средние значения списков равны.

Важно:
Приложение должно быть написано в соответствии с принципами
объектно-ориентированного программирования.
Используйте Pytest (для Python) или JUnit (для Java) для написания тестов,
которые проверяют правильность работы программы.
Тесты должны учитывать различные сценарии использования вашего приложения.
Используйте pylint (для Python) или Checkstyle (для Java) для проверки качества кода.
Сгенерируйте отчет о покрытии кода тестами. Ваша цель - достичь минимум 90% покрытия.
'''

from contextlib import redirect_stdout
import io
from final_task import ListsCompare

class TestListCompare:
    '''Test for ListCompare functions'''

    def __compare(self, l1, l2):
        lc = ListsCompare(l1, l2)

        with redirect_stdout(io.StringIO()) as f:
            lc.compare_lists_avg()
        return f.getvalue().strip()

    def test_compare_lists_avg_first_greater(self):
        '''Test for compare_lists_avg where first list greater than second'''
        s = self.__compare([0, 1, 2, 4, 8], [3, 1, 0])
        assert s == "Первый список имеет большее среднее значение"

    def test_compare_lists_avg_second_greater(self):
        '''Test for compare_lists_avg where second list greater than first'''
        s = self.__compare([0, 1, 2, 4, 8], [3, 5, 7])
        assert s == "Второй список имеет большее среднее значение"

    def test_compare_lists_avg_equal(self):
        '''Test for compare_lists_avg where both lists equal'''
        s = self.__compare([0, 1, 2, 4, 8], [3, 5, 6, 0, 1])
        assert s == "Средние значения равны"
