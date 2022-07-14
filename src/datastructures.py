
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class Family:

    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return random.randint(0, 99999999) 

    def add_member(self, member):
        self._members.append(member)

        pass

    def delete_member(self, id):
        for position in range(len(self._members)):
            if self._members[position]["id"] == id:
                self._members.pop(position)

    def update_member(self, id, member):
        ## you have to implement this method
        ## loop the list and replace the member with the given id
        pass

    def get_member(self, id):
        for m in self._members:
            if m["id"] == int(id):
                return m

        return None

    def get_all_members(self):
        return self._members
