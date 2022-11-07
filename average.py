from reduce_list import reduce_list
list = ['1', '2', '2', '3', '5']
res = [*set(list)]
my_list = reduce_list


def reduce_list():
  return list - max(list)


def average():
  return sum(my_list, res) / len(my_list, res)
