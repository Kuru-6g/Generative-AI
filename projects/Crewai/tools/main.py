import os
from crewai_tools import tool
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from langchain_openai import AzureChatOpenAI

os.environ["OTEL_SDK_DISABLED"] = "true"

load_dotenv()

azure_llm = AzureChatOpenAI(
    azure_deployment=os.environ.get("AZURE_OPENAI_DEPLOYMENT"), temperature=0.0
)


@tool
def get_account_id(name):
    """
    Retrieve the account ID based on the provided name.

    Args:
        name (str): The name of the customer.

    Returns:
        str: The account ID corresponding to the name, or "Name not found" if not found.
    """
    name_to_account_id = {
        "Alice": "A123",
        "Bob": "B456",
        "Charlie": "C789"
    }
    return name_to_account_id.get(name, "Name not found")


@tool
def get_last_bill_amount(account_id):
    """
    Retrieve the last bill amount based on the provided account ID.

    Args:
        account_id (str): The account ID of the customer.

    Returns:
        float: The last bill amount for the account, or "Account ID not found" if not found.
    """
    account_id_to_bill = {
        "A123": 120.50,
        "B456": 200.75,
        "C789": 99.99
    }
    return account_id_to_bill.get(account_id, "Account ID not found")


# Rest of your code remains the same
name = input("Enter name: ")

# Define your agents
billing_agent = Agent(
    role='Billing assistant',
    goal='Help with account ID and bill amount queries',
    backstory="""This agent is a helpful assistant that can retrieve the account id and the last bill amount for a customer. 
    Any other customer care requests are outside the scope of this agent""",
    verbose=True,
    allow_delegation=False,
    cache=False,
    llm=azure_llm,
    tools=[get_account_id, get_last_bill_amount]
)

function_executor_agent = Agent(
    role='Tool executor',
    goal='Execute tools and retrieve account ID and bill amount',
    backstory="""This agent executes all tools. 
    Anytime an agent needs information they will prompt this agent with the indicated function and arguments""",
    verbose=True,
    allow_delegation=True,
    cache=False,
    llm=azure_llm,
    tools=[get_account_id, get_last_bill_amount]
)


tool_execution_task = Task(
    description='Execute tools to retrieve account ID and bill amount',
    expected_output='Display the account IDs and corresponding bill amounts retrieved by the tools',
    agent=function_executor_agent,

)
# Define a new task that retrieves both account ID and bill amount
account_info_task = Task(
    description='Retrieve account ID and bill amount for a customer{name}',
    expected_output='Display the account ID and bill amount for the provided name',
    agent=billing_agent,
    human_input=True
)


# Define the logic for the new task
def get_account_info(name):
    account_id = get_account_id(name)
    if account_id == "Name not found":
        return "Name not found"
    bill_amount = get_last_bill_amount(account_id)
    return f"Account ID: {account_id}, Bill Amount: {bill_amount}"


# Update the crew to include the new task
crew = Crew(
    agents=[billing_agent, function_executor_agent],

    tasks=[account_info_task, tool_execution_task],
    process=Process.sequential,
    full_output=True,
    verbose=True,
    share_crew=False
)

# Kick off the crew and run the tasks
result = crew.kickoff()
print(result)