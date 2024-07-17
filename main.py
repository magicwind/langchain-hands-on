from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from dotenv import load_dotenv
from langchain_core.messages import AIMessage
from langchain_core.output_parsers import XMLOutputParser

load_dotenv()

prompt = ChatPromptTemplate.from_template("请写一篇关于{topic}的中文小故事，不超过100个字")

model = ChatAnthropic(model='claude-3-haiku-20240307')

# chain = prompt | model
# resp: AIMessage = chain.invoke({"topic": "小白兔"})

# print(resp.content)

# print(resp.response_metadata)

# print(resp.usage_metadata)
actor_query = '随机生成一名中国的知名作家及其代表作'

parser = XMLOutputParser()

# print(parser.get_format_instructions())

prompt = PromptTemplate(
    template="{query}\n{format_instructions}",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain = prompt | model | parser

print(prompt.format(query=actor_query))

output = chain.invoke({"query": actor_query})

print(type(output))

print(output)

