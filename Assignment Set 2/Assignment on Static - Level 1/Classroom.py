
class Classroom:
    classroom_list = []

    @staticmethod
    def search_classroom(class_room):
        return 'Found' \
                    if class_room.upper() in map(str.upper, Classroom.classroom_list) \
                else -1

Classroom.classroom_list = ['G015', 'G066', 'L123', 'L135', 'L143', 'L13']
print(Classroom.search_classroom('l135'))