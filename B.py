class math_people():
    def __init__(self,sname,name,my_class,alg,geo):
        self.my_name = name
        self.my_sname = sname
        self.my_class = my_class
        self.my_alg = alg
        self.my_geo = geo
        self.my_total = alg+geo

class math_class():
    def __init__(self,my_lines):
        self.line = my_lines
    def search_winner(self):
        nowmax = 0
        for i in range(len(self.line)):
            if self.line[i].my_total > nowmax:
                nowmax = self.line[i].my_total
        print("Победители в ",self.line[1].my_class," :")
        for i in range(len(self.line)):
            if self.line[i].my_total == nowmax:
                print(self.line[i].my_name," ",self.line[i].my_sname," ",self.line[i].my_total)
    def search_best_in(self,par):
        nowmax = 0
        if par == 1:
            for i in range(len(self.line)):
                if self.line[i].my_alg > nowmax:
                    nowmax = self.line[i].my_alg
            print("Победители в алгебре:")
            for i in range(len(self.line)):
                if self.line[i].my_alg == nowmax:
                    print(self.line[i].my_name," ",self.line[i].my_sname," ",self.line[i].my_class)
        elif par == 2:
            for i in range(len(self.line)):
                if self.line[i].my_geo > nowmax:
                    nowmax = self.line[i].my_geo
            print("Победители в геоме:")
            for i in range(len(self.line)):
                if self.line[i].my_geo == nowmax:
                    print(self.line[i].my_name," ",self.line[i].my_sname," ",self.line[i].my_class)



bufpar8 = list()
bufpar9 = list()
bufpar10 = list()
bufpar11 = list()

f = open('mat_dv.txt')
for line in f:
    buf = line.split()
    now_people = math_people(buf[0],buf[1],int(buf[2]),int(buf[3]),int(buf[4]))
    if now_people.my_class == 8:
       bufpar8.append(now_people)
    elif now_people.my_class == 9:
        bufpar9.append(now_people)
    elif now_people.my_class == 10:
        bufpar10.append(now_people)
    elif now_people.my_class == 11:
        bufpar11.append(now_people)

par8 = math_class(bufpar8)
par9 = math_class(bufpar9)
par10 = math_class(bufpar10)
par11 = math_class(bufpar11)
parall = math_class(bufpar8+bufpar9+bufpar10+bufpar11)

par8.search_winner()
par9.search_winner()
par10.search_winner()
par11.search_winner()

parall.search_best_in(1)
parall.search_best_in(2)

