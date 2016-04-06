class Friends:
        
    def __init__(self, connections):
        self.connections = []
        for pair in connections:
           self.connections.append(pair)

            
        
    def add(self, connection):
        
        if connection in self.connections:
            return (False)
        else:
            self.connections.append(connection)
            return (True)
           
    def remove(self, connection):
        if connection in self.connections:
            self.connections.remove(connection);
            return (True)
            
        else:
            return (False)
            
            
    def names(self):
        friends=[]
        friends=set(friends)
        for i in self.connections:
            i=list(i)
            if not i[0] in friends:
                friends.add(i[0])
            if not i[1] in friends:
                friends.add(i[1])    
        return (friends)
        
        
    def connected(self, name):
        friends=set([])
        for i in self.connections:
            i=list(i)
            if name == i[0]:
                friends.add(i[1])
            if name == i[1]:
                friends.add(i[0])
        return (friends)
        
        
        #commit

\
