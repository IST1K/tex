from hard import Team


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    class Team:
        def __init__(self):
            self.team_members = []

        def add_member(self, emp):
            self.team_members.append(emp)

        def show_team(self):
            for emp in self.team_members:
                print(emp.name, emp.position)

    def display_info(self):
        print(f"Сотрудник: {self.name}, Должность: {self.position}")

sot1 = Employee("Иван Развожаев", "Менеджер")
sot1.display_info()

sot2 = Employee("Алексей Клян", "Разработчик")
sot2.display_info()
team = Team()
team.add_member(sot1)
team.add_member(sot2)
team.show_team()