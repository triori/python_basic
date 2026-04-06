class Counter:

   def __init__(self, current=1, min_value=0, max_value=10):
       if min_value > max_value:
           raise ValueError('Минимум не может быть больше максимума')
       if not min_value <= current <= max_value:
           raise ValueError('Начальное значение должно быть в пределах диапазона')
       self.current = current
       self.min_value = min_value
       self.max_value = max_value

   def set_current(self, start):
       if not self.min_value <= start <= self.max_value:
           raise ValueError('Текущее значение должно быть в пределах диапазона')
       self.current = start

   def set_max(self, max_max):
       if max_max < self.min_value:
           raise ValueError('Максимум не может быть меньше минимума')
       if self.current > max_max:
           raise ValueError('Текущее значение больше нового максимума')
       self.max_value = max_max

   def set_min(self, min_min):
       if min_min > self.max_value:
           raise ValueError('Минимум не может быть больше максимума')
       if self.current < min_min:
           raise ValueError('Текущее значение меньше нового минимума')
       self.min_value = min_min

   def step_up(self):
       if self.current >= self.max_value:
           raise ValueError('Достигнут максимум')
       self.current += 1

   def step_down(self):
       if self.current <= self.min_value:
           raise ValueError('Достигнут минимум')
       self.current -= 1

   def get_current(self):
       return self.current

counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e) # Достигнут максимум
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e) # Достигнут минимум
assert counter.get_current() == 7, 'Test4'