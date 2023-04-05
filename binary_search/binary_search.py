
class BinarySearch():

    def search_iterative(self , list , item):
        low = 0 
        high = len(list) - 1 

        while low <= high: 
            mid = (low + high) // 2  
            guess = list[mid]

            if guess == item: 
                return mid
            elif guess > item : 
                high = mid - 1
            else:
                low = mid +1 
                        
        return None 
    
    def search_recursive (self, list, low, high, item):
        # Check base case 
        if high >= low :
            mid =(high + low) // 2
            guess = list[mid]

            if guess == item : 
                return list[mid]
            elif guess > item :
                return self.search_recursive(list, low, mid -1 , item)
            else:
                return None


  
bs = BinarySearch()
my_list = [1, 3, 5, 7, 9]

print(bs.search_iterative(my_list, 3)) # => 1

# 'None' means nil in Python. We use to indicate that the item wasn't found.
print(bs.search_iterative(my_list, -1)) # => None