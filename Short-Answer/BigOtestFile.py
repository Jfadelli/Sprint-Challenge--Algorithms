## test b)
import time
    
def test_b():
    n = input('n input : ')
    if n == 'test':
        test_values = [
        1, 10, 100, 1000, 10000, 100000, 1000000
    ]
        for i in range(len(test_values)):
            n = test_values[i]
    else:
        n = int(n)

    def power_two(my_range):
        return [x**2 for x in range(my_range)]
        
    def algo_test_func():
        sum = 0
        for i in range(n):
            j = 1
            while j < n:
                j *= 2
                sum += 1
        print('sum: ', sum)

    def measure_time(func):
        start = time.time()
        algo_test_func()
        end = time.time()
        print(end - start)  
        
    measure_time(lambda: power_two(10000000))

def test_c():
    print('Welcome to test C')

    n = input('n input : ')
    if n == 'test':
        test_values = [
        1, 10, 100, 1000, 10000, 100000, 1000000
    ]
        for i in range(len(test_values)):
            n = test_values[i]
    else:
        n = int(n)

    def power_two(my_range):
        return [x**2 for x in range(my_range)]

    def bunnyEars(n):
      if n == 0:
        return 0

      return 2 + bunnyEars(n-1)

    def measure_time(func):
        start = time.time()
        bunnyEars()
        end = time.time()
        print(end - start)  
        
        measure_time(lambda: power_two(10000000))

def run_tests():
    user = input('what test do you want to run? : test_a, test_b, test_c ')
    if user != 'q':
        if user == 'test_b':
            test_b()
        elif input() == 'test_a':
            print('test_a has not been installed')
            run_tests()
        elif user == 'test_c':
            test_c()
        else:
            return
    else:
        exit()
   

run_tests()
