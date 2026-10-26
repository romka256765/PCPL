from operator import itemgetter

class PC:
     def __init__(self, id, net_name, price, OS_id):
          self.id = id
          self.net_name = net_name
          self.price = price
          self.OS_id = OS_id

class OS:
     def __init__(self, id, name):
          self.id = id
          self.name = name

class PCOS:
     def __init__(self, PC_id, OS_id):
          self.PC_id = PC_id
          self.OS_id = OS_id

Operating_Systems = [
     OS(1, 'Widowz OS'),
     OS(2, 'LuxMax OS'),
     OS(3, 'VkusnoITochka'),

     OS(11, 'Other Widowz OS'),
     OS(22, 'Other LuxMax OS'),
     OS(33, 'Other VkusnoITochka'),
]

Personal_Computers = [
     PC(1, 'Mercury', 57900, 1),
     PC(2, 'Venus', 108200, 2),
     PC(3, 'Earth', 149600, 3),
     PC(4, 'Mars', 227900, 3),
     PC(5, 'Jupiter', 778600, 3),
]

PC_OS = [
     PCOS (1, 1),
     PCOS (2, 2),
     PCOS (3, 3),
     PCOS (4, 3), 
     PCOS (5, 3),

     PCOS (1, 11),
     PCOS (2, 22),
     PCOS (3, 33),
     PCOS (4, 33), 
     PCOS (5, 33),
]

def main():
     one_to_many = [(pc.net_name, pc.price, os.name)
     for pc in Personal_Computers
     for os in Operating_Systems
     if pc.OS_id == os.id]

     many_to_many_temp = [(os.name, pcos.PC_id, pcos.OS_id)
     for os in Operating_Systems
     for pcos in PC_OS
     if os.id == pcos.OS_id]

     many_to_many = [(pc.net_name, pc.price, OS_name)
     for OS_name, PC_id, OS_id in many_to_many_temp
     for pc in Personal_Computers if pc.id == PC_id]

     print("Задание 1")
     res_1 = []
     for i in one_to_many:
          if 'OS' in i[2]:
               res_1.append(i)
     print(res_1)

     print('Задание 2')
     res_2_unsorted = []
     for os in Operating_Systems:
          pc_price = [price for net_name, price, os_name in one_to_many if os_name == os.name]
          if len(pc_price) > 0:
               avg_price = sum(pc_price)/len(pc_price)
               res_2_unsorted.append((os.name, round(avg_price, 2)))
     res_2 = sorted(res_2_unsorted, key = itemgetter(1))
     print(res_2)

     print('Задание 3')
     res_3 = []
     for i in many_to_many:
          for j in i[0]:
               if j[0] == 'M':
                    res_3.append((i[0], i[2]))
     print(res_3)

if __name__ == '__main__':
     main()