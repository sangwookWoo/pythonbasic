class Team:
    count = 0
    order = []
    def __init__(self, number, name = None,  member = set()):
        self.number = number
        self.name = name
        self.__member = member
        Team.count += 1
        Team.order.append(number)
        
    def add_member(self, name):
        if name not in self.__member:
            self.__member.add(name)
            print(f'{name}님을 팀 {self.number}에 추가했습니다.')
        else:
            print(f'{name}님은 이미 팀에 있습니다.')
            
    def rm_member(self, name):
        if name in self.__member:
            self.__member.remove(name)
            print(f'{name}님을 팀에서 삭제했습니다.')
        else :
            print(f'{name}님은 해당 팀에 없습니다.')
            
    def get_count(self):
        return Team.count

    def get_order(self):
        return Team.order
    
    def set_order(self, x):
        if x in Team.order:
            Team.order.remove(x)
            Team.order.append(x)
        else :
            Team.order.append(x)
    
    def __len__(self):
        return len(self.__member) 