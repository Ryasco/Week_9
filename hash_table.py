class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"

contact_1 = Contact("Alice", "123-456-7890")
print(contact_1)

class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
   
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

contact_1 = Contact("Alice", "123-456-7890")
node_1 = Node(contact_1.name, contact_1)
print(node_1.key)
print(node_1.value)
print(node_1.next)




class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        contact = Contact(key, value)

        if self.data[index] is None:
            self.data[index] = Node(key, contact)
            return

        current = self.data[index]

        while current:
            if current.key == key:
                current.value.number = value
                return

            if current.next is None:
                break

            current = current.next

        current.next = Node(key, contact)

    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def print_table(self):
        for i in range(self.size):
            print(f"Index {i}:", end=" ")

            current = self.data[i]

            if current is None:
                print("None")
                continue

            while current:
                print(f"[{current.value}]", end="")
                if current.next:
                    print(" -> ", end="")
                current = current.next

            print()

table = HashTable(10)
table.print_table()
table.insert("Alice", "123-456-7890")
table.insert("Bob", "987-654-3210")
table.insert("Alice", "111-222-3333")  # Update Alice's number)
table.print_table()

contact = table.search("Alice")
print("\nSearch Result:", contact)
print(table.search("Charlie"))  

# Test your hash table implementation here.  