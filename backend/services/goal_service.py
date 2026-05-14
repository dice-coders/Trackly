from repository.goal_repository import GoalRepository
from schemas.goal_schemas import (GoalCreate, GoalUpdate, GoalResponse)
from models.goal_model import Goal
from typing import List

class GoalService :
    def __init__(self, repo: GoalRepository) :
        self.repo = repo
        
        
    def create_goal(self, schema: GoalCreate) -> Goal:
        goal = self.goal_create_to_model(schema)
        
        return self.repo.create_goal(goal)

    def get_goal(self, id: int) -> Goal:
        self.id_checker(id)
        return self.repo.get_goal(id)

    def list_goals(self) -> List[Goal]:
        return self.repo.list_goals()

    def update_goal(self, id: int, schema: GoalUpdate) -> Goal:
        self.id_checker(id)
            #Implementar validação de atributos nulos
        goal = self.goal_update_to_model(id, schema)
        updated = self.repo.update_goal(goal)
        return updated

    def delete_goal(self, id: int):
        self.id_checker(id)
        self.repo.delete_goal(id)



    def goal_create_to_model(self, schema: GoalCreate) -> Goal:
        goal = Goal(
            title = schema.title,
            description = schema.description,
            state = schema.state
        )
        return goal

    def goal_response_to_model(self, schema: GoalResponse) -> Goal:
        goal = Goal(
            title = schema.title,
            description = schema.description,
            state = schema.state
        )
        return goal

    def goal_update_to_model(self, id: int, schema: GoalUpdate) -> Goal:
        goal = Goal(
            title = schema.title,
            description = schema.description,
            state = schema.state,
            id = id
        )
        return goal

    def field_not_none_validate(self, id: int, data: GoalResponse) -> Goal:
        
        goal = self.repo.get_goal_by_id(id)
        new_data = self.goal_response_to_model(data)
        
        for field in ["title", "description", "state"]:
            value = getattr(new_data, field)

            if value is not None:
                setattr(goal, field, value)
        return goal

    def id_checker(self, id: int) :
        if id is not None :
            return id
