import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        # Создаём объект Runner
        runner = Runner("TestRunner")
        # Вызываем метод walk 10 раз
        for _ in range(10):
            runner.walk()
        # Проверяем, что дистанция равна 50
        self.assertEqual(runner.distance, 50, "Distance after walking 10 times should be 50")

    def test_run(self):
        # Создаём объект Runner
        runner = Runner("TestRunner")
        # Вызываем метод run 10 раз
        for _ in range(10):
            runner.run()
        # Проверяем, что дистанция равна 100
        self.assertEqual(runner.distance, 100, "Distance after running 10 times should be 100")

    def test_challenge(self):
        # Создаём два объекта Runner
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")
        # У runner1 вызываем run, у runner2 вызываем walk 10 раз
        for _ in range(10):
            runner1.run()
            runner2.walk()
        # Проверяем, что их дистанции не равны
        self.assertNotEqual(
            runner1.distance,
            runner2.distance,
            "Distances of runners should not be equal after different activities"
        )


# Запуск тестов
if __name__ == "__main__":
    unittest.main()

