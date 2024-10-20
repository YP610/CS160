class ListManipulator:
    def __init__(self,a_list) -> None:        
        self.a_list=a_list
        
        
    def swap_first_last(self)  -> None:
        temp= self.a_list[0]
        self.a_list[0]=self.a_list[len(self.a_list)-1]
        self.a_list[len(self.a_list)]=temp
        
    def sum_list(self) -> int:
        sum=0
        for i in self.a_list:
            sum+=i
        return sum
    
    def append_value(self, value:int ) -> None:
        self.a_list.append(value)
        
    def get_list(self) -> list:
        return self.a_list
    
    