import logging
from icecream import ic

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

model = OllamaLLM(model="llama3.1")


def parse_with_ollama(dom_chunks, parse_description):
    logger.debug("Starting parse_with_ollama function")
    ic("Starting parse_with_ollama function")
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        logger.debug(f"Processing chunk {i} of {len(dom_chunks)}")
        ic(f"Processing chunk {i} of {len(dom_chunks)}")
        try:
            logger.debug(f"Invoking Ollama model for chunk {i}")
            response = chain.invoke(
                {"dom_content": chunk, "parse_description": parse_description}
            )
            logger.debug(f"Received response for chunk {i}")
            ic(f"Parsed batch: {i} of {len(dom_chunks)}")
            parsed_results.append(response)
        except Exception as e:
            logger.error(f"Error processing chunk {i}: {str(e)}", exc_info=True)
            ic(f"Error processing chunk {i}: {str(e)}")

    logger.debug("Finished parse_with_ollama function")
    ic("Finished parse_with_ollama function")
    return "\n".join(parsed_results)
