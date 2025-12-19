from sql_adapter import SQLAdapter
from pydantic_ai import ModelRetry
#from logger import RootLogger
import logging
from pyodbc import ProgrammingERror
import tiktoken

tokenizer = tiktoken.encoding_for_model("gpt-4o")

#logger = RootLogger(name=__name__).get()
logger = logging.getLogger(__name__)

async def pyodbc_rag_search(query:str)
  conn = SQLAdapter()
  logger.info(f"starting pyodbc rag search {query} ")
  try: result = conn.query(query)
  except ProgrammingError as e:
    logger.error(f"Query error {e} ")
    raise ModelRetry(f"Query failed with {e} ")
  token_count = len(tokenizer.encode(str(result)))
  logger.debug(f" token count {token_count} ")
  if token_count > 500:
    raise ModelRetry(f" retry with {token_count} ")
  logger.info(result)
  return result
