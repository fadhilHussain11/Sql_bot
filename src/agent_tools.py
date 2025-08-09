from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain.agents.agent_types import AgentType


def generate_by_agent(db,llm,input):
    ## toolkit 
    toolkit = SQLDatabaseToolkit(db=db,llm=llm)
    agent = create_sql_agent(
        llm= llm,
        toolkit= toolkit,
        verbose=False,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        agent_executor_kwargs={
            "handle_parsing_errors" : True,
            "prefix":(
                "Answer briefly using the database. Do not show SQL."
              )
        }
    )
    response = agent.run(input)
    return response

